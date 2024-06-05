"""
Tests for functions in save_data_to_filetypes.py
"""

import os
import sys
from unittest.mock import mock_open, patch

import pandas as pd

# run from tests directory
sys.path.append("../src/data")

# to run from r4m_public directory add
sys.path.append("./src/data")


# import functions to test
from save_data_to_filetypes import csv_to_feather, is_feather_v1_or_v2

# Get the absolute path of the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Add the 'src' directory to the system path to run test from the 'tests' directory
sys.path.append(os.path.join(dir_path, "src"))

# Construct the paths to the data files
csv_file_path = os.path.join(dir_path, "../src", "data", "obfuscated_data.csv")
feather_file_path = os.path.join(dir_path, "../src", "data", "obfuscated_data.feather")


# Define test functions
def test_csv_to_feather() -> None:
    """
    Test the csv_to_feather function.
    """
    # Call the function with test data
    csv_to_feather(csv_file_path, feather_file_path)

    # Read the feather file
    df = pd.read_feather(feather_file_path)

    # Assert that the feather file was created
    assert isinstance(df, pd.DataFrame)

    return None


def test_is_feather_v1_or_v2() -> None:
    """
    Test the is_feather_v1_or_v2 function.
    """
    # Call the function with test data
    feather_version_2 = is_feather_v1_or_v2(feather_file_path)

    # Assert that the function returned the expected result
    assert feather_version_2 == "V2"

    # Construct path to a mock Feather v1 file
    feather_v1_file_path = os.path.join(dir_path, "../src/data/mock_feather_v1.feather")
    # Create mock Feather v1 file
    with open(feather_v1_file_path, "wb") as fh:
        # Write the magic bytes for Feather v1 at the beginning and end of the file
        fh.write(b"FEA1" + b"\0" * 92 + b"FEA1")

    # Call the function with the mock Feather v1 file
    feather_version_1 = is_feather_v1_or_v2(feather_v1_file_path)
    assert feather_version_1 == "V1"

    # Delete the mock Feather v1 file
    os.remove(feather_v1_file_path)

    # Create a mock file that is neither a Feather v1 nor a Feather v2 file
    mock_file = mock_open(
        read_data=b"This is a mock file that is neither a Feather v1 nor a Feather v2 file."
    )
    # Use the mock file in the context of the is_feather_v1_or_v2 function
    with patch("builtins.open", mock_file):
        feather_version = is_feather_v1_or_v2("mock_file_path")
    # Assert that the function returned None
    assert feather_version is None

    return None
