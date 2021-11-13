
from pathlib import Path

from transformers import AutoTokenizer, GPT2Tokenizer, GPT2Config, GPT2Model, GPT2LMHeadModel
from transformers import TrainingArguments
from transformers import Trainer
import torch
from transformers import DataCollatorForLanguageModeling

from datasets import load_dataset, Dataset


def evaluate(tokenizer, model):
    data = "Hello to you GPT2"
    data = tokenizer(data, return_tensors='pt')
    out = model.generate(data['input_ids'], max_length=1024, num_beams=5, no_repeat_ngram_size=2)
    print(tokenizer.decode(out[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))


# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# tokenizer.pad_token = tokenizer.eos_token
# model = GPT2LMHeadModel.from_pretrained('gpt2')
# evaluate(tokenizer, model)

tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')
model = GPT2LMHeadModel.from_pretrained("test_trainer/checkpoint-321")
evaluate(tokenizer, model)
