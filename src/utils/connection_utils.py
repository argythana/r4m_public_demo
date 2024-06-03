"""
Functions to connect to MongoDB Databases on local or remote servers.
Use the template_credentials.json file to insert your own credentials.json file.
Have the credentials.json file in the config folder.
"""

from __future__ import annotations

from typing import Any, Dict, Tuple

import pymongo
from pymongo.database import Database
from sshtunnel import SSHTunnelForwarder


def ssh_to_remote_server(server_credentials: Dict[Any, Any]) -> SSHTunnelForwarder:
    """
    SSH into a remote server.
    Args:
        server_credentials: Data in dict format from to a json file.
        ip, port, username should be in credentials.json.
    Return:
        ssh_connection: an SSHTunnelForwarder.
    """

    # SSH Tunnel to the remote VM
    ssh_connection: SSHTunnelForwarder = SSHTunnelForwarder(
        ssh_address_or_host=(
            server_credentials["ip"],
            server_credentials["port"],
        ),
        ssh_username=server_credentials["username"],
        ssh_pkey=server_credentials["ssh_pkey_location"],
        remote_bind_address=("localhost", 27017),
    )
    return ssh_connection


def connect_to_localhost_db(
    machine: str, db_credentials: Dict[str, str]
) -> Database[Any]:
    """
    Connect to the local MongoDB database on the localhost.
    Args:
        machine: The machine to connect to. Options are "local_pc", or "vm".
        db_credentials: A dictionary with the following credential keys and values of a DB:
            "mongodbUser", "mongodbPassword", "mongodbDatabase", according to the config.json file.
            Combine the scope and credentials suffix to get the DB credentials.
    Return:
        local_db: A database object with access to all collections.
    """
    # Connect to the MongoDB database
    db_client: pymongo.MongoClient[Any] = pymongo.MongoClient(
        host="localhost",
        port=27017,
        authSource=db_credentials["mongodbDatabase"],
        # No password on local PC.
        username=(db_credentials["mongodbUser"] if machine == "vm" else ""),
        password=(db_credentials["mongodbPassword"] if machine == "vm" else ""),
    )

    db_name: str = db_credentials["mongodbDatabase"]

    local_db: Database[Any] = db_client[db_name]
    return local_db


def connect_to_remote_db(
    server_credentials: Dict[str, str], database_credentials: Dict[str, str]
) -> Tuple[SSHTunnelForwarder, Database[Any]]:
    """
    Connect to the MongoDB database on a remote sever.
    Args:
        Select from the credentials.json
        server_credentials: The server to connect to.
        database_credentials: The database credentials.
    Return:
        remote_db: A database object with access to all collections.
        ssh_connection: An SSHTunnelForwarder object.
    """

    # Connect to the remote via SSH
    ssh_connection: SSHTunnelForwarder = ssh_to_remote_server(server_credentials)
    ssh_connection.start()

    # DB to connect to. Is the name from the config.json file.
    db_name = database_credentials["mongodbDatabase"]

    # Connect to the MongoDB database
    db_client: pymongo.MongoClient[Any] = pymongo.MongoClient(
        host="localhost",
        port=ssh_connection.local_bind_port,
        username=database_credentials["mongodbUser"],
        password=database_credentials["mongodbPassword"],
        authSource=db_name,
    )
    remote_db: Database[Any] = db_client[db_name]
    return ssh_connection, remote_db
