from datetime import datetime
import csv

class Product:

    file_name = 'data/products.csv'

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

