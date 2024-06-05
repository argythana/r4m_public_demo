import sys
import unittest

import pandas as pd
import polars as pl

# run from tests directory
sys.path.append("../src/utils")

# run from r4m_public directory
sys.path.append("./src/utils")

from time_file_to_df import (
    pandas_read_csv_file,
    pandas_read_csv_file_use_pyarrow,
    pandas_read_feather_file,
    polars_read_csv_file,
    polars_read_feather_file,
)


class TestTimeFileToDf(unittest.TestCase):
    def test_pandas_read_csv_file(self) -> None:
        df = pandas_read_csv_file()
        self.assertIsInstance(df, pd.DataFrame)
        return None

    def test_pandas_read_feather_file(self) -> None:
        df = pandas_read_feather_file()
        self.assertIsInstance(df, pd.DataFrame)
        return None

    def test_pandas_read_csv_file_use_pyarrow(self) -> None:
        df = pandas_read_csv_file_use_pyarrow()
        self.assertIsInstance(df, pd.DataFrame)
        return None

    def test_polars_read_csv_file(self) -> None:
        df = polars_read_csv_file()
        self.assertIsInstance(df, pl.DataFrame)
        return None

    def test_polars_read_feather_file(self) -> None:
        df = polars_read_feather_file()
        self.assertIsInstance(df, pl.DataFrame)
        return None


if __name__ == "__main__":
    unittest.main()
