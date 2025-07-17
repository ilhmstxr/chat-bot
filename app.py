import streamlit as st
from inference import chat_inference
from datetime import datetime  # Tambahkan ini

st.title("Chat with Gemini AI - pro 2.5")

if "messages" not in st.session_state:
    st.session_state.messages = []

# tampilkan pesan sebelumnya beserta waktu
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "time" in message:
            st.caption(f"Sent at: {message['time']}")

prompt = st.chat_input("Enter your message: ", accept_file=True, file_type=["jpg", "jpeg", "png"])

if prompt:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Gabungkan text dan file jika keduanya ada
    if prompt.text and prompt.files:
        uploaded_file = prompt.files[0]
        with st.chat_message("user"):
            st.markdown(prompt.text)
            st.markdown(uploaded_file.name)
            st.image(uploaded_file)
            st.caption(f"Sent at: {now}")
        st.session_state.messages.append({
            "role": "user",
            "content": f"{prompt.text}\n[Image: {uploaded_file.name}]",
            "time": now
        })

        response = chat_inference(prompt.text)
        now_resp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with st.chat_message("assistant"):
            st.markdown(response)
            # st.markdown("response image:")
            st.image(uploaded_file)
            st.caption(f"Sent at: {now_resp}")
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"{response}\n[Image: {uploaded_file.name}]",
            "time": now_resp
        })

    elif prompt.text:
        with st.chat_message("user"):
            st.markdown(prompt.text)
            st.caption(f"Sent at: {now}")
        st.session_state.messages.append({"role": "user", "content": prompt.text, "time": now})
        response = chat_inference(prompt.text)
        now_resp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with st.chat_message("assistant"):
            st.markdown(response)
            st.caption(f"Sent at: {now_resp}")
        st.session_state.messages.append({"role": "assistant", "content": response, "time": now_resp})

    elif prompt.files:
        uploaded_file = prompt.files[0]
        with st.chat_message("user"):
            st.markdown(uploaded_file.name)
            st.image(uploaded_file)
            st.caption(f"Sent at: {now}")
        st.session_state.messages.append({"role": "user", "content": f"[Image: {uploaded_file.name}]", "time": now})
        with st.chat_message("assistant"):
            # st.markdown("response image:")
            st.image(uploaded_file)
            st.caption(f"Sent at: {now}")
        st.session_state.messages.append({"role": "assistant", "content": f"[Image: {uploaded_file.name}]", "time": now})

