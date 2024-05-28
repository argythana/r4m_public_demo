"""
Copy a remote database to the local workstation.
Run on local PC to get a copy of selected collections from a remote DB.
"""

import json

from .connection_utils import copy_remote_app_db_on_local_pc

if __name__ == "__main__":
    # Run from utils/
    with open("../config/credentials.json") as credentials_file:
        credentials = json.load(credentials_file)
        host_server = "app_server"  # IP and Port are in the credentials file.
        schema = credentials["schema"]
        machine = credentials["machine"]

        # Remote DB collections to copy.
        copy_collections = [
            "users",
            "participations",
            # "activities",
            # "addresses",
        ]

        copy_remote_app_db_on_local_pc(
            host_server,
            schema,
            credentials,
            machine,
            copy_collections,
            source_db="app",
            target_db="app",  # Copy with same schema name as remote DB.
        )
