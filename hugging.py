from transformers import AutoTokenizer, GPT2Tokenizer, GPT2Config, GPT2Model, GPT2LMHeadModel
from transformers import TrainingArguments
from transformers import Trainer
import torch
from transformers import DataCollatorForLanguageModeling

from datasets import load_dataset, Dataset

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

from pathlib import Path
data = (Path.cwd() / 'data/alan-watts/clean.txt').read_text()

step = 1024
data = [data[n:n+1024] for n in range(0, len(data), 1024)]

ds = Dataset.from_dict({'text': data})
ds = ds.map(lambda d: tokenizer(d["text"]), batched=False)

cfg = GPT2Config()

#  need to use this rather than GPT2Model
#  https://huggingface.co/transformers/model_doc/gpt2.html
model = GPT2LMHeadModel.from_pretrained("gpt2")

training_args = TrainingArguments(
    "test_trainer",
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
)


#  https://github.com/huggingface/notebooks/blob/master/examples/language_modeling.ipynb
dc = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False, pad_to_multiple_of=1024,
)

trainer = Trainer(
    model=model, args=training_args, train_dataset=ds, data_collator=dc
)

trainer.train()
