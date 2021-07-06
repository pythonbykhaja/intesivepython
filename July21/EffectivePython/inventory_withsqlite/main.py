import sqlite3
import models

if __name__ == '__main__':
    
    sql_products_create_table = """
    CREATE TABLE IF NOT EXISTS products (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price real NOT NULL,
        quantity int 
    )
    """
    sql_sales_create_table = """
    CREATE TABLE IF NOT EXISTS sales (
        id integer PRIMARY KEY,
        product_id integer,
        quantity integer,
        created_date text NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(id)
        
    )
    """
    connection = models.create_connection(models.database_file())
    if connection is not None:
        models.create_table(connection, sql_products_create_table)
        models.create_table(connection, sql_sales_create_table)
        

    