"""
PLot the data from a dataframe.
Run from the src directory.
"""

import os

from pandas import DataFrame

from utils.create_plots import create_date_plots, load_data_to_cache

# Get the absolute path of the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the paths to the data files
feather_file_path = os.path.join(dir_path, ".", "data", "acts_by_date.feather")


if __name__ == "__main__":
    # Use cache function for static data
    df: DataFrame = load_data_to_cache(feather_file_path)

    # Plot the data
    # create_date_plots(df, chart_y="acts")
    # create_date_plots(df, chart_y="distance")
    create_date_plots(df, chart_y="users")
    create_date_plots(df, chart_y="duration")
