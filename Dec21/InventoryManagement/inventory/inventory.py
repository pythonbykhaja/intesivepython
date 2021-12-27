from models.products import Product

product_list = []


def add_product(id, name, description,category,mrp):
    """
    This function will add the product
    """
    product = Product(id, name, description,category,mrp)
    product_list.append(product)
