# Creative Writing with GPT-2

[Get started quickly on Google Colab]().

The GPT series of language models from Open AI have revolutionized natural language processing.

This tool allows you to fine-tune GPT2 by training on text from your favourite authors.  You can then write together by inputting a prompt, seeing the resulting text and choosing whether to keep it or modify it.  An example of human and machine being creative together!

This repo provides:

- CLI to fine-tune GPT2 with a single `clean.txt` file,
- 13 `clean.txt` datasets for authors like Tolkien and Issac Assimov,
- a Streamlit app to interact & generate text with a fine-tuned model,


## Examples of Generated Text

For all examples below the model prompt is `He opened the door`.

### Harry Potter

> of the bookshop. Inside was a large glass raffle and over it sat a note. It said about Voldemort's defeat of the Dark Lord, and that "most troublesome thing which never occurred to Mr. Malfoy has been my one-night stand against him, in the main, against Voldemort, who always wanted to be chosen the new wizard of the school."Harry stopped and looked out the window at the sky. The sky and sea were now gray and gloomy. "All right,"

### Tolkien

and gasped with delight. The others then followed. 'You have been very generous!' he said. 'But don't you trust that Mr. Aragorn will take your husband as the heir?’ Gandalf was astonished. 'Yes, of course,' he said. 'But would you follow him wherever you went? He will tell you that he would stay in Bag End. And he will.’ He felt uneasy. 'No!’ said Fro

### Issac Asimov

and roared wildly: "And you all know that up there in the office are forty-three men of our Corporation, and when an employee or a member of one of our subsidiaries turns to one of them, that member may well want to disobey orders."    This warning wasn't useful, but we brought it back anyway. As one man put it, "We've moved the doors of the office to the foyer at intervals; therefore, the view is better. And an inside shot

### The Bible


## Generating Text

The best way to generate text from a model is to use the provided Streamlit app, which will provide access to models in `./models` (this will also download models from S3):

```shell
$ make app
```

If you just want to download pre-trained models from S3:

```shell
$ make pulls3
```


## Train

You can train your own model as well: 

```shell
$ python train.py harry
```
The command above will use data from `./data/harry/clean.txt` and save your model checkpoints & tokenizer in `./models/harry`.

```shell
$ python train.py --help

Usage: train.py [OPTIONS] AUTHOR

Options:
  --epochs INTEGER
  --base_model TEXT
  --help             Show this message and exit.
```

## Data

Datasets are setup by putting a `clean.txt` into `data/$AUTHOR_NAME`:

Training will look for a `clean.txt` file in `data/$AUTHOR/clean.txt` - this file should contain raw text - for example the `harry` dataset:

```shell
$ head -n 1 data/harry/clean.txt
Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you'd expect to be involved in anything strange or mysterious, because they just didn't hold with such nonsense.
```

I've included a few authors I like to write with:

```
$ tree -L 1 data
data
├── alan-watts
├── art-of-war
├── asimov
├── bible
├── harry
├── hemingway
├── mahabarta
├── meditations
├── plato
└── tolkien
```

You can also create mixtures of datasets by joining together text files, or by training the same model with multiple authors in series.
