
def main_menu():
    """
    This implements the main menu functionality
    Returns
        1. To Add Inventory Items
        2. To Update Inventory
        3. To print all the inventory Items 
    """
    try:
        print("Options")
        print("1. Add Inventory Items")
        print("2. Update Inventory Items")
        print("3. Show Inventory Items")
        choice = int(input("Enter the choice: "))
        if not 1 <= choice <=3:
            raise KeyError('Invalid Choice')
        return choice
    except ValueError as ve:
        raise KeyError(ve)

def does_user_wants_to_continue():
    """
    This method will ask for the user input to continue or to stop
    Returns :
        True if user wants to continue
        False otherwise
    """
    choice = input('Enter n to stop and any other key to continue :')
    if choice == 'n':
        return False
    return True
    
