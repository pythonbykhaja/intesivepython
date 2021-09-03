class Address:
    def __init__(self, street, city, pincode) -> None:
        self.street = street
        self.city = city
        self.pincode = pincode

class Student:
    def __init__(self,name, email, street, city, pincode) -> None:
        self.name = name
        self.email = email
        self.address = Address(street,city, pincode)

class Faculty:
    def __init__(self,name, email, street, city, pincode) -> None:
        self.name = name
        self.email = email
        self.address = Address(street,city, pincode)
        