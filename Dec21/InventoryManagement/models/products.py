from datetime import datetime

class Product:
    """
    This class represents the product
    """
    def __init__(self, id, name, description,category,mrp):
        """
        Initializer for Product

        :param id: The id of the product
        :param name: The name of the product
        :param description: The description of the product
        :param category: The category of the product
        :param mrp: The maximum retail price of the product
        """
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.mrp = mrp
        self.created_at = datetime.now()
        # todo: fix the updated_at to be changed when attributes are changed
        self.upated_at = datetime.now()

    def __str__(self):
        return(f"{self.id}, {self.name}, {self.description}, {self.category}, {self.mrp},  {self.created_at}")

