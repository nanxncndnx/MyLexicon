import streamlit as st
import openai

import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
default_model = "kimi-k2.5"

# Loading the models informations =>
with open("models_info.json", "r") as f:
    MODELS = json.load(f)

# Initializing the model type =>
if "model_type" not in st.session_state:
    st.session_state.model_type = default_model

def ChangeModelType(model_name):
    if model_name in MODELS:
        st.session_state.model_type = model_name
        return f"The model successfully changed to {model_name}"
    else:
        return """ Unknown model! \n avaible models currently are : \n kimi-k2.5 \n qwen \n deepseek-v3.2 \n glm4.7 """

def WakeUpModel(word):

    client = openai.OpenAI(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = API_KEY
    )

    response = client.chat.completions.create(
        model=MODELS[st.session_state.model_type]["model_id"],
        messages=[{"role": "user", "content": f"just define the word {word} very friendly and short like a translate in english no more and less information and talk just the meaning"}]
    )

    res = response.choices[0].message.content
    return res
