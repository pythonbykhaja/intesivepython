import bookmodel


def add_book():
    books_dict = bookmodel.parse_books_into_dict()
    title = input('Enter the name of the book: ')
    author = input('Enter the author: ')
    books_dict['books'].append({'title': title, 'author': author})
    bookmodel.save_books(books_dict)

def query_book():
    title= input('Enter book name')
    books_dict = bookmodel.parse_books_into_dict()
    for book in books_dict['books']:
        if book['title'] == title:
            print("book found")
            print(f"title = {book['title']} author = {book['author']}")
            break
    else:
        print('cannot find the book')


if __name__ == '__main__':
    # write code here to ask the user who executes the program
    # To enter book details and store it in the json file
    while True:
        selection = int(input("Enter \n1 for Adding book \n2 for Searching Book: "))
        if selection == 1:
            add_book()
        else:
            query_book()
        choice = input('Do you want to continue? press N to exit')
        if choice == 'N':
            break
