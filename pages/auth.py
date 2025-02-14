import streamlit as st
from services import auth_service

def app():
    st.title("Sign In with Google")
    
    st.markdown("""
        <script src="https://accounts.google.com/gsi/client" async defer></script>
        <div id="g_id_onload"
            data-client_id="359866608188-9hq8i78khcfutmlnco3ae6uv8bjv4tmg.apps.googleusercontent.com"
            data-callback="handleCredentialResponse"
            data-auto_prompt="false">
        </div>
        <div class="g_id_signin" 
             data-type="standard"
             data-theme="filled_blue"
             data-size="large"
             data-text="sign_in_with"
             data-shape="rectangular"
             data-logo_alignment="left">
        </div>
        <script>
        function handleCredentialResponse(response) {
            const token = response.credential;
            window.location.href = window.location.origin + "/?token=" + token;
        }
        </script>
    """, unsafe_allow_html=True)
