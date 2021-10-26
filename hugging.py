from transformers import *
from transformers import AutoTokenizer
from transformers import TrainingArguments
from transformers import Trainer
import torch
from transformers import DataCollatorForLanguageModeling

from datasets import load_dataset

data = ["hi", "bye"]
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

dataset = load_dataset("text", data_files=["data/alan-watts/clean.txt"])
dataset = dataset.map(lambda d: tokenizer(d["text"]), batched=True)

#  https://github.com/huggingface/notebooks/blob/master/examples/language_modeling.ipynb
dc = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False, pad_to_multiple_of=1024
)

cfg = GPT2Config()

#  need to use this rather than GPT2Model
#  https://huggingface.co/transformers/model_doc/gpt2.html
model = GPT2LMHeadModel.from_pretrained("gpt2")

training_args = TrainingArguments("test_trainer")

trainer = Trainer(
    model=model, args=training_args, train_dataset=dataset["train"], data_collator=dc
)

trainer.train()
