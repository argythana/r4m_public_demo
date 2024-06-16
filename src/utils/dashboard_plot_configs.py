import streamlit as st

from .demo_site_colors import color_template

# "Chart Option Name": key ["dataframe column name", "Chart Title", "Chart Y-Axis Title"]
chart_labels = {
    "Distance Challenge Progress": ["Challenge Progress", "Challenge Progress"],
    "Top 20 Leaderboard": ["Leaderbord", "Leaderboard", "Leaderboard"],
    "Active Users per day": ["users", "Active Users Daily", "Active Users Daily"],
    "Activities per day": ["acts", "Daily Activities", "Total Activities"],
    # "Progress Bar": ["Progress Bar", "Progress Bar"],
    "Distance per day": ["distance", "Daily Distance, Kms", "Distance"],
    "Activities Duration per day": [
        "duration",
        "Hours of activities per day",
        "Total Duration per day",
    ],
    "Total Distance": ["total_distance", "Total Distance, Kms", "Total Distance"],
    "Total Activities": ["total_activities", "Total Activities", "Total Activities"],
    "Total Duration": ["total_duration", "Total Duration, hours", "Total Duration"],
    "Unique Users": ["unique active users", "Unique Users", "Unique Active Users"],
    "Daily Activities Data Sample": ["Activities", "Activities", "Activities"],
}

chart_config = {
    "responsive": True,
    "displayModeBar": False,
    "scrollZoom": False,
    "doubleClick": False,
    "staticPlot": False,
}


common_axes_properties = {
    "tickcolor": color_template["ticks"],
    # "showticklabels": True,
    "ticks": "",
    "tickfont": dict(color=color_template["lines"]),
    "title_font": dict(color=color_template["lines"]),
}


common_layout_properties = {
    "plot_bgcolor": color_template["background"],
    "paper_bgcolor": color_template["background"],
    "dragmode": False,
    "hovermode": "x",
    # "margin": dict(l=5, r=5, b=5, t=35, pad=10),  # Adjust these values as needed
}


# Hide the Streamlit instructions about the input fields.
def hide_streamlit_instructions() -> None:
    st.markdown(
        """
        <style>
            div[data-testid="InputInstructions"] > span:nth-child(1) {
                visibility: hidden;
            }
        </style>
    """,
        unsafe_allow_html=True,
    )

    return None


# Hide the Streamlit menu and footer.
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .block-container
            {
                padding-top: 0.8rem;
                padding-bottom: 0rem;
                margin-top: 0.8rem;
                }
            </style>
            """
