import os
from dataclasses import dataclass
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

def is_inventory_available():
    """
    Returns:
      True if the inventory file is found else returns false
    """
    return os.path.exists(inventory_file_path()) and os.path.isfile(inventory_file_path())

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

    @staticmethod
    def read_inventory_from_input():
        id = int(input('Enter the id: '))
        name = input('Enter the product name: ')
        price = float(input('Enter the product price: '))
        quantity = int(input('Enter the quantity: '))
        inventory = Inventory(id,name,price,quantity)
        return inventory