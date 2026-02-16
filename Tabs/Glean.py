import streamlit as st
from .chat_styles import CHAT_STYLES

def create_glean_page():
    """Create a chat interface page"""
    
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
        response = f"{prompt}"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
