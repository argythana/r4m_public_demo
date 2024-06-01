import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from utils import connection_utils


class TestSSHConnection(unittest.TestCase):
    @patch("utils.connection_utils.SSHTunnelForwarder")
    def test_ssh_to_remote_server(self, mock_ssh_tunnel):
        # Create a mock for SSHTunnelForwarder
        mock_ssh_tunnel_instance = MagicMock()
        mock_ssh_tunnel.return_value = mock_ssh_tunnel_instance

        # Call your function with the arguments
        credentials = {
            "test_fake_server": {"ip": "192.168.0.1", "port": 22, "username": "tester"},
            "ssh_pkey_location": "/path/to/fake/private/key",
        }
        ssh_connection_instance = connection_utils.ssh_to_remote_server(
            "test_fake_server", credentials
        )

        # Verify that SSHTunnelForwarder was called with the correct arguments
        mock_ssh_tunnel.assert_called_once_with(
            ssh_address_or_host=(
                credentials["test_fake_server"]["ip"],
                credentials["test_fake_server"]["port"],
            ),
            ssh_username=credentials["test_fake_server"]["username"],
            ssh_pkey=credentials["ssh_pkey_location"],
            remote_bind_address=("localhost", 27017),
        )

        # Verify that the result is the mock SSHTunnelForwarder
        self.assertEqual(ssh_connection_instance, mock_ssh_tunnel_instance)


if __name__ == "__main__":
    unittest.main()
