# Creative writing with GPT2

[Quickly get started on Google Colab](https://colab.research.google.com/drive/1sNtF6Z9U_fXIIZHfJqpZVr_-vh3Ki8GN).

One of 2019's most important machine learning stories is the progress of using transfer learning on massive language models (such as Open AI'- GPT2 or Google's BERT).

We have been experimenting with retraining GPT2 on authors we like, and using the model as a writing partner. The process has been enlightening, and points towards a future where human and machine can write creatively together.

GPT-2 is not ready to write text on it's own - but with a bit of human supervision you can use the text it generates to write interesting text!  

GPT2 was originally trained on 40 GB of text from Wikipedia & news articles.  This library can be used to generate text with the base GPT2 model and to fine tune the base GPT2 model to text of your choosing.

This library wraps around the excellent Hugging Face Transformers library.  Two of the scripts have been copied into this repo - `run_generation` and `run_lm_finetuning`, [both of which can be found here](https://github.com/huggingface/transformers/tree/master/examples).

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

## To run locally

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
