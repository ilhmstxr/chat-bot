import streamlit as st
from inference import chat_inference

st.title("Chat with Gemini AI - pro 2.5")
# input_text = st.text_input("Enter your message:")

# menyimpan pesan ke dalam session state
if "messages" not in st.session_state:
    st.session_state.messages = []
        
# menyimpan pesan ke dalam session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# menuliskan pesan 
prompt = st.chat_input("Enter your message: ", accept_file=True, file_type=["jpg", "jpeg", "png"])

if prompt:
    # Gabungkan text dan file jika keduanya ada
    if prompt.text and prompt.files:
        uploaded_file = prompt.files[0]
        with st.chat_message("user"):
            st.markdown("input text: " + prompt.text)
            st.markdown("input image: " + uploaded_file.name)
            st.image(uploaded_file)
        st.session_state.messages.append({
            "role": "user",
            "content": f"{prompt.text}\n[Image: {uploaded_file.name}]"
        })

        # response dari ai (contoh: text + image)
        response = chat_inference(prompt.text)
        with st.chat_message("assistant"):
            st.markdown("response text: " + response)
            st.markdown("response image:")
            st.image(uploaded_file)
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"{response}\n[Image: {uploaded_file.name}]"
        })

    # Hanya text
    elif prompt.text:
        response = chat_inference(prompt.text)
        with st.chat_message("user"):
            st.markdown("input text: " + prompt.text)
        st.session_state.messages.append({"role": "user", "content": prompt.text})
        with st.chat_message("assistant"):
            st.markdown("response text: " + response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Hanya file
    elif prompt.files:
        uploaded_file = prompt.files[0]
        with st.chat_message("user"):
            st.markdown("input image: " + uploaded_file.name)
            st.image(uploaded_file)
        st.session_state.messages.append({"role": "user", "content": f"[Image: {uploaded_file.name}]"})
        with st.chat_message("assistant"):
            st.markdown("response image:")
            st.image(uploaded_file)
        st.session_state.messages.append({"role": "assistant", "content": f"[Image: {uploaded_file.name}]"})

