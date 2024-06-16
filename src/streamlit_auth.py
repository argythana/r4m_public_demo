import hashlib

import streamlit as st

from utils.dashboard_plot_configs import hide_streamlit_instructions


def hash_password(password: str) -> str:
    """
    Hash the password.
    Args: password: string.
    Return: string.
    """
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_password() -> None:
    """
    Check the password for the public dashboard.
    return: None
    """

    # Define your username and password hash
    hide_streamlit_instructions()
    correct_username = st.secrets["username"]
    correct_password_hash = hash_password(st.secrets["password"])

    # Create placeholders for the login inputs and button
    username_placeholder = st.empty()
    password_placeholder = st.empty()
    button_placeholder = st.empty()
    custom_message_placeholder = st.empty()

    # Only display login inputs and button if the user is not authenticated
    if not st.session_state.get("authenticated", False):
        hide_streamlit_instructions()
        # Input fields
        username = username_placeholder.text_input("Username", key="username_input")
        password = password_placeholder.text_input(
            "Password",
            key="password_input",
            type="password",
        )

        # Check the password
        if button_placeholder.button("Login"):
            if (
                username == correct_username
                and hash_password(password) == correct_password_hash
            ):
                st.session_state["authenticated"] = True
                # Clear the placeholders after a successful login
                username_placeholder.empty()
                password_placeholder.empty()
                button_placeholder.empty()
                custom_message_placeholder.empty()
            else:
                st.error("Incorrect username or password.")
    return None
