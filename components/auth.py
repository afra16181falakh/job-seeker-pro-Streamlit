import streamlit as st

def display_auth_status(message, success=True):
    """Displays an authentication status message with styling."""
    if success:
        st.success(message)
    else:
        st.error(message)

def logout_button():
    """Creates a logout button."""
    return st.button("Logout")

# If you have a custom sign-in form, you can put it here:
def sign_in_form():
    # Example (replace with your actual sign-in form)
    st.subheader("Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        # Perform authentication logic here (e.g., call a function from auth_service)
        st.write("Attempting to sign in...")