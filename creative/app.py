"""streamlit application to interact with fine-tuned GPT2 models"""
from pathlib import Path

import streamlit as st
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Model, GPT2Tokenizer

from creative.evaluate import evaluate, load_checkpoint
from creative.load import load_last_checkpoint, load_models


@st.cache(allow_output_mutation=True)
def hist(data=[]):
    """cache the history of prompts and responses"""
    return data


if __name__ == "__main__":
    models = load_models()
    base = models[0].parent
    model_names = [m.name for m in models]
    model = st.selectbox("model", model_names)
    model = base / model

    checkpoint = load_last_checkpoint(model)
    model = load_checkpoint(checkpoint)
    tokenizer = model["tokenizer"]
    model = model["mdl"]

    history = hist()
    max_length = st.sidebar.number_input(
        "max-length", value=256, min_value=0, max_value=1024, step=32
    )

    prompt = st.text_input("Prompt")
    if prompt:
        response = evaluate(tokenizer, model, prompt, max_length=max_length)
        history.append({"prompt": prompt, "response": response.replace(prompt, "")})

        for th in history[::-1]:
            st.json(th)
