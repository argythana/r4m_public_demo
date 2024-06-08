from typing import Any, Dict

from demo_streamlit_colors import color_template

PLOTS_LABELS = {
    # chart_y: [chart title, y-axis title
    "acts": ["Activities", "Total Activities"],
    "Challenge Progress": ["Challenge Progress", "Challenge Progress"],
    "Leaderboard": ["Leaderboard", "Leaderboard"],
    # "Progress Bar": ["Progress Bar", "Progress Bar"],
    "Daily Distance": ["Daily Distance, kilometers", "Distance"],
    "Total Distance": ["Total Distance", "Total Distance"],
    "Total Activities": ["Total Activities", "Total Activities"],
    "Active Users Daily": ["Active Users Daily", "Active Users Daily"],
    "Unique Active Users": ["Unique Active Users", "Unique Active Users"],
    # "Duration": ["Duration", "Total Duration By Day"],
    # "Total Duration": ["Total Duration", "Total Duration"],
}

plot_config: Dict[str, bool] = {
    "responsive": True,
    "displayModeBar": False,
    "scrollZoom": False,
    "doubleClick": False,
    "staticPlot": False,
}

common_axes_properties: Dict[str, Any] = {
    "tickcolor": color_template["ticks"],
    # "showticklabels": True,
    "ticks": "",
    "tickfont": dict(color=color_template["lines"]),
    "title_font": dict(color=color_template["lines"]),
}


common_layout_properties: Dict[str, Any] = {
    "plot_bgcolor": color_template["background"],
    "paper_bgcolor": color_template["background"],
    "dragmode": False,
    "hovermode": "x",
    # "margin": dict(l=5, r=5, b=5, t=35, pad=10),  # Adjust these values as needed
}
