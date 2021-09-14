import models

if __name__ == '__main__':
    models.initialize_database()
    #models.add_book('Who moved my cheese', 'spenser')
    models.search_book_by_title('Who')
