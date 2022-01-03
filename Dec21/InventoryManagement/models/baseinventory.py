from datetime import datetime


class BaseInventoryModel:
    """
    This represents the base model
    """
    def __init__(self, file_name) -> None:
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.file_name = file_name

    def save(self):
        """
        This method represents saving the csv
        """
        pass