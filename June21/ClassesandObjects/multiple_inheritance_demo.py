class Animal:
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh............'

class Donkey(Animal):
    def says(self):
        return 'Hee-haw.............'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

a1 = Animal()
print(a1.says())

h1 = Horse()
print(h1.says())

d1 = Donkey()
print(d1.says())

m1 = Mule()
print(Mule.__mro__)
print(m1.says())

h1 = Hinny()
print(Hinny.__mro__)
print(h1.says())