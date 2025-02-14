import streamlit as st
from services import resume_parser_service
from utils import helpers
import os

def app():
    st.header("Profile Setup")

    # Upload Resume
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "doc", "docx"])
    if uploaded_file is not None:
        #Save file to local storage
        with open(os.path.join("tempDir",uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())

        # Load resume
        st.success("Resume is successfully uploaded")
        st.session_state["resume"] = uploaded_file.name #Saves the file name for job_listing to call

    # Save job details
    job_title = st.text_input("Job Title")
    job_location = st.text_input("Job Location")
    if st.button("Save Details"):
        st.session_state["job_title"] = job_title
        st.session_state["job_location"] = job_location