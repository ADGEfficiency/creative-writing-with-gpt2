from pathlib import Path
import streamlit as st

from evaluate import evaluate
from transformers import AutoTokenizer, GPT2Tokenizer, GPT2Config, GPT2Model, GPT2LMHeadModel

from evaluate import load

@st.cache(allow_output_mutation=True)
def hist(data=[]):
    return data

models = [p for p in (Path().cwd() / 'models').iterdir() if p.is_dir()]
model = st.selectbox('model', models)

checkpoints = [p for p in model.iterdir() if p.is_dir() and 'checkpoint' in str(p)]

if len(checkpoints) == 0:
    "No checkpoint found"

else:

    checkpoint = list(sorted(checkpoints))[-1]
    model = load(checkpoint)
    tokenizer = model['tokenizer']
    model = model['mdl']

    history = hist()
    max_length = st.sidebar.number_input('max-length', value=256, min_value=0, max_value=1024, step=32)

    prompt = st.text_input('Prompt')

    if prompt:
        response = evaluate(tokenizer, model, prompt, max_length=max_length)
        history.append({
            'prompt': prompt,
            'response': response.replace(prompt, '')
        })

        for th in history[::-1]:
            st.json(th)
