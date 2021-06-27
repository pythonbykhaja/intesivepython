

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

if __name__ == '__main__':
    write_to_file_using_print()
