st.title("LEGAL ASSITANT")

def read_uploaded_file(file):
    content = file.read()
    return content


uploaded_file = st.file_uploader("/content/sample_data/constitution of india.pdf")

if uploaded_file is not None:
    
    file_content = read_uploaded_file(uploaded_file)

   
    user_input = st.text_input("Enter the question", "")

    if st.button("Send"):
     
        bot_response = file_content[:200]  
        st.text("Bot:", bot_response)
