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


if __name__ == '__main__':
    read_and_display('simple.txt')