
from pathlib import Path

from transformers import AutoTokenizer, GPT2Tokenizer, GPT2Config, GPT2Model, GPT2LMHeadModel
from transformers import TrainingArguments
from transformers import Trainer
import torch
from transformers import DataCollatorForLanguageModeling

from datasets import load_dataset, Dataset
import click


def evaluate(tokenizer, model, data, max_length=24):
    data = tokenizer(data, return_tensors='pt')
    out = model.generate(data['input_ids'], max_length=max_length, num_beams=5, no_repeat_ngram_size=2)
    return tokenizer.decode(out[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)


def load(output_dir=None):

    if output_dir is not None:
        output_dir = Path(output_dir)
        tokenizer = GPT2Tokenizer.from_pretrained(output_dir.parent / 'tokenizer')
        tokenizer.pad_token = tokenizer.eos_token
        return {
            'tokenizer': tokenizer,
            'mdl': GPT2LMHeadModel.from_pretrained(output_dir),
            'cfg': GPT2Config()
        }
    else:

        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        tokenizer.pad_token = tokenizer.eos_token
        return {
            'tokenizer': tokenizer,
            'mdl': GPT2LMHeadModel.from_pretrained('gpt2'),
            'cfg': GPT2Config()
        }


@click.command()
@click.argument('output_dir')
def cli(output_dir):

    model = load(output_dir)
    tokenizer = model['tokenizer']
    model = model['model']

    while True:
        print('Input:')
        request = input(">>> ")
        response = evaluate(tokenizer, model, request)
        print(response)


if __name__ == '__main__':
    cli()
