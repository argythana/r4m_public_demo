import sys

sys.path.append("./src/utils")
sys.path.append("../src")
sys.path.append("../src/utils")


import unittest
from unittest.mock import MagicMock, patch

from create_dbs_utils import copy_remote_app_db_on_local_pc


class TestCreateDBsUtil(unittest.TestCase):
    @patch("create_dbs_utils.connect_to_remote_db")
    @patch("create_dbs_utils.connect_to_localhost_db")
    def test_copy_remote_app_db_on_local_pc(
        self,
        mock_connect_to_localhost_db: MagicMock,
        mock_connect_to_remote_db: MagicMock,
    ) -> None:
        # Set up mock objects
        mock_remote_db = MagicMock()
        mock_local_db = MagicMock()
        mock_connect_to_remote_db.return_value = (MagicMock(), mock_remote_db)
        mock_connect_to_localhost_db.return_value = mock_local_db

        # Call the function with test data
        copy_remote_app_db_on_local_pc({}, {}, {}, [])

        # Assert that the function behaved as expected
        mock_connect_to_remote_db.assert_called_once()
        mock_connect_to_localhost_db.assert_called_once()

        return None
