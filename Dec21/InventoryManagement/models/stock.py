from models.baseinventory import BaseInventoryModel

class Stock(BaseInventoryModel):
    """
    This class represents the Stock of the items in the Store
    """
    def __init__(self, id, quantity) -> None:
        super().__init__(file_name='data/stocks.csv')
        self.id = id
        self.quantity = quantity
    
    def save(self):
        """
        This method will save the Stock record
        """
        pass

    def update(self, new_quantity):
        """
        This method will updated the stock of the existing product
        """
        pass

    def __str__(self) -> str:
        return f"{self.id}, {self.quantity}"
        