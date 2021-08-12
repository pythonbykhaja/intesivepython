def read_and_display(filename):
    """This function will try to read the contents of the text file and 
    display the contents

    Arguments:
       filename (str): path of the file
    """
    with open(file=filename) as file_object:
        text = file_object.read() # read all content
        print(text)

def read_partial_and_display(filename, characters = 10):
    """This function reads files and displays the text as per the characters passed
    """
    with open(file=filename) as file_object:
        text = file_object.read(characters)
        print(text)    


if __name__ == '__main__':
    #read_and_display('simple.txt')
    read_partial_and_display('data.txt', 1000)