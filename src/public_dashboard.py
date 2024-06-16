"""
Create a version of a "Challenge" Dashboard for the public demo.
"""

import sys

import streamlit as st

from streamlit_auth import check_password

# Import modules from src when run from a folder next to src.
sys.path.append("../src")

from utils.all_plots_from_df import create_all_charts_from_feather_file
from utils.dashboard_plot_configs import (
    hide_streamlit_instructions,
    hide_streamlit_style,
)

if __name__ == "__main__":
    # Request user authentication
    if "authenticated" not in st.session_state:
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        st.session_state["authenticated"] = False
        hide_streamlit_instructions()

    # Check password
    check_password()
    # Initialize session state
    if st.session_state["authenticated"]:
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        st.markdown(
            "<h5 style='text-align: center; color: #0693e3;'>Run4More <strong>analytics</strong> Demo</h5>",
            unsafe_allow_html=True,
        )

        # Dashboard from feather file
        create_all_charts_from_feather_file("./data/acts_by_date_trend.feather")

    else:
        st.info(
            "Please login by clicking on the Login button. Username: `r4m_worth`, Pwd: `$millions`."
        )
