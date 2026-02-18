import openai
import streamlit as st
from streamlit_option_menu import option_menu

import os
from dotenv import load_dotenv

# importing all the tabs python files =>
from Tabs import Glean

from header_style import (
    MENU_STYLES,
    GLASS_DIVIDER_HTML,
    LOGO_HTML,
)


# Catching the answer from the kimi-k2.5 =>
def WakeUpModel(word):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    
    client = openai.OpenAI(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = API_KEY
    )

    response = client.chat.completions.create(
        model="moonshotai/kimi-k2.5",
        messages=[{"role": "user", "content": f"just define the word {word} very friendly and short like a translate in english no more and less information and talk just the meaning"}]
    )

    res = response.choices[0].message.content
    return res

# Logo of App =>
st.markdown(LOGO_HTML, unsafe_allow_html=True)

# Navigation Menu
navbar = option_menu(
    menu_title=None,
    options=['What is it', 'Glean', 'Vault', 'Forge'], 
    icons=['question-lg', 'database-fill-add', 'safe', 'hammer'], 
    default_index=0,
    orientation="horizontal",
    styles=MENU_STYLES,
    key="main_navbar"
)

# Glass Divider
st.markdown(GLASS_DIVIDER_HTML, unsafe_allow_html=True)

if navbar == "Glean":
    Glean.create_glean_page()
