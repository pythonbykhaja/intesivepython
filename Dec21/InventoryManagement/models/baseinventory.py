from datetime import datetime
import os
import csv


class BaseInventoryModel:
    """
    This represents the base model
    """

    _file_name = ""

    def __init__(self, created_at=None, updated_at=None) -> None:
        """
        This is a base initalizer 
        """
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def save(self):
        """
        This method represents saving the csv
        """
        # check if the folder exists
        data_directory = os.path.dirname(self._file_name)
        # if path not exists create a directory
        if not os.path.exists(data_directory):
            os.mkdir(data_directory)
        is_csv_file_existing = os.path.exists(self._file_name)
        # we need to write these to the csv file
        field_dict = self.__dict__
        with open(self._file_name, 'a') as csv_file:
            #writng to csv using https://docs.python.org/3/library/csv.html#csv.DictWriter
            writer = csv.DictWriter(csv_file, field_dict.keys())
            if not is_csv_file_existing:
                writer.writeheader()
            writer.writerow(field_dict)



