# Creative writing with GPT-2

[Quickly get started with a notebook on Google Colab](https://colab.research.google.com/drive/1sNtF6Z9U_fXIIZHfJqpZVr_-vh3Ki8GN).

One of 2019's most important machine learning stories is the progress of using transfer learning on massive language models.

I have been experimenting with retraining GPT-2 on authors we like, and using the model as a writing partner. The process has been enlightening, and points towards a future where human and machine can write creatively together.

[You can see examples of text generation from some of the finetuned models here](https://github.com/ADGEfficiency/creative-writing-with-gpt2/tree/master/examples/).

Dependencies
- [Hugging Face Transformers](https://github.com/huggingface/transformers) at version [2.2.1](https://github.com/huggingface/transformers/tree/v2.2.1) - I wrap around `examples/run_generation.py` and `examples/run_lm_finetuning.py` (these no longer exist in the same place in later versions of HuggingFace)
- [googledrivedownloader](https://github.com/ndrplz/google-drive-downloader) to get pre fine-tuned models from my GoogleDrive


## How to write creatively with GPT-2

GPT-2 is not ready to write text on it's own - but with a bit of human supervision you can use the text it generates to write interesting text!  

Be fair to your machine colleague, if a sentence can work without modification, use it. Don't be afraid to correct it.  Typical mistakes are repetition of the same object in different forms

GPT-2 was originally trained on 40 GB of text from Wikipedia & news articles.  This library can be used to generate text with the base GPT-2 model and to fine tune the base GPT-2 model to text of your choosing.

The library has a number of datasets in `creative-writing-with-gpt2/data`.  A dataset is defined as a text file called `clean.txt` - for example `asimov/clean.txt`.

```
$ tree -L 1 creative-writing-with-gpt2/data
creative-writing-with-gpt2/data
├── alan-watts
├── asimov
├── bible
├── harry
├── hemingway
├── mahabarta
├── meditations
├── plato
└── tolkien
```

A number of pre-fine-tuned models are available in `creative-writing-with-gpt2/models.py` - you can download them to your machine by running `python models.py`.

## Run on Colab

The recommended way to interact with this repo is [through this Google Colab notebook](https://colab.research.google.com/drive/1sNtF6Z9U_fXIIZHfJqpZVr_-vh3Ki8GN) - the free GPU is useful for fine-tuning.

## Run locally

```bash
git clone https://github.com/ADGEfficiency/creative-writing-with-gpt2
cd creative-writing-with-gpt2
pip install -r requirements.txt
python models.py
```

To run the text generation with fine-tuned model (either downloaded from running `python gdrive_models.py` or from training yourself.

```bash
python run_generation.py \
  --model_type=gpt2 \
  --model_name_or_path="./models/tolkien" \
  --length=200
```

```bash
python run_lm_finetuning.py \
  --output_dir="./models/harry" \
  --model_type=gpt2 \
  --model_name_or_path=gpt2 \
  --do_train \
  --train_data_file="./data/harry/clean.txt" \
  --num_train_epochs=4 \
  --overwrite_output_dir \
  --save_steps 10000
```

To run the text generation with the base GPT2 model:

```bash
python run_generation.py \
  --model_type=gpt2 \
  --model_name_or_path="models/gpt2" \
  --length=200
```

## Further reading

[Allen Institute for Artificial Intelligence GPT-2 Explorer](https://gpt2.apps.allenai.org/?text=Joel%20is)

[huggingface/transformers](https://github.com/huggingface/transformers)

[The Illustrated GPT-2 - Visualizing Transformer Language Models](http://jalammar.github.io/illustrated-gpt2/)

[The State of Transfer Learning in NLP](https://ruder.io/state-of-transfer-learning-in-nlp/)
