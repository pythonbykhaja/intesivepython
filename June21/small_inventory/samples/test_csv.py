import csv

def read_inventory(filename='inventory.csv'):
    with open(filename, 'rt') as inventory:
        # this function automatically closes the file once the code in this block
        # execution is completed

        # create a csv reader
        inventory_csv_reader = csv.reader(inventory)
        for row in inventory_csv_reader:
            print(row)
            print(type(row))

def read_inventory_dict(filename='inventory.csv'):
    with open(filename, 'rt') as inventory:
        # this function automatically closes the file once the code in this block
        # execution is completed

        # create a csv reader
        field_names = ['Id', 'Product', 'Description', 'Quantity']
        inventory_csv_dict_reader = csv.DictReader(inventory, fieldnames=field_names)
        for row in inventory_csv_dict_reader:
            print(row)
            print(type(row))


if __name__ == '__main__':
    read_inventory()
    read_inventory_dict()
        