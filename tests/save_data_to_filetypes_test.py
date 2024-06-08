"""
Tests for functions in save_data_to_filetypes.py
"""

import os
import sys
from unittest.mock import mock_open, patch

# run from tests directory
sys.path.append("../src/data")
# to run from r4m_public directory add
sys.path.append("./src/data")

# import functions to test
from save_data_to_filetypes import is_feather_v1_or_v2

# Get the absolute path of the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the paths to the data files
csv_file_path = os.path.join(dir_path, "../src", "data", "acts_dy_date.csv")
feather_file_path = os.path.join(dir_path, "../src", "data", "acts_by_date.feather")


def test_is_feather_v1_or_v2() -> None:
    """
    Test the is_feather_v1_or_v2 function.
    """
    # Call function with test data
    feather_version_2 = is_feather_v1_or_v2(feather_file_path)

    # Assert the function returned expected value
    assert feather_version_2 == "V2"

    # Construct path to mock Feather v1 file
    feather_v1_file_path = os.path.join(dir_path, "../src/data/mock_feather_v1.feather")
    # Create mock Feather v1 file
    with open(feather_v1_file_path, "wb") as fh:
        # Write the magic bytes for Feather v1 at beginning and end of file
        fh.write(b"FEA1" + b"\0" * 92 + b"FEA1")

    # Assert function returns v1
    feather_version_1 = is_feather_v1_or_v2(feather_v1_file_path)
    assert feather_version_1 == "V1"

    # Delete the mock Feather v1 file
    os.remove(feather_v1_file_path)

    # Create mock file that is neither a Feather v1 nor Feather v2
    mock_file = mock_open(
        read_data=b"Mock file that is neither a Feather v1 nor Feather v2."
    )
    # Test is_feather_v1_or_v2 function with mock file
    with patch("builtins.open", mock_file):
        feather_version = is_feather_v1_or_v2("mock_file_path")
    # Assert that the function returned None
    assert feather_version is None

    return None
