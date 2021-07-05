import os
from dataclasses import dataclass
import json

def get_empty_inventory():
    """
    This method returns an empty dictionary containing 
    inventory data
    """
    inventory_dict = dict()
    inventory_dict['items'] = list()
    return inventory_dict

def inventory_file_path():
    """
    This method returns standard inventory file path
    """
    return 'data/inventory.json'

def get_inventory_index(inventory_dict, id):
    """
    This method returns the index of the item in inventory dictionary
    Returns:
       index of the item if found

    Raises:
        KeyError if the id is not found
    """
    count = 0
    for item in inventory_dict["items"]:
        if item['id'] == id:
            return count
        count += 1
    raise KeyError("Id not found")





def is_inventory_available():
    """
    Returns:
      True if the inventory file is found else returns false
    """
    return os.path.exists(inventory_file_path()) and os.path.isfile(inventory_file_path())

def load_inventory_dict():
    if is_inventory_available():
        with open(inventory_file_path()) as inv_file:
            return json.load(inv_file)
    return get_empty_inventory()



@dataclass
class Inventory:
    id: int
    name: str
    price: float
    quantity: int

    def to_dict(self):
        """
        This method returns dictionary representation of Inventory object
        """
        inv = dict()
        inv['id'] = self.id
        inv['name'] = self.name
        inv['price'] = self.price
        inv['quantity'] = self.quantity
        return inv

    def __str__(self) -> str:
        return f"{self.id}, {self.name}, {self.price}, {self.quantity}"

    @staticmethod
    def header():
        return f"id, name, price, quantity"



    @staticmethod
    def read_inventory_from_input():
        id = int(input('Enter the id: '))
        name = input('Enter the product name: ')
        price = float(input('Enter the product price: '))
        quantity = int(input('Enter the quantity: '))
        inventory = Inventory(id,name,price,quantity)
        return inventory