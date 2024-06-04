"""
Compare the time it takes to read data using different file formats and libraries.
"""

import os
import timeit

import pandas as pd

# Get the absolute path of the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the paths to the data files
csv_file_path = os.path.join(dir_path, "..", "data", "obfuscated_data.csv")
feather_file_path = os.path.join(dir_path, "..", "data", "obfuscated_data.feather")


def read_csv_file() -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv(csv_file_path)
    return df


def read_feather_file() -> pd.DataFrame:
    df: pd.DataFrame = pd.read_feather(feather_file_path)
    return df


# Time using pandas from csv file
time_taken_csv = timeit.timeit(read_csv_file, number=1000)


# Time using pandas from feather file
time_taken_feather = timeit.timeit(read_feather_file, number=1000)


print(
    f"Time for pandas to read the csv file 1000 times: {time_taken_csv} seconds.\n"
    f"Time for pandas to read the feather file 1000 times: {time_taken_feather} seconds.",
)
