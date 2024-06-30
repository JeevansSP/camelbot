
import streamlit as st
from chatAgent import ChatAgent

st.header("CamelBot 🤖")

if "auth" not in st.session_state:
    st.session_state.auth = {}
    st.error("Please connect to the API first by entering the Azure URL and API key.")


if st.session_state.auth:
    if "CamelBot" not in st.session_state:
        st.session_state.CamelBot = ChatAgent(api_key=st.session_state.auth['key'], base_url=st.session_state.auth['url'])
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        response = st.session_state.CamelBot.run('Hi')
        st.session_state.messages.append({'role': 'assistant', 'content': response})

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])

    prompt = st.chat_input("Enter message to send to server", key="message")
    if prompt:
        with st.chat_message('user'):
            st.markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        
        response = st.session_state.CamelBot.run(prompt)
        with st.chat_message('assistant'):
            st.markdown(response)
        st.session_state.messages.append({'role': 'assistant', 'content': response})
