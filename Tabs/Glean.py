import streamlit as st
import json

from .chat_styles import CHAT_STYLES

from DataBase.setup import *
from model_optimizer import ChangeModelType

with open("models_info.json", "r") as f:
    info = json.load(f)

def create_glean_page():
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Apply custom CSS
    st.markdown(CHAT_STYLES, unsafe_allow_html=True)

    # Display each message separately
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'''
            <div class="user-message">
                <div class="message-bubble user-bubble">{message["content"]}</div>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
            <div class="assistant-message">
                <div class="message-bubble assistant-bubble">{message["content"]}</div>
            </div>
            ''', unsafe_allow_html=True)

    # Chat input
    if prompt := st.chat_input("Type a word here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        ai_usage = st.session_state.ai_enabled

        if prompt.startswith(".set_ai"):
            st.session_state.ai_enabled = True
            response = f"Ai Model enabled. Currently using => {st.session_state.model_type}"
            st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt.startswith(".unset_ai"):
            st.session_state.ai_enabled = False
            response = "Ai Model disabled. using dictionary API for faster  lookups."
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        if prompt.startswith(".add"):
            use_internet = prompt.endswith('"use_internet"')
            use_ai = prompt.endswith('"use_ai"')

            promptValue = prompt.replace(".add", "").replace('"use_internet"', "").replace('"use_ai"', "").strip().strip('"')

            if use_internet:
                ai_usage = False
            elif use_ai:
                ai_usage = True
            else:
                ai_usage = st.session_state.ai_enabled

            promptMeaning = GrabingTheMeaning(promptValue, "add", ai_usage)
            response = f"{promptMeaning}"
            st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt.startswith(".meaning"):
            use_internet = prompt.endswith('"use_internet"')
            use_ai = prompt.endswith('"use_ai"')

            promptContent = prompt.replace(".meaning", "").replace('"use_internet"', "").replace('"use_ai"', "").strip().strip('"')
            
            if use_internet:
                ai_usage = False
            elif use_ai:
                ai_usage = True
            else:
                ai_usage = st.session_state.ai_enabled

            promptMeaning = GrabingTheMeaning(promptContent, "meaning", ai_usage)
            response = f"{promptMeaning}"
            st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt.startswith(".change_model"):
            parts = prompt.lower().split()
            requested = parts[-1]
            new_model_name = ChangeModelType(requested)
            response = f"{new_model_name}"
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        if prompt.startswith(".info"):
            parts = prompt.lower().split()
            promptPayload = info[parts[-1]]["description"]
            response = f"{promptPayload}"
            st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt.startswith(".model_options"):
            options = "\n".join([f"• {key}" for key in info.keys()])
            response = f"Avaible Models Are =>\n{options}"
            st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt.startswith(".status"):
            response = f""" Model Usage => {st.session_state.ai_enabled}\n\nCurrent Model => {st.session_state.model_type} """
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        if prompt.startswith(".show"):
            parts = prompt.replace(".show", "").strip().split()
    
            words = "words" in parts
            definitions = "definitions" in parts
    
            response = Listing(words, definitions)
            st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt.startswith(".del"):
            word = prompt.replace(".del", "").strip().strip('"')
            response = DeletingWord(word)
            st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt.startswith(".clear"):
            st.session_state.messages = []
            st.rerun()

        st.rerun()
