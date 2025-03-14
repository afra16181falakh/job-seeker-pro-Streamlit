import streamlit as st
from services import job_api_service

def app():
    st.header("Job Listings")

    # Job search filters
    job_title = st.text_input("Job Title")
    job_location = st.text_input("Location")
    experience_level = st.selectbox("Experience Level", ["Any", "Entry", "Mid", "Senior"])
    salary_range = st.slider("Salary Range", 0, 200000, (0, 100000))
    remote_option = st.selectbox("Remote/Hybrid", ["Any", "Remote", "Hybrid", "On-site"])
    
    if st.button("Search Jobs"):
        # Call the job API service with the search parameters
        jobs = job_api_service.search_jobs(job_title, job_location, experience_level, salary_range, remote_option)
        if jobs:
            for job in jobs:
                st.write(f"**{job['title']}** at {job['company']}")
                st.write(f"Location: {job['location']}")
                st.write(f"Description: {job['description']}")
                st.write(f"Salary: {job.get('salary', 'Not specified')}")
                st.write(f"Experience Level: {job.get('experience_level', 'Not specified')}")
                st.write("---")
        else:
            st.warning("No jobs found matching your criteria.")
        if jobs:
            for job in jobs:
                st.write(f"**{job['title']}** at {job['company']}")
                st.write(f"Location: {job['location']}")
                st.write(f"Description: {job['description']}")
                st.write("---")
        else:
            st.warning("No jobs found matching your criteria.")

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
