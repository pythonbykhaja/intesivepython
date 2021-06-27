

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
    
def read_all_contents():
    """
    This function will demonstrate the read method
    """
    computer_file_obj = open('computer.txt', 'rt')
    information = computer_file_obj.read()
    print(information)
    computer_file_obj.close()

def read_by_chunks(chunk_size=100):
    """
    This function demonstrates the read by chunk size (number of characters)
    """
    computer_file_obj = open('computer.txt', 'rt')
    fragment_count = 0
    while True:
        fragment = computer_file_obj.read(chunk_size)
        if not fragment:
            break
        fragment_count += 1
        print(f'Fragment {fragment_count} \n{fragment}')
    computer_file_obj.close()

def read_by_lines():
    """
    This method demonstrates readline
    """
    computer_file_obj = open('computer.txt', 'rt')
    line_count = 0
    while True:
        line = computer_file_obj.readline()
        if not line:
            break
        line_count += 1
        print(f"line: {line_count}\n{line}")
    computer_file_obj.close()

def read_all_lines():
    """
    This method demonstrates readlines()
    """
    computer_file_obj = open('computer.txt', 'rt')
    lines = computer_file_obj.readlines()
    for line in lines:
        print(line)




def seperate_bw_prints(message=""):
    for index in range(100):
        print('#', sep='', end='')
    print()
    print(message)
    for index in range(100):
        print('#', sep='', end='')
    print()



if __name__ == '__main__':
    #write_to_file_using_print()
    #write_to_file_using_write()
    seperate_bw_prints('Read all contents')
    read_all_contents()
    
    seperate_bw_prints('Read by Chunk')
    read_by_chunks(chunk_size=1000)
    seperate_bw_prints('Read by lines')
    read_by_lines()
    seperate_bw_prints('Reading all lines')
    read_all_lines()
    
