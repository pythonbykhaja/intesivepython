

def write_to_file_using_print():
    """
    In this method we write the content to the file using print statemetn
    """
    print_to_file = 'print.txt'
    print_file_obj = open(file=print_to_file, mode='wt')
    print('Printing numbers till 100', file=print_file_obj)
    for index in range(100):
        print(index, file=print_file_obj)
    print_file_obj.close()


def write_to_file_using_write():
    """
    This function is used to demonstrate using write funcion 
    """
    file_name = "review.txt"
    file_obj = open(file=file_name, mode='wt')
    quotes = '''The purpose of our lives is to be happy. — Dalai Lama,
    Life is what happens when you’re busy making other plans. — John Lennon
    Get busy living or get busy dying. — Stephen King
    You only live once, but if you do it right, once is enough. — Mae West
    '''
    print(f'length of quotes: {len(quotes)}')
    count = file_obj.write(quotes)
    print(f"file written succesfully and the return value is {count}")
    file_obj.close()
    


if __name__ == '__main__':
    write_to_file_using_print()
    write_to_file_using_write()
