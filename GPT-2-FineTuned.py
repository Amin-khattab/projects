from datasets import load_dataset
from transformers import GPT2Tokenizer,GPT2LMHeadModel,TrainingArguments,Trainer,pipeline

dataset = load_dataset("text",data_files={"train":"sarcastic_qa_dataset.txt"})

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

def preprocess(example):
    inputs =  tokenizer(example['text'], truncation=True, padding='max_length', max_length=128)
    inputs["labels"] = inputs["input_ids"].copy()
    return inputs

tokenized_dataset = dataset["train"].map(preprocess,batched=True)

model = GPT2LMHeadModel.from_pretrained("gpt2")
model.resize_token_embeddings(len(tokenizer))

training_args = TrainingArguments(
    output_dir="./GPT-2",
    per_device_train_batch_size=2,
    num_train_epochs=5,
    logging_steps=10,
    save_steps=50,
    save_total_limit=2,
    fp16=False
)

trainer = Trainer(
    model = model,
    train_dataset=tokenized_dataset,
    args =training_args,
    tokenizer = tokenizer
)

trainer.train()

model.save_pretrained("gpt2-finetuned")
tokenizer.save_pretrained("gpt2-finetuned")

generator = pipeline("text-generation",model="gpt2-finetuned",tokenizer="gpt2-finetuned")
print(generator("my name is", max_length = 50,num_return_sequences = 1))
