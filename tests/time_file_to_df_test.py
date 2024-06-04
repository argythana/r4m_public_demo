import sys
import unittest

import pandas as pd

# src to path

sys.path.append("../src")
sys.path.append("../src/utils")

from time_file_to_df import read_csv_file, read_feather_file


class TestTimeFileToDf(unittest.TestCase):
    def test_read_csv_file(self) -> None:
        df = read_csv_file()
        self.assertIsInstance(df, pd.DataFrame)
        return None

    def test_read_feather_file(self) -> None:
        df = read_feather_file()
        self.assertIsInstance(df, pd.DataFrame)
        return None


if __name__ == "__main__":
    unittest.main()
