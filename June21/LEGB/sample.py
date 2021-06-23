animal = 'Tiger'

def local_function():
    animal = 'Lion'
    print(animal)
    print(f"Locals are {locals()}")
    print(f"Globals are {globals()}")

local_function()

def change_global():
    global animal
    animal = 'Lion'
    print(animal)

change_global()
print(animal)
