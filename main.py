import openai
import streamlit as st
from streamlit_option_menu import option_menu

# importing all the tabs python files =>
from Tabs import Glean

from header_style import (
    MENU_STYLES,
    GLASS_DIVIDER_HTML,
    LOGO_HTML,
)

default_model = "kimi-k2.5"

# Initializing the model type =>
if "model_type" not in st.session_state:
    st.session_state.model_type = default_model

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
