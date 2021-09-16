import os
import sqlite3
from sqlite3.dbapi2 import Error

def database_file_path():
    """
    This function returns the database file path
    """
    return 'data/library.db'

def initialize_database():
    """
    This method will check if the db file exists or not.
    If the file doesn't exist a db file with empty database will be created
    """
    if not os.path.exists(database_file_path()):
        connection = sqlite3.connect(database_file_path())
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE books 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(50) NOT NULL,
        author VARCHAR(50)
        )
        ''')
        connection.close()

def add_book(title, author):
    """
    This method will add the book
    """
    try:
        connection = sqlite3.connect(database_file_path())
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO books (title, author) VALUES ('{title}','{author}')")
        connection.commit()
    finally:
        connection.close()

def search_book_by_title(title):
    """
    This method will search the book from the books table depending on title
    """
    connection = None
    try:
        connection = sqlite3.connect(database_file_path())
        cursor = connection.cursor()
        cursor.execute(f"select * from books where title like '%{title}%'")
        rows = cursor.fetchall()
        for row in rows:
            print(f"id --> {row[0]} title --> {row[1]} author --> {row[2]} ")
            yield row[0]
    except Error as e:
        print(e)
    finally:
        connection.close()


def update_book(id, new_title, new_author):
    """
    update the book with new_title and new_author
    """
    connection = None
    try:
        connection = sqlite3.connect(database_file_path())
        sql = f""" UPDATE books
        SET title='{new_title}', author='{new_author}'
        where id = {id}
        """
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except Error as e:
        print(e)
    finally:
        connection.close()


def delete_book_by_title(title):
    """
    Delete the book by title
    """
    for id in search_book_by_title(title):
        try:
            sql = 'DELETE FROM books where id=?'
            connection = sqlite3.connect(database_file_path())
            connection.execute(sql, (id,))
            connection.commit()
        except Error as e:
            print(e)
        finally:
            connection.close()



