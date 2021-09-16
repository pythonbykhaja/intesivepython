#!/usr/bin/env python
import argparse
import models

def add_default_arguments(subparser):
    """
    This method will add the default arguments
    """
    subparser.add_argument('-t', '--title', type=str, help='title of the book')
    subparser.add_argument('-a', '--author', type=str, help='author of the book')
    subparser.add_argument('-d', '--debug', action="store_true")
    
def argument_parser():
    """
    This method will create the command line argument parsing structure
    """
    books_parser = argparse.ArgumentParser(description="This is books cli")
    subparsers = books_parser.add_subparsers(dest="command")
    add = subparsers.add_parser("add")
    add_default_arguments(add)
    get = subparsers.add_parser("get")
    add_default_arguments(get)
    update = subparsers.add_parser("update")
    add_default_arguments(update)
    update.add_argument('-i', '--id', type=int, help="Id of the book")
    delete = subparsers.add_parser("delete")
    add_default_arguments(delete)

    args = books_parser.parse_args()
    return args

if __name__ == '__main__':
    args = argument_parser()
    models.initialize_database()
    # we need to process arguments and call the necessary model functions
    if args.command == 'add':
        if args.debug:
            print(f"inside add and arguments are {args}")
        models.add_book(title=args.title, author=args.author)
    elif args.command == "get":
        if args.debug:
            print(f"inside get and arguments are {args}")
        for id in models.search_book_by_title(args.title):
            print(f"id is {id}")
    elif args.command == "update":
        if args.debug:
            print(f"inside update and arguments are {args}")
        models.update_book(id=args.id,new_title=args.title, new_author=args.author)
    elif args.command == "delete":
        if args.debug:
            print(f"inside delete and arguments are {args}")
        models.delete_book_by_title(title=args.title)
    