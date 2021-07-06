import datetime
import sqlite3
from sqlite3 import Error

class Product:
    """
    This class represents the product
    """
    id: int
    name: str
    price: float
    quantity: int


class Sales:
    """
    This class represents sales
    """
    id: int
    pid: int
    quantity: int
    price: float
    createddate: str

def database_file():
    """
    This function will return the database file location
    """
    return 'data/inventory.db'

def create_connection(db_file):
    """
    This method connects to the database and returns the connection
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return connection


def create_table(connection: sqlite3.Connection, create_table_sql: str):
    """
    This method will execute the sql for creating tables
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)

