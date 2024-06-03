"""
Function to create MongoDB databases and collections.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

from bson import ObjectId
from connection_utils import connect_to_localhost_db, connect_to_remote_db
from pymongo.database import Database
from sshtunnel import SSHTunnelForwarder

# First Datetime log
INIT_CHECK_DATETIME = datetime(2022, 2, 10, 0, 0, 0, 0)


def copy_remote_app_db_on_local_pc(
    server_credentials: Dict[str, str],
    remote_db_credentials: Dict[str, str],
    local_db_credentials: Dict[str, str],
    collections_to_copy: List[str],
) -> None:
    """
    Connect to MongoDB on a remote server and copy the selected collections to a DB on local PC.
    You may copy the "app" DB collections to the "analytics" DB any other DB as long credentials are in config.json..
    Args:
        server_credentials: The server to connect to. Should be selected from the credentials.json file.
            Available options are: "app_server", "analytics_server".
        remote_db_credentials: Credentials data in dict format from the credentials.json file.
        local_db_credentials: Credentials data in dict format from the credentials.json file.
        collections_to_copy: A list of DB collection names, to copy from remote to local.
    Return: None
    """
    # DB to copy from.
    remote_connection_results: Tuple[SSHTunnelForwarder, Database[Any]] = (
        connect_to_remote_db(server_credentials, remote_db_credentials)
    )

    ssh_connection: SSHTunnelForwarder = remote_connection_results[0]
    from_remote_db: Database[Any] = remote_connection_results[1]

    # Local DB to copy to.
    db_target: Database[Any] = connect_to_localhost_db(
        machine="local_pc", db_credentials=local_db_credentials
    )

    # Copy listed collections from the VM database to a local database.
    for db_collection in collections_to_copy:
        # Fetch all documents from the remote database.
        remote_documents: List[Dict[str, Any]] = list(
            from_remote_db[db_collection].find()
        )

        # For each document in the remote database:
        for remote_doc in remote_documents:
            # Check if the document is in the local database.
            local_doc: Optional[Dict[str, Any]] = db_target[db_collection].find_one(
                {"_id": ObjectId(remote_doc["_id"])}
            )

            # If document is not in the local database, insert it.
            if local_doc is None:
                db_target[db_collection].insert_one(remote_doc)
            # If document is in the local database, compare it with the remote document.
            else:
                # If they are not the same, update the local document with the remote document.
                if local_doc != remote_doc:
                    db_target[db_collection].replace_one(
                        {"_id": ObjectId(remote_doc["_id"])}, remote_doc
                    )

    # Close the connections.
    from_remote_db.client.close()
    db_target.client.close()
    ssh_connection.stop()
    return None
