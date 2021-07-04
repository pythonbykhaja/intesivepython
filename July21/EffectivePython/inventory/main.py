"""
This module is used to store the inventory data 
"""
import inventory
import json
import menu

def write_to_inventory(inventory_dict):
    with open(inventory.inventory_file_path(), 'w') as inv_file:
                json.dump(inventory_dict,inv_file,indent=4)


if __name__ == '__main__':
    print("Enter the inventory details")
    inventory_dict = inventory.load_inventory_dict()

    while True:
        choice = menu.main_menu()

        if choice == 1:
            # Add inventory
            inv = inventory.Inventory.read_inventory_from_input()
            inventory_dict['items'].append(inv.to_dict())
            write_to_inventory(inventory_dict)
        elif choice == 2:
            # Update the inventory
            id = int(input('Enter the Id: '))
            count = 0
            for item in inventory_dict['items']:
                if id == item['id']:
                    print('product found')
                    print(item)
                    price = item['price']
                    choice = input(f'price: [{price}]')
                    if choice.strip() != '':
                        new_price = float(choice.strip())
                        item['price'] = new_price
                    quantity = item['quantity']
                    choice = input(f'quantity: [{quantity}]')
                    if choice.strip() != '':
                        new_quantity = int(choice.strip())
                        item['quantity'] = new_quantity
                    inventory_dict['items'][count] = item
                    write_to_inventory(inventory_dict)
                    break
                count = count + 1
            
        else:
            # Show the inventory
            for item in inventory_dict['items']:
                print(str(item))

        if not menu.does_user_wants_to_continue():
            break
        
    
    


        
