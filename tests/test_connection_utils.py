"""
Functions to test the connections to the remote servers and to mongo Databases.
"""

import json
from datetime import datetime
from unittest.mock import MagicMock
from typing import cast

import pymongo
import pytest
from pymongo.collection import Collection
from pymongo.database import Database
from sshtunnel import SSHTunnelForwarder  # type: ignore

INIT_CHECK_DATETIME = datetime(2022, 2, 10, 0, 0, 0, 0)


@pytest.fixture
def host_server():
    return "app_server"


@pytest.fixture
def credentials():
    try:  # Run inside src folder.
        with open("src/config/credentials.json") as credentials_file:
            credentials = json.load(credentials_file)
    except FileNotFoundError:  # Run from folder next to src, e.g. tests.
        with open("../src/config/credentials.json") as credentials_file:
            credentials = json.load(credentials_file)
    return credentials


@pytest.fixture
def db_collection():
    return MagicMock(spec=Collection)


@pytest.fixture
def database_schema():
    return "appProd"


def test_ssh_to_remote_server(
    host_server: str, credentials: dict
) -> SSHTunnelForwarder:
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
        ssh_pkey=credentials["ssh_pkey_location"],
        remote_bind_address=("localhost", 27017),
    )
    assert isinstance(ssh_connection_instance, SSHTunnelForwarder)
    return ssh_connection_instance


def test_create_datetime_init_check(
    db_collection: Collection, init_check_datetime: datetime = INIT_CHECK_DATETIME
) -> None:
    """
    Create  a collection to store datetime checks, if it doesn't exist.
    Set init datetime to check activities.
    Args:
        init_check_datetime (datetime): The beginning of time for this Database.
        db_collection: The database collection to use.
        datetime object: The datetime to start checking for activities.
    Returns:
        None.
    """

    # first datetime log to check activities
    if db_collection["misc"].find_one({"key": "checkDatetime"}) is None:
        db_collection["misc"].insert_one(
            {"key": "checkDatetime", "value": init_check_datetime}
        )
    return None


def test_connect_to_remote_db(
    host_server: str, database_schema: str, credentials: dict
) -> None:
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

    with SSHTunnelForwarder(
        ssh_address_or_host=(
            credentials[host_server]["ip"],
            credentials[host_server]["port"],
        ),
        ssh_username=credentials[host_server]["username"],
        ssh_pkey=credentials["ssh_pkey_location"],
        remote_bind_address=("localhost", 27017),
    ) as ssh_connection_instance:
        ssh_connection_instance = cast(SSHTunnelForwarder, ssh_connection_instance)

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
        assert isinstance(remote_db, Database)
