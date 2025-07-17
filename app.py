import streamlit as st
from inference import chat_inference

st.title("Chat with Gemini AI - pro 2.5")
# input_text = st.text_input("Enter your message:")


if "messages" not in st.session_state:
    st.session_state.messages = []
        
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


prompt = st.chat_input("Enter your message: ")
if prompt:  
    # container respon dari AI
    response = chat_inference(prompt)
    with st.chat_message("assistant"):
        st.write(response)
    # st.write("Response:", response)
