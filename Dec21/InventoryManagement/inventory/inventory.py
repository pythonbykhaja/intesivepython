from models.products import Product

def add_product(id, name, description,category,mrp):
    """
    This function will add the product
    """
    if id not in Product.ids() :
        product = Product(id, name, description,category,mrp)
        product.save()
    else:
        print(f"Product with id {id} already exists")
