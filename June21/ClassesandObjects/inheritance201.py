class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"Person(name={self.name})"

class Doctor(Person):
    def __init__(self, name, specialization):
        # default behavior
        #super().__init__(name)
        self.name = f"Dr. {name}"
        self.specialization = specialization
    def __repr__(self) -> str:
        return f"{super().__repr__()} Doctor(specialization= {self.specialization})"

class Engineer(Person):
    def __init__(self, name, category):
        super().__init__(name)
        self.category = category

    def __repr__(self) -> str:
        return f"{super().__repr__()} Engineer(category= {self.category})"

khaja = Person(name='khaja')
print(str(khaja))
print(repr(khaja))

anand = Doctor(name='Anand', specialization='MD')
print(str(anand))
print(repr(anand))

ramana = Engineer(name='Ramana', category='computers')
print(str(ramana))
print(repr(ramana))


        