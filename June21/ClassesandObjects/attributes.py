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
        Car.count += 1

    def info(self):
        """
        This instance method prints the information about the 
        instance attributes and class attributes defined
        """
        print(f"Brand = {self.brand} id = {id(self.brand)}")
        print(f"Model = {self.model} id = {id(self.model)}")
        print(f"Reg-No = {self.reg_no} id = {id(self.reg_no)}")
        print(f"Count = {Car.count}, id = {id(Car.count)}")

    # class level attribute
    count = 0

ms_car = Car(brand='Maruti', model='Swift', reg_no='123')
hc_car = Car(brand='Hyundai', model='Creta', reg_no='124')
ms_car.info()
hc_car.info()


