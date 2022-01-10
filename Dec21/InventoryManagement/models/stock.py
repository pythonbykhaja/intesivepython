from models.baseinventory import BaseInventoryModel

class Stock(BaseInventoryModel):

    _file_name='data/stocks.csv'

    """
    This class represents the Stock of the items in the Store
    """
    def __init__(self, id, product_id, quantity, created_at=None, updated_at=None) -> None:
        super().__init__(created_at, updated_at)
        self.id = id
        self.product_id = product_id
        self.quantity = quantity

    

    def update(self, new_quantity):
        """
        This method will updated the stock of the existing product
        """
        pass

    def __str__(self) -> str:
        return f"{self.id}, {self.quantity}"
        