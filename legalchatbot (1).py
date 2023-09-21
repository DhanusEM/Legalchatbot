
import streamlit as st
import openai

st.title("LEGAL ASSITANT")

import streamlit as st
import openai


openai.api_key = "YOUR_API_KEY"

st.title("LEGAL ASSISTANT")

def generate_legal_answer(question, context):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose an appropriate engine
        prompt=f"Question: {question}\nContext: {context}\nAnswer:",
        max_tokens=200
    )
    return response.choices[0].text

uploaded_file = st.file_uploader("")

if uploaded_file is not None:
    file_content = read_uploaded_file(uploaded_file)
    user_input = st.text_input("Enter the question", "")

    if st.button("Send"):
        bot_response = generate_legal_answer(user_input, file_content[:500])
        st.text("Answer:", bot_response)
