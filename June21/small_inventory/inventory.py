from dataclasses import dataclass
import csv
from os import write

@dataclass
class Inventory:
    id: int
    name: str
    price: float
    quantity: int
    field_names = ['id', 'name', 'price', 'quantity']

    def to_dict(self):
        inv_dict = dict()
        inv_dict['id'] = self.id
        inv_dict['name'] = self.name
        inv_dict['price'] = self.price
        inv_dict['quantity'] = self.quantity
        return inv_dict

    @staticmethod
    def get_inventory_from_cli():
        id = int(input('Enter the id: '))
        name = input('Enter the product name: ')
        price = float(input('Enter the product price: ')) 
        quantity = int(input('Enter the quanity available: '))
        return Inventory(id,name, price, quantity)

def add_inventory_item(inventory, filename='data/inventory.csv'):
    with open(filename, 'at') as inv_obj:
        writer = csv.DictWriter(inv_obj, inventory.field_names)
        writer.writerow(inventory.to_dict())


if __name__ == '__main__':
    while True:
        inventory = Inventory.get_inventory_from_cli()
        add_inventory_item(inventory)
        choice = input('Do you want to continue? y or n ')
        if choice == 'n':
            break




