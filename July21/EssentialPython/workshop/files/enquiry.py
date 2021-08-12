"""This file stores the information of users who have enquired for a course
"""
enquiry_data_file = 'data/enquiry.txt'


def main():
    """
    This function will be used for interacting or entering data
    """
    while True:
        message = """
    1. Add Enquiry information
    2. show all Enquires
    3. quit

    Enter your choice? 
    """
        choice = input(message)
        if choice == '1':
            ask_user_input()
        elif choice == '2':
            print('Code under progress')
        else:
            break


def ask_user_input():
    name = input('Enter your name: ')
    mobile = input('Enter your mobile: ')
    course = input('Enter the course which you are looking for : ')

    with open(file=enquiry_data_file, mode='a') as file_object:
        file_object.write(f"{name}, {mobile}, {course}\n")




if __name__ == '__main__':
    main()