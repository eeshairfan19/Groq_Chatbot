import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Chatbot with Memory",
)

st.title("AI Chatbot with Memory")

client = Groq(
    api_key=st.secrets["GROQ_API_Key"]
)

question = st.text_area(
    "Ask a question:",
    height=150,
)

if st.button("Generate Response"):

    if question.strip():

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
        {
            "role": "user",
            "content": question,
        }
            ],
            )

        st.success(response.choices[0].message.content)

    else:
        st.warning("Please enter a question.")