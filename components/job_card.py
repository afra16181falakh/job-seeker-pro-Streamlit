import streamlit as st

def job_card(job):
    """Displays a job card with formatted information."""
    st.subheader(job["title"])
    st.write(f"Company: {job['company']}")
    st.write(f"Location: {job['location']}")
    st.write(f"Description: {job['description']}")
    st.write(f"Salary: {job.get('salary', 'Not specified')}")
    st.write(f"Experience Level: {job.get('experience_level', 'Not specified')}")
    #st.markdown(f"[Apply Now]({job['link']})")  # Use st.markdown for links
    st.write("---")  # Separator
