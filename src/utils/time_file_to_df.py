"""
Compare the time to read data using different file formats and libraries.
"""

import os
import timeit

import pandas as pd
import polars as pl

# Get the absolute path of the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the paths to the data files
csv_file_path = os.path.join(dir_path, "..", "data", "acts_dy_date.csv")
feather_file_path = os.path.join(dir_path, "..", "data", "acts_by_date.feather")


def pandas_read_csv_file() -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv(csv_file_path)
    return df


def pandas_read_csv_file_use_pyarrow() -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv(csv_file_path, engine="pyarrow")
    return df


def pandas_read_feather_file() -> pd.DataFrame:
    df: pd.DataFrame = pd.read_feather(feather_file_path)
    return df


def polars_read_csv_file() -> pl.DataFrame:
    df: pl.DataFrame = pl.read_csv(csv_file_path)
    return df


def polars_read_feather_file() -> pl.DataFrame:
    df: pl.DataFrame = pl.read_ipc(feather_file_path, memory_map=False)
    return df


# Number of times to run the function to get the average time
NUMBER = 500

# Time pandas read csv
pandas_read_csv_time = timeit.timeit(pandas_read_csv_file, number=NUMBER)

# Time pandas read csv using pyarrow
pandas_read_csv_use_pyarrow_time = timeit.timeit(
    pandas_read_csv_file_use_pyarrow, number=NUMBER
)

# Time pandas read csv feather
pandas_read_feather_time = timeit.timeit(pandas_read_feather_file, number=NUMBER)


# Time polars read csv
polars_read_csv_time = timeit.timeit(polars_read_csv_file, number=NUMBER)

# Time polars read feather
polars_read_feather_time = timeit.timeit(polars_read_feather_file, number=NUMBER)

print(
    f"Time for pandas to read the csv file {NUMBER} times: {pandas_read_csv_time} seconds.\n"
    f"Time for pandas to read the csv file using pyarrow {NUMBER} times: {pandas_read_csv_use_pyarrow_time} seconds.\n"
    f"Time for pandas to read the feather file {NUMBER} times: {pandas_read_feather_time} seconds.\n"
    f"Time for polars to read the csv file {NUMBER} times: {polars_read_csv_time} seconds.\n"
    f"Time for polars to read the feather version 2 file {NUMBER} times: {polars_read_feather_time} seconds.\n"
)
