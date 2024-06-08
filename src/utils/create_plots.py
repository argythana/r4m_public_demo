import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from demo_streamlit_colors import color_template
from plot_constants_configs import (
    PLOTS_LABELS,
    common_axes_properties,
    common_layout_properties,
    plot_config,
)


def create_date_plots(df: pd.DataFrame, *, chart_y: str) -> None:
    # TODO: add parameter groupby: str
    """
    Plot the data in the DataFrame by date.
    Args:
        df: pd.DataFrame: The DataFrame to plot.
        chart_y: str: The activity column to plot on the y-axis.
            Options: are "users", "acts", "distance", "duration" and their combinations with walk_run and bike.
        TODO: groupby: str: The date aggregation to group the data by.
            Options: are "day", "week", "month", "quarter", "year".
    Returns:
        None
    """
    # Get chart title, y-axis title from the dictionary
    chart_title, y_axis_title = PLOTS_LABELS[chart_y]
    df_column_name = f"{chart_y.lower()}"
    # Create a plotly chart
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df[df_column_name],
            name=chart_y,
            mode="markers+lines",
            line=dict(color=color_template["lines"]),
            marker=dict(color=color_template["lines"], size=2),
        )
    )
    fig.update_layout(
        title=chart_title,
        # yaxis_title=f"{chart_name}",
        xaxis=dict(
            nticks=8,  # len(df.index),
            tickformat="%d-%m",
            **common_axes_properties,
        ),
        yaxis=dict(
            range=[
                0 - 0.25,
                df[df_column_name].max() + 0.05 * df[df_column_name].max(),
            ],
            **common_axes_properties,
        ),
        **common_layout_properties,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config=plot_config,
    )

    return None
