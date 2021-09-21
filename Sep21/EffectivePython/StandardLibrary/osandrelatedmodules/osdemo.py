import os



def current_cwd():
    cwd = os.getcwd()
    print(f"the current working directory is {cwd}")

if __name__ == "__main__":
    current_cwd()
    os.chdir("../")
    current_cwd()
    folder_path = os.path.join(os.getcwd(),'osandrelatedmodules')
    os.chdir(folder_path)
    current_cwd()
    parent_directory = os.getcwd()
    data_dir = os.path.join(parent_directory,"data")
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    
    # recursive folder creation
    csv_dir = os.path.join(data_dir,"files", "csv")
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)

    parent_directory = "D:\\khajaclassroom\\python_intensive"
    dir_list = os.listdir(parent_directory)
    print(dir_list)

    parent_directory="D:\\temp\\test"
    for root, d_names, f_names in os.walk(parent_directory):
        print(root,d_names,f_names)

    # Commonly used functions
    print(os.name)

    #os.rename(src="test.txt", dst="newtest.txt")

    #os.path.getsize()


    

