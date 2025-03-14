import streamlit as st
from services import resume_parser_service
from utils import helpers
import os

def app():
    st.header("Profile Setup")

    # Upload Resume
    if not os.path.exists("tempDir"):
        os.makedirs("tempDir")  # Ensure the temporary directory exists
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "doc", "docx"])
    if uploaded_file is not None:
        # Save file to local storage
        with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
            f.write((uploaded_file).getbuffer())

        # Parse the uploaded resume
        parsed_data = resume_parser_service.parse_resume(os.path.join("tempDir", uploaded_file.name))
        if parsed_data:
            st.success("Resume is successfully uploaded and parsed")
            # Populate user profile with parsed data
            st.session_state["name"] = parsed_data.get("personal_info", {}).get("name")
            st.session_state["email"] = parsed_data.get("personal_info", {}).get("email")
            st.session_state["work_experience"] = parsed_data.get("work_experience", [])
            st.session_state["education"] = parsed_data.get("education", [])
        else:
            st.error("Failed to parse the resume. Please try again.")

    # Save job details
    job_title = st.text_input("Job Title")
    job_location = st.text_input("Job Location")
    if st.button("Save Details"):
        st.session_state["job_title"] = job_title
        st.session_state["job_location"] = job_location
