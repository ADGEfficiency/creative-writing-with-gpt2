from pathlib import Path

import streamlit as st
from transformers import GPT2Tokenizer, GPT2Config, GPT2Model, GPT2LMHeadModel

from creative.evaluate import evaluate, load_checkpoint


@st.cache(allow_output_mutation=True)
def hist(data=[]):
    return data


def load_models(base: Path=Path.cwd()):
    return [p for p in (base / 'models').iterdir() if p.is_dir()]

def get_last_checkpoint(model):
    checkpoints = [p for p in model.iterdir() if p.is_dir() and 'checkpoint' in str(p)]
    assert len(checkpoints) > 0, "No checkpoint found!"
    return list(sorted(checkpoints))[-1]

if __name__ == '__main__':
    models = load_models()
    model = st.selectbox('model', models)

    checkpoint = get_last_checkpoint(model)

    model = load_checkpoint(checkpoint)
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
