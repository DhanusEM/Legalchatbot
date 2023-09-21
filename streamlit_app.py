import streamlit as st
import openai


openai.api_key = "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"

st.title(" Legal Assistant")

def generate_legal_answer(question, context, language="en"):
    prompt = f"Question ({language}): {question}\nContext ({language}): {context}\nAnswer:"
    response = openai.Completion.create(
        engine="davinci",  
        prompt=prompt,
        max_tokens=250,  
        temperature=0.7,  
    )
    return response.choices[0].text

uploaded_file = st.file_uploader("/content/sample_data/constitution of india.pdf")

if uploaded_file is not None:
    file_content = st.read_uploaded_file(uploaded_file)
    user_input = st.text_input("Enter the question", "")
    selected_language = st.selectbox("Select Language", ["English", "தமிழ்"])

    if st.button("Send"):
        if selected_language == "English":
            bot_response = generate_legal_answer(user_input, file_content[:500], "en")
        elif selected_language == "தமிழ்":
            bot_response = generate_legal_answer(user_input, file_content[:500], "ta")
        else:
            bot_response = "Language not supported."

        st.text("Answer:", bot_response),
