"""fine-tune a model"""
from pathlib import Path

import click
import torch
from datasets import Dataset, load_dataset
from transformers import (AutoTokenizer, DataCollatorForLanguageModeling,
                          GPT2Config, GPT2LMHeadModel, GPT2Model,
                          GPT2Tokenizer, Trainer, TrainingArguments)

from creative.evaluate import evaluate, load_checkpoint


def train_gpt2(ds: Dataset, output_dir: Path, epochs: int, base_model:str=None) -> None:
    model = load_checkpoint(base_model)

    tokenizer = model["tokenizer"]
    cfg = model["cfg"]
    mdl = model["mdl"]

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
        num_train_epochs=epochs,
    )

    #  https://github.com/huggingface/notebooks/blob/master/examples/language_modeling.ipynb
    dc = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
        pad_to_multiple_of=1024,
    )

    trainer = Trainer(model=mdl, args=training_args, train_dataset=ds, data_collator=dc)
    trainer.train()
    tokenizer.save_pretrained(output_dir / "tokenizer")


def main(author: str, epochs: int, base_model: str = None) -> None:
    data = Path(f"./data/{author}/clean.txt").read_text()
    data = data.replace("\n", " ")
    step = 1024
    data = [data[i : i + step] for i in range(0, len(data), step)]
    ds = Dataset.from_dict({"text": data[:2]})
    output_dir = Path(f"./models/{author}")
    train_gpt2(ds, output_dir, epochs=epochs, base_model=base_model)


@click.command()
@click.argument("author")
@click.option("--epochs", default=3)
@click.option("--base_model", default=None)
def cli(author:str, epochs:int, base_model:str) -> None:
    main(author, epochs, base_model)


if __name__ == "__main__":
    cli()
