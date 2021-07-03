"""
This module is used to store the inventory data 
"""
import inventory
import json

if __name__ == '__main__':
    print("Enter the inventory details")
    inventory_dict = inventory.load_inventory_dict()

    while True:
        inv = inventory.Inventory.read_inventory_from_input()
        inventory_dict['items'].append(inv.to_dict())
        choice = input('Enter n to stop and any other key to continue')
        if choice == 'n':
            break
    
    with open(inventory.inventory_file_path(), 'w') as inv_file:
        json.dump(inventory_dict,inv_file,indent=4)


        
