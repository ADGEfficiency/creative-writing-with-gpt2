"""evaluate a fine-tuned model"""
from pathlib import Path

import click
import torch
from datasets import Dataset, load_dataset
from transformers import (AutoTokenizer, DataCollatorForLanguageModeling,
                          GPT2Config, GPT2LMHeadModel, GPT2Model,
                          GPT2Tokenizer, Trainer, TrainingArguments)


def evaluate(tokenizer, model, data, max_length=24):
    data = tokenizer(data, return_tensors="pt")
    out = model.generate(
        data["input_ids"], max_length=max_length, num_beams=5, no_repeat_ngram_size=2
    )
    return tokenizer.decode(
        out[0], skip_special_tokens=True, clean_up_tokenization_spaces=True
    )


def load_checkpoint(output_dir=None):
    if output_dir is not None:
        output_dir = Path(output_dir)
        tokenizer = GPT2Tokenizer.from_pretrained(output_dir.parent / "tokenizer")
        tokenizer.pad_token = tokenizer.eos_token
        return {
            "tokenizer": tokenizer,
            "mdl": GPT2LMHeadModel.from_pretrained(output_dir),
            "cfg": GPT2Config(),
        }
    else:

        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        tokenizer.pad_token = tokenizer.eos_token
        return {
            "tokenizer": tokenizer,
            "mdl": GPT2LMHeadModel.from_pretrained("gpt2"),
            "cfg": GPT2Config(),
        }


@click.command()
@click.argument("output_dir")
def cli(output_dir):
    model = load(output_dir)
    tokenizer = model["tokenizer"]
    model = model["model"]

    while True:
        print("Input:")
        request = input(">>> ")
        response = evaluate(tokenizer, model, request)
        print(response)


if __name__ == "__main__":
    cli()
