"""
This script initializes the analytics database by cloning the collections from the AppDB.
"""

import json
from connection_utils import init_analytics_db

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
        # AppDB collections to clone locally.
        db_collections_list = ["users", "activities", "participations"]

    # Todo: Document that credentials should be in config.json file.
    init_analytics_db(
        host_server,
        schema,
        credentials,
        machine,
        db_collections=db_collections_list,
        target_db_name="app",  # Todo: Remove clone db from init analytics.
    )
