def print_hashes():
    print("############################################################")


def welcome(name, func):
    func()
    print(name)
    func()
    name()

if __name__ == "__main__":
    welcome("Python From QT", print_hashes)
    

