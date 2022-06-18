from pathlib import Path

from transformers import AutoTokenizer, GPT2Tokenizer, GPT2Config, GPT2Model, GPT2LMHeadModel
from transformers import TrainingArguments
from transformers import Trainer
import torch
from transformers import DataCollatorForLanguageModeling

from datasets import load_dataset, Dataset

import click
from evaluate import evaluate, load


def train_gpt2(ds, output_dir, epochs, base_model=None):
    model = load(base_model)

    tokenizer = model['tokenizer']
    cfg = model['cfg']
    mdl = model['mdl']

    #  batched=True actually runs the map in batch - doesn't batch the data (was confusing!)
    ds = ds.map(lambda d: tokenizer(d["text"], truncation=True), batched=True)

    #  need to use this rather than GPT2Model
    #  https://huggingface.co/transformers/model_doc/gpt2.html
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        save_strategy="epoch",
        num_train_epochs=epochs
    )

    #  https://github.com/huggingface/notebooks/blob/master/examples/language_modeling.ipynb
    dc = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False, pad_to_multiple_of=1024,
    )

    trainer = Trainer(
        model=mdl, args=training_args, train_dataset=ds, data_collator=dc
    )
    trainer.train()
    tokenizer.save_pretrained(Path(output_dir) / 'tokenizer')


@click.command()
@click.argument('author')
@click.option('--epochs', default=3)
@click.option('--base_model', default=None)
def cli(author, epochs, base_model):
    data = (Path.cwd() / f'data/{author}/clean.txt').read_text()

    #  I wonder if I can not do this here...
    #  just pass in a big string to the DataCollator ?
    data = data.replace('\n', '')
    step = 1024
    data = [data[i:i+step] for i in range(0, len(data), step)]
    ds = Dataset.from_dict({'text': data})

    output_dir = Path().cwd() / f'models/{author}'
    train_gpt2(ds, output_dir, epochs=epochs, base_model=base_model)


if __name__ == '__main__':
    cli()
