from tensorflow.python.keras.utils.version_utils import training
from transformers import GPT2Tokenizer,GPT2LMHeadModel,Trainer,TrainingArguments,DataCollatorForLanguageModeling
from datasets import load_dataset
import time

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

model = GPT2LMHeadModel.from_pretrained("gpt2")

dataset = load_dataset("wikitext","wikitext-2-raw-v1",split="train")

def preprocess(example):
    return tokenizer(example["text"],padding="max_length",truncation=True,max_length=128)

tokenized_dataset = dataset.map(preprocess,batch_size=True)

datacollator = DataCollatorForLanguageModeling(mlm=False,tokenizer=tokenizer)

training_arguments = TrainingArguments(
    num_train_epochs=3,
    save_steps=1000,
    logging_steps=100,
    learning_rate=5e-5,
    per_device_train_batch_size=16,
    output_dir="./MY_GPT"
)

trainer = Trainer(
    args=training_arguments,
    data_collator=datacollator,
    model=model,
    train_dataset=tokenized_dataset
)

trainer.train()


#PIPELINE

import torch
from transformers import pipeline

chatbot = pipeline("text-generation",model="./MY_GPT",tokenizer="./MY_GPT")

print("input 'exit' or 'quit' to abbort")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit","quit"]:
        break

    response = chatbot(
        user_input,
        max_length = len(user_input) + 40,
        num_return_sequences = 1,
        do_sample=True,
        temperature=2.0,
        pad_token_id=50256
    )

    print("Bot: ", response[0])
