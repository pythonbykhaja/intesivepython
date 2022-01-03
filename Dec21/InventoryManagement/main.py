from inventory import inventory
from models.products import Product


def get_input_from_user(field_name):
    """
    This is the reusable method to collect input from user
    """
    result = input(f"Enter {field_name}: ")
    return result

if __name__ == '__main__':

    id = get_input_from_user('id')
    name = get_input_from_user('name')
    description = get_input_from_user('description')
    category = get_input_from_user('category')
    mrp = float(get_input_from_user('mrp'))

    inventory.add_product(id, name,description,category,mrp)
    for item in inventory.product_list:
        print(item)