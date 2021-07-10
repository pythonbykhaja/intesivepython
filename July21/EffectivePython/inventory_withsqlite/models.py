import datetime
import sqlite3
from sqlite3 import Error
from dataclasses import dataclass
from sqlite3.dbapi2 import Cursor

@dataclass
class Product:
    """
    This class represents the product
    """
    id: int
    name: str
    price: float
    quantity: int

    def __str__(self) -> str:
        return f"{self.id}, {self.name}, {self.price}, {self.quantity}"

    def header() -> str:
        return "id, name, price, quantity"

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

        Raises:
          sqlite3.IntegrityError: When inserting a product with same id
        """
        insert_statement = f"INSERT into products (id, name, price, quantity)  VALUES({self.id}, '{self.name}', {self.price}, {self.quantity})"
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            cursor.execute(insert_statement)
            connection.commit()

    def sell(self, quantity):
        """
        This method will reduce the quantity of the item sold from inventory
        """
        update_statement = f"UPDATE products SET quantity={self.quantity-quantity} WHERE id={self.id}"
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            cursor.execute(update_statement)
            connection.commit()

    def update(self):
        """
        This method will implement the update to the database
        """
        update_statement = f"UPDATE products SET name='{self.name}',price={self.price},quantity={self.quantity} WHERE id={self.id}"
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            cursor.execute(update_statement)
            connection.commit()

    @staticmethod
    def get_all_products():
        select_query = "SELECT * from products"
        products = list()
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(select_query):
                product = Product(row[0],row[1], row[2], row[3])
                products.append(product)
        return products
                



        

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

