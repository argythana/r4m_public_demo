"""
Copy a remote database to the local workstation.
Run on local PC to get a copy of selected collections from a remote DB.
TODO: Refactor to check if collection exists. If exits, update, going 1 month back.
"""

import json
from typing import Any, Dict, List

from create_dbs_utils import copy_remote_app_db_on_local_pc

if __name__ == "__main__":
    # Run from utils/
    # Connect to the remote VM using SSH.
    with open("../config/credentials.json") as credentials_file:
        all_credentials_dict: Dict[str, Any] = json.load(credentials_file)

        # Chose server credentials. # App server.
        server_credentials: Dict[str, str] = all_credentials_dict[
            "app_server_credentials"
        ]

        machine: str = "vm"
        scope: str = "Prod_"  # ProductionDB version.
        remote_db_credentials_suffix: str = "appDb_Credentials"  # App DB.

        # DB credentials from local credentials file.
        remote_db_credentials: Dict[str, str] = all_credentials_dict[
            scope + remote_db_credentials_suffix
        ]

        print(remote_db_credentials)

        # Local DB credentials from local credentials file.
        local_db_credentials: Dict[str, str] = {
            "mongodbUser": "",
            "mongodbPassword": "",
            "mongodbDatabase": "run4moreProd",
        }

        # Copy collections from remote to local.
        copy_collections: List[str] = [
            "users",
        ]

        # Copy remote DB to local.
        copy_remote_app_db_on_local_pc(
            server_credentials,
            remote_db_credentials,
            local_db_credentials,
            copy_collections,
        )
