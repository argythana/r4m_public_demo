"""
Connect to a local host database.
"""

from __future__ import annotations

import json
from typing import Any, Dict

from connection_utils import connect_to_localhost_db
from pymongo.database import Database

if __name__ == "__main__":
    # Run from utils/
    with open("../config/credentials.json") as credentials_file:
        all_credentials_dict: Dict[str, Any] = json.load(credentials_file)

        # Machine is hardcoded in the credentials file.
        machine: str = all_credentials_dict["machine"]

        # Choose the following two values to select DB to connect.
        scope: str = "Prod_"  # Production DB version.
        db_credentials_suffix: str = "appDb_Credentials"  # App DB.
        db_credentials_name: str = scope + db_credentials_suffix
        db_credentials: Dict[str, str] = all_credentials_dict[db_credentials_name]

    appProdDB: Database[Any] = connect_to_localhost_db(machine, db_credentials)
    print(appProdDB.list_collection_names())
    appProdDB.client.close()
