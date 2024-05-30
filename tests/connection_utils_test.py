"""
Functions to test the connections to the remote servers and to mongo Databases.
"""

import sys
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest
from pymongo.collection import Collection
from pymongo.database import Database

sys.path.insert(0, "./../src")
sys.path.insert(0, "./src")
sys.path.insert(0, "./src/utils")

from utils import connection_utils

INIT_CHECK_DATETIME = datetime(2022, 2, 10, 0, 0, 0, 0)


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

    assert db["misc"].find_one({"key": "checkDatetime"}) is not None


def test_successful_db_connection(db):
    database_name = "testProd"
    machine = "local_pc"
    credentials = {
        "testProd": {
            "mongodbUser": "testProdUser",
            "mongodbDatabase": "testProd",
            "mongodbPassword": "test_pwd",
        },
    }

    # Mock the connect_to_localhost_db function to return the mock db
    with patch("connection_utils.connect_to_localhost_db", return_value=db):
        # Test connection to an existing local database
        db = connection_utils.connect_to_localhost_db(
            database_name, machine, credentials
        )

        # Verify
        assert db is not None


def test_init_new_db(db):
    database_name = "testProd"
    schema = "Prod"
    machine = "local_pc"
    new_db_name = "test"
    credentials = {
        "testProd": {
            "mongodbUser": "testProdUser",
            "mongodbDatabase": "testProd",
            "mongodbPassword": "test_pwd",
        },
    }

    # Mock the connect_to_localhost_db function to return the mock db
    with patch("connection_utils.connect_to_localhost_db", return_value=db):
        # Test connection to an existing local database
        db = connection_utils.connect_to_localhost_db(
            database_name, machine, credentials
        )

        # Mock the connect_to_localhost_db function to return the mock db
        with patch("connection_utils.connect_to_localhost_db", return_value=db):
            # Test init new database
            connection_utils.init_new_db(
                schema, credentials, machine, new_db_name=new_db_name
            )

        # Verify
        assert db is not None


def test_failed_db_connection():
    # Setup
    db_schema = "testProd"
    machine = "local_pc"
    invalid_credentials = {"username": "invalid", "password": "invalid"}

    # Exercise and Verify
    with pytest.raises(Exception):  # replace with the specific exception you expect
        connection_utils.connect_to_localhost_db(
            db_schema, machine, invalid_credentials
        )
