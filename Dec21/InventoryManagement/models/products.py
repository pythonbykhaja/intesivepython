from datetime import datetime
from models.baseinventory import BaseInventoryModel
import csv

class Product(BaseInventoryModel):
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
        super().__init__(file_name='data/products.csv')
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.mrp = mrp

    def __str__(self):
        """
        This is string representation of object
        T"""
        return(f"{self.id}, {self.name}, {self.description}, {self.category}, {self.mrp}, {self.created_at}")
    
    def save(self):
        """
        This method will save the Current Object to the file
        """
        with open(self.file_name, 'a') as file:
            writer = csv.writer(file, delimiter = ',')
            writer.writerow([self.id, self.name, self.description, self.category, self.mrp,self.created_at ])

    @classmethod
    def ids(cls):
        """
        This method will read all the existing ids from the csv file 
        """
        item_ids = []
        with open(cls.file_name, 'r') as file:
            reader = csv.reader(file, delimiter = ',')
            for row in reader:
                if len(row) > 0:
                    item_ids.append(row[0])
        return item_ids
