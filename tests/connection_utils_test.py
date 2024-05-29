"""
Functions to test the connections to the remote servers and to mongo Databases.
"""

import json
from datetime import datetime
from unittest.mock import MagicMock

import pytest
from pymongo.collection import Collection
from pymongo.database import Database
from sshtunnel import SSHTunnelForwarder  # type: ignore

INIT_CHECK_DATETIME = datetime(2022, 2, 10, 0, 0, 0, 0)


@pytest.fixture
def host_server():
    return "test_fake_server"


@pytest.fixture
def database_schema():
    return "testProd"


@pytest.fixture
def mock_ssh_pkey():
    return MagicMock()


@pytest.fixture
def credentials(mock_ssh_pkey):
    try:  # Run inside src folder.
        with open("src/config/template_credentials.json") as credentials_file:
            credentials = json.load(credentials_file)
    except FileNotFoundError:  # Run from folder next to src, e.g. tests.
        with open("../src/config/template_credentials.json") as credentials_file:
            credentials = json.load(credentials_file)

    # Add the mock SSH key to the credentials
    credentials["ssh_pkey_location"] = mock_ssh_pkey
    return credentials


@pytest.fixture
def ssh_connection_instance(credentials, host_server):
    ssh_connection_instance = SSHTunnelForwarder(
        ssh_address_or_host=(
            credentials[host_server]["ip"],
            credentials[host_server]["port"],
        ),
        ssh_username=credentials[host_server]["username"],
        ssh_pkey=credentials["ssh_pkey_location"],
        remote_bind_address=("localhost", 27017),
    )
    return ssh_connection_instance


@pytest.fixture
def db():
    return MagicMock(spec=Database)


@pytest.fixture
def db_collection():
    return MagicMock(spec=Collection)


def test_create_datetime_init_check(
    db: Database, init_check_datetime: datetime = INIT_CHECK_DATETIME
) -> None:
    """
    Create  a collection to store datetime checks, if it doesn't exist.
    Set init datetime to check activities.
    Args:
        init_check_datetime (datetime): The beginning of time for this Database.
        db: The database to use.
        datetime object: The datetime to start checking for activities.
    Returns:
        None.
    """

    # first datetime log to check activities
    if db["misc"].find_one({"key": "checkDatetime"}) is None:
        db["misc"].insert_one({"key": "checkDatetime", "value": init_check_datetime})
    return None