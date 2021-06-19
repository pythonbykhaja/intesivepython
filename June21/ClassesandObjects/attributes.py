class Car:
    """
    This class represents an Car
    """
    def __init__(self, brand, model, reg_no):
        """
        Initalizing the Car with arguments
        brand
        model
        reg_no
        """
        # instance attribute
        self.brand = brand
        self.model = model
        self.reg_no = reg_no

    # class level attribute
    count = 0

# car = Car(brand='Honda', model='City', reg_no='0353')
# print(car.brand)
# print(car.model)
