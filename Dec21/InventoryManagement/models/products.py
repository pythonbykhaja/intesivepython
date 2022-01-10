from datetime import datetime
from models.baseinventory import BaseInventoryModel
import csv

class Product(BaseInventoryModel):
    _file_name = 'data/products.csv'

    """
    This class represents the product
    """
    def __init__(self, id, name, description,category,mrp,created_at=None, updated_at=None):
        """
        Initializer for Product

        :param id: The id of the product
        :param name: The name of the product
        :param description: The description of the product
        :param category: The category of the product
        :param mrp: The maximum retail price of the product
        """
        super().__init__(created_at, updated_at)
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.mrp = mrp

    def __str__(self):
        """
        This is string representation of object
        T"""
        return(f"{self.id}, {self.name}, {self.description}, {self.category}, {self.mrp}, {self.created_at}, {self.updated_at}")
    

    
