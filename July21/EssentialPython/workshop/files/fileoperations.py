def read_and_display(filename):
    """This function will try to read the contents of the text file and 
    display the contents

    Arguments:
       filename (str): path of the file
    """
    file_object = open(file=filename) # open the file 
    text = file_object.read() # read all content
    print(text)
    file_object.close() # close the file

def read_partial_and_display(filename, characters = 10):
    """This function reads files and displays the text as per the characters passed
    """
    file_object = open(file=filename)
    text = file_object.read(characters)
    print(text)
    file_object.close()


if __name__ == '__main__':
    #read_and_display('simple.txt')
    read_partial_and_display('data.txt', 1000)