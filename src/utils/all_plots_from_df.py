"""
This module contains functions to create charts from a dataframe.
"""

from __future__ import annotations

import datetime
import random
from typing import Optional, Union

import pandas as pd
import plotly.graph_objects as go  # type: ignore
import streamlit as st
from pandas import DataFrame

from .dashboard_plot_configs import (
    chart_config,
    chart_labels,
    common_axes_properties,
    common_layout_properties,
)
from .demo_site_colors import color_template


@st.cache_data
def load_data_to_cache(file_path: str) -> pd.DataFrame:
    cache_df: DataFrame = pd.read_feather(file_path)
    # Set date column as index
    cache_df.set_index("date", inplace=True, drop=True)
    # get rid of column  Unnamed: 0
    cache_df = cache_df[cache_df.columns.difference(["Unnamed: 0"])]
    return cache_df


def create_daily_aggregations_charts(
    chart_name: Union[str, None], df: pd.DataFrame
) -> None:
    """
    Create a table with totals columns, by user:
    user, total distance, total duration, total activities.
    Args:
        chart_name: The name of the chart to create. A key from the chart_labels dictionary.
        df: the pandas DataFrame.
    Returns:
        None
    """
    # Get chart title, y-axis title from the dictionary
    df_column_name: Optional[str] = None  # Assign default value
    chart_title: Optional[str] = None  # Assign a default value
    y_axis_title: Optional[str] = None  # Assign a default value

    if chart_name is not None:
        (chart_title, y_axis_title) = (
            chart_labels[chart_name][1],
            chart_labels[chart_name][1],
        )
        df_column_name = chart_labels[chart_name][0]
    if df_column_name is None:
        raise ValueError(
            "chart_name cannot be None. Please Fix the chart labels dictionary."
        )

    # Create a plotly chart
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df[df_column_name],
            name=chart_name,
            mode="markers+lines",
            line=dict(
                color=color_template["lines"],
                width=0.75,
            ),
            marker=dict(color=color_template["lines"], size=0.5),
        )
    )
    fig.update_layout(
        title=chart_title,  # Design choice, it is  in the sidebar.
        yaxis_title=f"{y_axis_title}",
        xaxis=dict(
            nticks=10,  # len(df.index),
            tickformat="%d-%m",
            **common_axes_properties,
        ),
        yaxis=dict(
            range=[
                str(0 - 0.25),
                str(df[df_column_name].max() + 0.05 * df[df_column_name].max()),
            ],
            **common_axes_properties,
        ),
        **common_layout_properties,
    )

    # Display chart in Streamlit app
    st.plotly_chart(
        fig,
        use_container_width=True,
        config=chart_config,
    )

    return None


def create_progress_bar_from_df(df: pd.DataFrame) -> None:
    """
    Create a progress bar chart for the challenge.
    Calculate the percentage of the challenge completed. Goal is 5000 km.
    Arg:
        df: A pandas DataFrame.
    Returns:
        None
    """
    # Challenge goal distance
    goal_distance: Union[int, float] = 100000000

    # Challegne goal column should be calculated first.
    # Either here or in the main script.
    # df["total_distance"] = df["distance"].cumsum()
    # current_distance from last row of DataFrame column "total_distance.
    current_distance: Union[int, float] = df["total_distance"].iloc[-1]

    percentage_completed = (current_distance / goal_distance) * 100
    # percentage_remaining = 100 - percentage_completed

    # Create plotly chart
    fig = go.Figure()
    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=percentage_completed,
            number={
                "suffix": "%",
                "font": {"size": 64, "color": color_template["lines"]},
            },
            # title={"text": "Challenge Progress"},
            domain={"x": [0, 1], "y": [0, 1]},
            gauge={
                "axis": {
                    "range": [None, 100],
                    "tickwidth": 1,
                    "tickcolor": color_template["ticks"],
                    "showticklabels": True,
                    "ticks": "",
                    "tickfont": dict(color=color_template["ticks"]),
                },
                "bar": {
                    "color": color_template["demo"],
                    "thickness": 1,
                },
                # "bar": {"color": color_template["lines"]},
                "bgcolor": color_template["background"],
                "steps": [{"range": [0, 100], "color": "#bfbfbf"}],
            },
        ),
    )

    fig.update_layout(
        # title={"text": "Challenge Progress"},  # Design choice, since it is  in the sidebar.
        plot_bgcolor=color_template["background"],
        paper_bgcolor=color_template["background"],
        dragmode=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config=chart_config,
    )

    return None


@st.cache_data
def fake_leaderboard() -> None:
    """
    Create a fake dataframe with 20 rows and 5columns:
    Rank, username, Kms, € raised, Lottery tickets.
    Username is a list of 20 random names
    Kms is a list of 20 random floats between 1000 and 5000
    Rank is kms rank in ascending order
    € raised is a list of 20 random floats between 2300 and 11500
    Lottery tickets is an integer division of Kms by 10
    Display the dataframe in a table.
    """
    # Create a fake dataframe with 20 rows and 5 columns
    fake_df: DataFrame = pd.DataFrame(
        {
            "Username": [
                "Username " + str(i) for i in range(1, 21)
            ],  # A list of 20 random names
            "Kms": [
                random.uniform(1000, 5000) for _ in range(20)
            ],  # A list of 20 random floats between 1000 and 5000
            "€ raised": [
                random.uniform(2300, 11500) for _ in range(20)
            ],  # A list of 20 random floats between 2300 and 11500
        }
    )

    # Lottery tickets is an integer division of Kms by 10
    fake_df["Lottery tickets"] = fake_df["Kms"] // 10
    fake_df["Rank"] = fake_df["Kms"].rank(ascending=False).astype(int)

    # Sort DataFrame by 'Rank'
    fake_df.sort_values(by="Rank", inplace=True)

    # Set Rank as index
    fake_df.set_index("Rank", inplace=True)

    # Display  dataframe in a table
    st.write(fake_df)

    return None


def create_all_charts_from_feather_file(filename: str) -> None:
    """
    Create all charts for the dashboard.
    Args:
        filename: A string with the path to the feather file.
    Returns:
        None
    """

    df: DataFrame = load_data_to_cache(filename)

    # Calculate cumulative totals for all dates
    # TODO refactor this to a function and get also bike, walk-run totals for everything.
    df["total_distance"] = df["distance"].cumsum()
    df["total_duration"] = df["duration"].cumsum()
    df["total_activities"] = df["acts"].cumsum()

    # Create a select box in the sidebar from the dictionary keys
    chart_option = st.selectbox(
        "Please select a visualization from the menu:", chart_labels.keys(), index=0
    )

    # Don't use date selection slider for leaderboard and challenge progress.
    if chart_option == "Top 20 Leaderboard":
        fake_leaderboard()
    elif chart_option == "Distance Challenge Progress":
        create_progress_bar_from_df(df)
    elif chart_option == "Daily Activities Data Sample":
        # Display all columns and 10 rows of the obfuscated DataFrame
        st.write(df[:10])

    # TODO: Copy this chart from Production code.
    # elif chart_option == "Progress Donut":
    #     create_progress_donut_chart(db_collection)

    else:
        # Convert index to datetime.date type
        df.index = pd.Index(pd.to_datetime(df.index).date)

        # Create a date slider
        min_date: datetime.date = df.index.min()
        max_date: datetime.date = df.index.max()

        # Skip date slider if there is only one date, create charts without slider
        if min_date == max_date:
            create_daily_aggregations_charts(chart_name=chart_option, df=df)
        else:
            # Create a date slider
            selected_dates = st.slider(
                label="Set a date range",
                min_value=min_date,
                max_value=max_date,
                value=(min_date, max_date),
                step=None,
                format=None,
                key="date_range_slider",
            )
            # Filter DataFrame based on the selected date range
            df = df[(df.index >= selected_dates[0]) & (df.index <= selected_dates[1])]

            # Create the streamlit charts based on the selected option
            create_daily_aggregations_charts(chart_name=chart_option, df=df)

            # TODO: Create weekly and monthly aggregations charts
            # create_weekly_aggregations_charts(chart_name=chart_option, df=df)

    return None
