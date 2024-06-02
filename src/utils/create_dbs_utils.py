"""
Function to create MongoDB databases and collections.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Tuple

from connection_utils import connect_to_localhost_db, connect_to_remote_db
from pymongo.database import Database
from sshtunnel import SSHTunnelForwarder

# First Datetime log
INIT_CHECK_DATETIME = datetime(2022, 2, 10, 0, 0, 0, 0)


def copy_remote_app_db_on_local_pc(
    server_credentials: Dict[str, str],
    remote_db_credentials: Dict[str, str],
    local_db_credentials: Dict[str, str],
    copy_collections: List[str],
) -> None:
    """
    Connect to MongoDB on a remote server and copy the selected collections to a DB on local PC.
    You may copy the "app" DB collections to the "analytics" DB any other DB as long credentials are in config.json..
    Args:
        server_credentials: The server to connect to. Should be selected from the credentials.json file.
            Available options are: "app_server", "analytics_server".
        remote_db_credentials: Credentials data in dict format from to the credentials.json file.
        local_db_credentials: Credentials data in dict format from to the credentials.json file.
        copy_collections: A list of DB collection names, to copy from remote to local.
    Return: None
    """
    # DB to copy from.
    remote_connection_results: Tuple[SSHTunnelForwarder, Database[Any]] = (
        connect_to_remote_db(server_credentials, remote_db_credentials)
    )

    from_remote_db: Database[Any] = remote_connection_results[1]
    ssh_connection: SSHTunnelForwarder = remote_connection_results[0]

    # DB to copy to. Gets the same scope as the remote DB.
    db_target = connect_to_localhost_db(
        machine="local_pc", db_credentials=local_db_credentials
    )

    # Copy listed collections from the VM database to a local database.
    # TODO: Refactor to update if collection exists. Code breaks if collection exists
    for db_collection in copy_collections:
        db_collection_documents = list(from_remote_db[db_collection].find())
        # Create the collections on the local PC database.
        db_target[db_collection].insert_many(db_collection_documents)

    # Close the connections.
    from_remote_db.client.close()
    db_target.client.close()
    ssh_connection.stop()
    return None
