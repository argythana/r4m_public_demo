"""
Connect to a remote host database on a VM.
Use from local PC for dev and testing..
"""

from __future__ import annotations

import json
from typing import Any, Dict, Tuple

from connection_utils import connect_to_remote_db
from pymongo.database import Database
from sshtunnel import SSHTunnelForwarder

if __name__ == "__main__":
    # Get credentials from local file.
    with open("../config/credentials.json") as credentials_file:
        all_credentials_dict: Dict[str, Any] = json.load(credentials_file)

        # Chose server credentials.
        server_credentials: Dict[str, str] = all_credentials_dict[
            "app_server_credentials"  # App server.
        ]

        machine: str = "vm"
        scope: str = "Prod_"  # ProductionDB version.
        # DB to connect to.
        db_credentials_suffix: str = "appDb_Credentials"  # App DB.

        # DB credentials from local credentials file.
        db_credentials: Dict[str, str] = all_credentials_dict[
            scope + db_credentials_suffix
        ]

    connection_results: Tuple[SSHTunnelForwarder, Database[Any]] = connect_to_remote_db(
        server_credentials, db_credentials
    )
    ssh_connection: SSHTunnelForwarder = connection_results[0]
    appProdDB: Database[Any] = connection_results[1]

    appProdDB.client.close()
    ssh_connection.stop()
