import streamlit as st
from services import auth_service
import firebase_admin
from firebase_admin import auth, credentials
import json

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate("path/to/your/firebase/credentials.json")
    firebase_admin.initialize_app(cred)

def app():
    st.title("Welcome to Job Seeker Pro")
    
    # Google Sign-In button
    if 'token' not in st.session_state:
        if st.button("Sign in with Google"):
            st.session_state['redirect_to_auth'] = True
            st.rerun()
    elif 'redirect_to_auth' in st.session_state and st.session_state['redirect_to_auth']:
        from pages import auth
        auth.app()
    else:
        try:
            # Verify the existing token
            auth_service.sign_in_with_google()
        except Exception as e:
            st.error(f"Error during sign-in: {str(e)}")
    
    # Display sign-in status
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.success(f"Welcome back, {st.session_state.get('name', 'User')}!")
