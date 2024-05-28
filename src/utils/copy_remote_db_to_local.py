"""
This script is used to clone the remote database to the local workstation.
"""

import json
from connection_utils import copy_remote_app_db_on_local_pc

import os

# Get the absolute path of the directory where the credentials.json file is located
config_dir = os.path.abspath("../config/")

if __name__ == "__main__":
    # Run from utils/
    with open("../config/credentials.json") as credentials_file:
        credentials = json.load(credentials_file)
        host_server = "app_server"
        schema = credentials["schema"]
        machine = credentials["machine"]
        # AppDB collections to copy.
        copy_collections = ["users", "activities", "participations"]

    copy_remote_app_db_on_local_pc(
        host_server,
        schema,
        credentials,
        machine,
        copy_collections,
        copy_db_name="app",
    )
