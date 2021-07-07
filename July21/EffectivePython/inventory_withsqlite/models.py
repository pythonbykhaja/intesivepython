import datetime
import sqlite3
from sqlite3 import Error
from dataclasses import dataclass

@dataclass
class Product:
    """
    This class represents the product
    """
    id: int
    name: str
    price: float
    quantity: int

    @staticmethod
    def create_product_from_userinput():
        """
        This method will create product from the user input
        Returns:
          Product
        """
        id = int(input('Enter Id: '))
        name = input('Enter Product Name: ')
        price = float(input('Enter product price: '))
        quantity = int(input('Enter quanity: '))
        return Product(id=id, name=name,price=price,quantity=quantity)


    def save(self):
        """
        This statement will insert the product into the database
        """
        insert_statement = f"INSERT into products (id, name, price, quantity)  VALUES({self.id}, '{self.name}', {self.price}, {self.quantity})"
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            cursor.execute(insert_statement)
            connection.commit()
        

@dataclass
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

def create_connection(db_file) -> sqlite3.Connection:
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

