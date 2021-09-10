import yaml
import os

def books_store_location():
    """
    This method will return the books location
    """
    return "data/books.yaml"

def parse_books_into_dict():
    """
    This method is used to parse the json file into dictionary
    """
    if not os.path.exists(books_store_location()):
        return empty_books_dictionary()
    with open(books_store_location(), mode='r') as books_file:
        return yaml.load(books_file)


def empty_books_dictionary():
    """
    This method will return empty books dictionary
    """
    books_dict = {'name': 'qtlibrary', 'books': []}
    return books_dict

def save_books(books_dict):
    """
    This method is used to save the books dictionary
    """
    with open(books_store_location(), mode='wt') as books_file:
        yaml.dump(books_dict,books_file)

def empty_book():
    """
    This method will return empty book structure
    """
    return {'title': '', 'author': ''}
