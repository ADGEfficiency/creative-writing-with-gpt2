# Creative writing with GPT2

https://colab.research.google.com/drive/1sNtF6Z9U_fXIIZHfJqpZVr_-vh3Ki8GN

GPT-2 is not ready to write text on it's own - but with a bit of human supervision you can use the text it generates to write interesting text!  

GPT2 was originally trained on 40 GB of text from Wikipedia & news articles.  We can take the raw

This library wraps around the excellent Hugging Face Transformers library.  Two of the scripts have been copied into this repo - `run_generation` and `run_lm_finetuning`.  

The recommended way to interact with this repo is [through this Google Colab notebook](https://colab.research.google.com/drive/1sNtF6Z9U_fXIIZHfJqpZVr_-vh3Ki8GN) - the free GPU is useful for training.

To run locally:

```bash
pip install -r requirements.txt
python gdrive_models.py
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

