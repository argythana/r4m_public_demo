"""
Copy selected collections from a remote database to a local workstation.
For Dev and Testing.
TODO: Refactor to check if collection exists. If exits, update, going 1 month back.
"""

import json
from typing import Any, Dict, List

from create_dbs_utils import copy_remote_app_db_on_local_pc

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
        remote_db_credentials_suffix: str = "appDb_Credentials"  # App DB.

        # Get remote DB credentials from local file.
        remote_db_credentials: Dict[str, str] = all_credentials_dict[
            scope + remote_db_credentials_suffix
        ]

        # Ser local DB credentials from local credentials file.
        local_db_credentials: Dict[str, str] = {
            "mongodbUser": "",
            "mongodbPassword": "",
            "mongodbDatabase": "run4moreProd",  # Name of the local DB.
        }

        # Select collections to copy from remote to local.
        collections_to_copy: List[str] = [
            "users",
            "activities",
        ]

        # Copy remote DB collections to local.
        copy_remote_app_db_on_local_pc(
            server_credentials,
            remote_db_credentials,
            local_db_credentials,
            collections_to_copy,
        )
