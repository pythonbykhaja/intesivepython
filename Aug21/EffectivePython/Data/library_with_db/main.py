import models

if __name__ == '__main__':
    models.initialize_database()
    models.add_book('Who moved my cheese', 'spenser')
    models.search_book_by_title('Who')

    for id in models.search_book_by_title('Who'):
        models.update_book(id, 'Who Moved My Cheese', 'Dr Spenser Johnson')

    models.delete_book_by_title('Who')
