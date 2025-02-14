import streamlit as st
from services import job_api_service

def app():
    st.header("Job Listings")

    #Check user information
    if "job_title" in st.session_state:
        job_title = st.session_state["job_title"]
        job_location = st.session_state["job_location"]
    else:
        st.warning("Set up the job titles!")
        return

    #Show the jobs
    linkedin_company_insights = job_api_service.get_linkedin_company_insights("google") #Function does not exist
    st.write("Linkedin is the bestest", linkedin_company_insights)