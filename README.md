# Creative Writing with GPT2

The GPT series of generative models have revolutionized natural language processing.

The most advanced models are only available through paid APIs - for GPT2 the model weights are openly available. This means we can fine-tune GPT2 ourselves!

# Use

## Generating Text

A Streamlit app allows text generation with fine-tuned models in `./models`:

```shell
$ make app
```

The `make app` command will also pull previously fine-tuned models from S3.


## Fine Tuning

You can fine tune your own models using the command below - this will train on GPU if available:

```shell
$ python creative/train.py harry
```

This will use the text from `./data/harry/clean.txt` and output a model to `./models/harry`:

```shell
$ tree ./models/harry
```

You can then interact with this model through the Streamlit application.


# Examples

All examples below are generated with the model prompt `He opened the door`.

## Harry Potter

> of the bookshop. Inside was a large glass raffle and over it sat a note. It said about Voldemort's defeat of the Dark Lord, and that "most troublesome thing which never occurred to Mr. Malfoy has been my one-night stand against him, in the main, against Voldemort, who always wanted to be chosen the new wizard of the school."Harry stopped and looked out the window at the sky. The sky and sea were now gray and gloomy. "All right,"

## Tolkien

> and gasped with delight. The others then followed. 'You have been very generous!' he said. 'But don't you trust that Mr. Aragorn will take your husband as the heir?’ Gandalf was astonished. 'Yes, of course,' he said. 'But would you follow him wherever you went? He will tell you that he would stay in Bag End. And he will.’ He felt uneasy. 'No!’ said Fro

## Issac Asimov

> and roared wildly: "And you all know that up there in the office are forty-three men of our Corporation, and when an employee or a member of one of our subsidiaries turns to one of them, that member may well want to disobey orders."    This warning wasn't useful, but we brought it back anyway. As one man put it, "We've moved the doors of the office to the foyer at intervals; therefore, the view is better. And an inside shot

## Alan Watts / Art of War / Mahabarta Blend

>  of his house, and beholding a beautiful lady of beautiful features, he addressed her, saying,--Welcome, dear lady, to thy house. Do thou tell me, O son of Kunti, what the merits are that attach to gifts of kine. I shall, therefore, tell thee what is the merit that attaches to the gift of a cow. It behoveth thee to discourse to me on this topic."Bhishma continued, Hearing these words of the illustrious Rishi, the lady became filled with joy. She then addressed him in the following words:--O thou that art conversant with the Vedas, I desire to hear thee discourse on the topic of gifts. In this connection is recited the old narrative of an old discourse between a Brahmana and a Kshatriya. The discourse took place in days of yore between the Rishis of old and the Sudras of modern times. One of them, viz., a Sudra, having obtained a son by the name of Vasishtha, solicited his kinsmen to give him up for adoption into the kingly order. Having obtained his son from the son-in-law of that king who had obtained him from his own kins"


# Data

Training will look for a `clean.txt` file in `data/$AUTHOR/clean.txt` - this file should contain raw text - for example the `harry` dataset:

```shell
$ head -n 1 data/harry/clean.txt
Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you'd expect to be involved in anything strange or mysterious, because they just didn't hold with such nonsense.
```

I've included a few authors I like to write with:

```shell
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

You can also create mixtures and blends by combining multiple authors into a single `clean.txt` file.
