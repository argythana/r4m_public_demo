"""
Functions to connect to remote servers and to MongoDB Databases.
Make sure to have the credentials.json file in the config folder.
Use the template_credentials.json file to create your own credentials.json file.
Use from local PC for dev and testing and from localhost on VMs for production.
"""

from __future__ import annotations

from datetime import datetime
from typing import List

import pymongo
from pymongo.collection import Collection
from pymongo.database import Database
from sshtunnel import SSHTunnelForwarder  # type: ignore

# First Datetime log
INIT_CHECK_DATETIME = datetime(2022, 2, 10, 0, 0, 0, 0)


def ssh_to_remote_server(host_server: str, credentials: dict) -> SSHTunnelForwarder:
    """
    SSH into remote server.
    Args:
        host_server: The server to connect to. IP, port, username should be in credentials.json.
            Available options are: "app_server", "analytics_server".
        credentials: Data in dict format from to the credentials.json file.
    Return: server_instance, an SSHTunnelForwarder.
    """

    # SSH Tunnel into the remote VM
    ssh_connection_instance = SSHTunnelForwarder(
        ssh_address_or_host=(
            credentials[host_server]["ip"],
            credentials[host_server]["port"],
        ),
        ssh_username=credentials[host_server]["username"],
        remote_bind_address=("localhost", 27017),
    )
    return ssh_connection_instance


def connect_to_remote_db(
    host_server: str, database_schema: str, credentials: dict
) -> Database:
    """
    Connect to a MongoDB database on a remote sever from local PC.
    Args:
        host_server: The server to connect to. IP, port, username should be in credentials.json.
        database_schema: The database schema (name) to connect to. Examples options are:
            appProd, appDev, tasksProd, tasksDev, analyticsDev, analyticsProd.
            The database_schema contains username, pwd and name of Database.
            The schema has version suffix: Prod or Dev. So, we need also the prefix: tasks, or app, or analytics.
            For "non-app" DBs the scope and the DB name are identical.
        credentials: Data in dict format from the credentials.json file.
    Return: A database object with access to all remote DB collections.
    """

    ssh_connection_instance = ssh_to_remote_server(host_server, credentials)
    # start the SSH tunnel. Close it after use.
    ssh_connection_instance.start()

    # which DB to connect to. Is the name from a schema.
    db_name: str = credentials[database_schema]["mongodbDatabase"]

    # Connect to the MongoDB database
    db_client: pymongo.MongoClient = pymongo.MongoClient(
        host="localhost",
        port=ssh_connection_instance.local_bind_port,
        username=credentials[database_schema]["mongodbUser"],
        password=credentials[database_schema]["mongodbPassword"],
        authSource=db_name,
    )
    remote_db: Database = db_client[db_name]
    return remote_db


def connect_to_localhost_db(
    database_schema: str, machine: str, credentials: dict
) -> Database:
    """
    Connect to the local MongoDB database on the localhost.
    Use on local PC for development and on remote VMs for production.
    Args:
        database_schema: The database schema (name) to connect to. Examples of DBs:
            "run4moreProd", "run4moreDev", "tasksProd", "tasksDev", "analyticsDev", "analyticsProd".
            The schema has suffix from dbVersion: Prod or Dev.
            We need also the prefix  "tasks", "app", or "analytics", or "test".
        machine: remote server or local PC. Arguments can be "remote" or "local_pc".
            The "machine" argument is already set accordingly on local PC and on VMs in the credentials.json file.
        credentials: Data in dict format from to the credentials.json file.
    Return: A database object with access to all collections.
    """

    # The DB to connect to. Is the name from a schema.
    db_name: str = credentials[database_schema]["mongodbDatabase"]

    # Connect to the MongoDB database
    db_client: pymongo.MongoClient = pymongo.MongoClient(
        host="localhost",
        port=27017,
        username=credentials[database_schema]["mongodbUser"] if machine == "vm" else "",
        password=(
            credentials[database_schema]["mongodbPassword"] if machine == "vm" else ""
        ),
        authSource=db_name,
    )
    # Create new local DB and name it according to credentials template.
    local_db: Database = db_client[db_name]
    return local_db


def copy_remote_app_db_on_local_pc(
    host_server: str,
    schema: str,
    credentials: dict,
    machine: str,
    copy_collections: List[str],
    *,
    source_db: str = "app",
    target_db: str = "app",
) -> None:
    """
    Connect to MongoDB on a remote server and copy the selected collections to a DB on local PC.
    You may copy the "app" DB collections to the "analytics" DB any other DB as long credentials are in config.json.
    By default, this function is hardcoded to copy from the remote "app" DB to local "app" DB.
    So, both source and target DBs in this function are hardcoded to "appProd" (collections created by app).
    Args:
        host_server: The server to connect to. Should be selected from the credentials.json file.
            Available options are: "app_server", "analytics_server".
        schema: The schema to connect to. The available schema suffix are "Prod" or "Dev".
        credentials: Credentials data in dict format from to the credentials.json file.
        machine: options are "local_pc", or "vm".
        copy_collections: A list of DB collection names, to copy from remote to local.
        source_db: str = "app", Copy from remote "app" DB. Other option is "analytics".
        target_db: str = "app", Copy to local "app" DB. Other option is "analytics".
    Return: None
    """
    # DB to copy from.
    from_remote_db: Database = connect_to_remote_db(
        host_server, source_db + schema, credentials
    )

    # DB to copy to. Gets the same schema as the remote DB.
    db_target = connect_to_localhost_db(target_db + schema, machine, credentials)

    # Copy listed collections from the VM database to a local database.
    # TODO: Refactor to update if collection exists. Code breaks if collection exists
    for db_collection in copy_collections:
        db_collection_documents = list(from_remote_db[db_collection].find())
        # Create the collections on the local PC database.
        db_target[db_collection].insert_many(db_collection_documents)

    # Close the connections.
    from_remote_db.client.close()
    db_target.client.close()
    return None


def create_datetime_init_check(
    db_collection: Collection, init_check_datetime: datetime = INIT_CHECK_DATETIME
) -> None:
    """
    Create a DB collection to store datetime checks, if it doesn't exist.
    Set init datetime to check before updating future collections.
    Args:
        init_check_datetime (datetime): The beginning of time for this Database.
        db_collection: The database instance to use.
        datetime object: The datetime to start checking for activities.
    Returns:
        None.
    """

    # A collection containing only datetime logs to check before updating future collections.
    if db_collection["misc"].find_one({"key": "checkDatetime"}) is None:
        db_collection["misc"].insert_one(
            {"key": "checkDatetime", "value": init_check_datetime}
        )
    return None


def init_new_db(
    schema: str,
    credentials: dict,
    machine: str,
    *,
    new_db_name: str = "test",
) -> None:
    """
    Initialize a new localhost database with a first datetime log
    Args:
        schema: The database version to create. Can be "Prod" or "Dev".
        credentials: Data in dict format from to the credentials.json file.
        machine: remote server or local PC.
            The default in credentials.json on Remote VMs is 'vm'.
            The default in credentials.json on local workstation is 'local_pc'.
        new_db_name: str = "test", The prefix of the new database name.
    Return: None
    """

    # Connect to a MongoDB Database
    new_db: Database = connect_to_localhost_db(
        new_db_name + schema, machine, credentials
    )

    # Init first datetime log.
    create_datetime_init_check(new_db["misc"], INIT_CHECK_DATETIME)

    new_db.client.close()
