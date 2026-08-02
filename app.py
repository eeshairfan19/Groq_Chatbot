import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Chatbot with Memory",
)

st.title("AI Chatbot with Memory")

client = Groq(
    api_key=st.secrets["GROQ_API_Key"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Reset Conversation"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages,
            )

            answer = response.choices[0].message.content

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )