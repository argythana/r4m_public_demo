import os
from typing import Optional

import pandas as pd

# Get the absolute path of the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the paths to the data files
csv_file_path = os.path.join(dir_path, "..", "data", "acts_dy_date.csv")
feather_file_path = os.path.join(dir_path, "..", "data", "acts_by_date.feather")


def csv_to_feather(csv_file_path: str, feather_file_path: str) -> None:
    """
    Read a csv file and save it as a Feather file.

    :param csv_file_path: The path to the csv file.
    :param feather_file_path: The path to save the Feather file.
    :return: None
    """
    # Read csv file
    df = pd.read_csv(csv_file_path)

    # Save DataFrame as Feather file. Identical to .ipc files.
    df.to_feather(feather_file_path)  # Default version is 2

    return None


# get feather file type, Refactored function from:
# https://github.com/aertslab/create_cisTarget_databases/blob/master/feather_v1_or_v2.py


def is_feather_v1_or_v2(feather_file: str) -> Optional[str]:
    """
    Check if the passed filename is a Feather v1 or v2 file.

    :param feather_file: Feather v1 or v2 filename.
    :return: "V1" or "V2" if the file is a Feather v1 or v2 file, respectively.

    """

    with open(feather_file, "rb") as fh_feather:
        # Read first 6 and last 6 bytes to see if we have a Feather v2 file.
        fh_feather.seek(0, 0)
        feather_v2_magic_bytes_header = fh_feather.read(6)
        fh_feather.seek(-6, 2)
        feather_v2_magic_bytes_footer = fh_feather.read(6)
        if feather_v2_magic_bytes_header == feather_v2_magic_bytes_footer == b"ARROW1":
            return "V2"

        # Read first 4 and last 4 bytes to see if we have a Feather v1 file.
        feather_v1_magic_bytes_header = feather_v2_magic_bytes_header[0:4]
        feather_v1_magic_bytes_footer = feather_v2_magic_bytes_footer[2:]
        if feather_v1_magic_bytes_header == feather_v1_magic_bytes_footer == b"FEA1":
            return "V1"

    return None


if __name__ == "__main__":
    # Convert the csv file to a Feather file
    csv_to_feather(csv_file_path, feather_file_path)

    # Check if the Feather file is a v1 or v2 file
    print(is_feather_v1_or_v2(feather_file_path))
# is_feather_v1_or_v2("acts_by_date.feather")
