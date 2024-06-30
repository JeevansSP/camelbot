import streamlit as st

st.set_page_config(page_title='CamelBot - Chat with me', page_icon="🤖", layout='wide')
st.header('BOB Hackathon 2024 - Chat with me')
url = None
key = None

if "auth" not in st.session_state:
    st.session_state.auth = {}

if url is None or key is None:
    url = st.text_input("Asure URL")
    key = st.text_input("Enter API")

if url and key:
    st.session_state.auth['url'] = url
    st.session_state.auth['key'] = key
    st.page_link('pages/_Chat.py',label='Connect')

    
