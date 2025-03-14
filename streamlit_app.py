import streamlit as st
from pages import home, profile_setup, job_listings

# Set the layout to wide mode for better use of screen space
st.set_page_config(layout="wide")

#Main App Loop
def main():
    #Set state for Authentication
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in'] == False:
        home.app()
    else:
        st.write("Welcome, %s" % st.session_state.name)
        sign_out = st.button("Sign Out")
        if sign_out:
            st.session_state["logged_in"] = False
            st.session_state["name"] = None
            st.write("You have signed out.")
        profile_setup.app()
        job_listings.app()

#Run Main entry point
if __name__ == "__main__":
    main()