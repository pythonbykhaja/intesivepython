import argparse


if __name__ == '__main__':
    books_parser = argparse.ArgumentParser(description="This is books cli")
    subparsers = books_parser.add_subparsers()
    init = subparsers.add_parser("init")
    init.add_argument('-p','--path', type=str, default='data/library.db')
    add = subparsers.add_parser("add")
    add.add_argument('-t', '--title', type=str, help='title of the book')
    add.add_argument('-a', '--author', type=str, help='author of the book')
    args = books_parser.parse_args()
    # we need to process arguments and call the necessary model functions
    