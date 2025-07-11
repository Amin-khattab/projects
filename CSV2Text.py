import pandas as pd
from datasets import Dataset
from transformers import T5Tokenizer
from transformers import T5ForConditionalGeneration,TrainingArguments,Trainer
import torch

device = torch.device("mps" if torch.has_mps else "cpu")

df = pd.read_csv("training_pairs.csv")

dataset = Dataset.from_pandas(df)

tokenizer = T5Tokenizer.from_pretrained('t5-small')

def preprocess(example):
    input_text = "generate:" + example['input']
    target_text = example['output']

    model_input =tokenizer(input_text, truncation=True, padding ='max_length', max_length=64)
    label = tokenizer(target_text, truncation=True, padding ='max_length', max_length=64)

    model_input["labels"] = label["input_ids"]
    return model_input

tokenized_dataset = dataset.map(preprocess,remove_columns=dataset.column_names)

model = T5ForConditionalGeneration.from_pretrained('t5-small').to(device)

training_args = TrainingArguments(output_dir='./t5-output',
                                per_device_train_batch_size=4,
                                  num_train_epochs=20,
                                  logging_steps=5,
                                  save_steps=20,
                                  save_total_limit=1,
                                  remove_unused_columns= False
                                  )

trainer = Trainer(
    model = model,
    args = training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer
)

trainer.train()


def generate_text(input_str):

    input_ids = tokenizer("generate:" + input_str, return_tensors ="pt").input_ids.to(device)
    output_ids = model.generate(input_ids,max_length=64)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

print(generate_text("Name=Amin;Age=18;Job=AIE;Location=kurdistan"))
