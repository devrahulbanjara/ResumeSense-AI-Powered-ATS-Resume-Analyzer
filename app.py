import os
import streamlit as st
from dotenv import load_dotenv
from utils.pdf_processing import input_pdf_setup
from utils.resume_evaluation import evaluate_resume_fit, evaluate_percentage_match

# Load environment variables
load_dotenv()

# Streamlit UI setup
st.set_page_config(page_title="ATS Resume Expert")
st.header("Resume Sense")

# User input fields
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# Buttons for actions
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

# Handle submit buttons
if submit1:
    if uploaded_file is not None:
        # Convert uploaded resume PDF to image
        pdf_content = input_pdf_setup(uploaded_file)
        response = evaluate_resume_fit(input_text, pdf_content)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume.")

elif submit3:
    if uploaded_file is not None:
        # Convert uploaded resume PDF to image
        pdf_content = input_pdf_setup(uploaded_file)
        response = evaluate_percentage_match(input_text, pdf_content)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume.")
