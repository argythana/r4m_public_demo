"""
Initialise a new database and add an initial datetime log.
"""

import json

from connection_utils import init_new_db  # type: ignore

if __name__ == "__main__":
    # Run from utils/
    with open("../config/credentials.json") as credentials_file:
        credentials = json.load(credentials_file)

        schema = credentials["schema"]
        machine = credentials["machine"]

    # DB credentials should be in config.json file.
    try:
        init_new_db(
            schema,
            credentials,
            machine,
            new_db_name="test",
        )
    except KeyError as e:
        print(
            f"DB credentials should be in config.json. This DB name does not have valid credentials.\nKeyError: {e}"
        )
