import sqlite3
import models

def initialize():
    sql_products_create_table = """
    CREATE TABLE IF NOT EXISTS products (
        id integer PRIMARY KEY,
        name text NOT NULL,
        price real NOT NULL,
        quantity int 
    )
    """
    sql_sales_create_table = """
    CREATE TABLE IF NOT EXISTS sales (
        id integer PRIMARY KEY,
        product_id integer,
        quantity integer,
        created_date text NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(id)
        
    )
    """
    connection = models.create_connection(models.database_file())
    if connection is not None:
        models.create_table(connection, sql_products_create_table)
        models.create_table(connection, sql_sales_create_table)

    connection.close()

def insert_product(products, ids):
    print("Enter product information")
    product = models.Product.create_product_from_userinput()
    if product.id in ids:
        print(f"change the id as there is existing product with id = {product.id} ")
    else:
        product.save()

def display_products(products):
    print(models.Product.header())
    for product in products:
        print(str(product))

def accept_change_from_user(field_name: str, current_value: str):
    result = input(f"Enter {field_name}: [{current_value}] ")
    if result.strip() != "" and result != current_value:
        return result
    return None


def update_product(products, ids):
    print('Update product')
    id = int(input('Enter the id of the product'))
    if id not in ids:
        print("Invalid Id entered")
    else:
        selected_product: models.Product = list(filter(lambda product: product.id == id),products)[0]
        #selected_product: models.Product = [product for product in products if product.id == id][0]
        result = accept_change_from_user('name', selected_product.name)
        is_updated = False
        if result:
            is_updated = True
            selected_product.name = result
        result = accept_change_from_user('price', str(selected_product.price))
        if result:
            is_updated = True
            selected_product.price = float(result)
        result = accept_change_from_user('quantity', str(selected_product.quantity))
        if result:
            is_updated = True
            selected_product.quantity = int(result)
        
        if is_updated:
            selected_product.update()

    
    

def main_menu():
    print("Welcome to Inventory")
    choice = int(input("Enter 1 for inventory and 2 for sales "))
    if choice == 1:
        products = models.Product.get_all_products()
        ids = [product.id for product in products]
        inventory_choice = int(input("Enter 1 to create item, 2 to view items 3 to update items "))
        if inventory_choice == 1:
            insert_product(products, ids)
        elif inventory_choice == 2:
            display_products(products)
        elif inventory_choice == 3:
            update_product(products, ids)
    elif choice == 2:
        pass



if __name__ == '__main__':
    initialize()
    products = models.Product.get_all_products()
    ids = [product.id for product in products]
    while True:
        try:
            main_menu()
            choice = input('Enter n to stop and y to continue: ')
            if choice == 'n':
                break
        except sqlite3.IntegrityError as ie:
            print("You have entered the product with existing id")
            

    
    


        

    