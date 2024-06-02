import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.append("./src/utils")
sys.path.append("../src/utils")
sys.path.append("../utils")

from connection_utils import (
    connect_to_localhost_db,
    connect_to_remote_db,
    ssh_to_remote_server,
)


class TestConnectionUtils(unittest.TestCase):
    @patch("connection_utils.SSHTunnelForwarder")
    def test_ssh_to_remote_server(self, mock_SSHTunnelForwarder: MagicMock) -> None:
        # Setup
        server_credentials = {
            "ip": "127.0.0.1",
            "port": 22,
            "username": "test",
            "ssh_pkey_location": "/path/to/key",
        }

        # Call the function
        ssh_to_remote_server(server_credentials)

        # Assert
        mock_SSHTunnelForwarder.assert_called_once_with(
            ssh_address_or_host=(server_credentials["ip"], server_credentials["port"]),
            ssh_username=server_credentials["username"],
            ssh_pkey=server_credentials["ssh_pkey_location"],
            remote_bind_address=("localhost", 27017),
        )
        return None

    @patch("connection_utils.pymongo.MongoClient")
    def test_connect_to_localhost_db(self, mock_MongoClient: MagicMock) -> None:
        # Setup
        machine = "local_pc"
        db_credentials = {
            "mongodbUser": "test",
            "mongodbPassword": "test",
            "mongodbDatabase": "test_db",
        }

        # Call the function
        connect_to_localhost_db(machine, db_credentials)

        # Assert
        mock_MongoClient.assert_called_once_with(
            host="localhost",
            port=27017,
            authSource=db_credentials["mongodbDatabase"],
            username="",
            password="",
        )
        return None

    @patch("connection_utils.pymongo.MongoClient")
    @patch("connection_utils.ssh_to_remote_server")
    def test_connect_to_remote_db(
        self, mock_ssh_to_remote_server: MagicMock, mock_MongoClient: MagicMock
    ) -> None:
        # Setup
        server_credentials = {
            "ip": "127.0.0.1",
            "port": 22,
            "username": "test",
            "ssh_pkey_location": "/path/to/key",
        }
        database_credentials = {
            "mongodbUser": "test",
            "mongodbPassword": "test",
            "mongodbDatabase": "test_db",
        }

        # Mock
        mock_ssh_to_remote_server.return_value = MagicMock(local_bind_port=27017)

        # Call the function
        connect_to_remote_db(server_credentials, database_credentials)

        # Assert
        mock_MongoClient.assert_called_once_with(
            host="localhost",
            port=27017,
            username=database_credentials["mongodbUser"],
            password=database_credentials["mongodbPassword"],
            authSource=database_credentials["mongodbDatabase"],
        )
        return None


if __name__ == "__main__":
    # ignore in pytest coverage
    unittest.main()  # pragma: no cover
