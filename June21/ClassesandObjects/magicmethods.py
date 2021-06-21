class Message:
    def __init__(self, message):
        self.message = message

    def __eq__(self, other):
        return self.message.lower() == other.message.lower()
    
    def __str__(self):
        return self.message

    def __repr__(self):
        return f"message => {self.message}"


hello= Message('Hello')
hai = Message('Hai')
again_hello = Message('Hello')

print(hello == again_hello)
print(hello == hai)
print(str(hai))
print(str(hello))
print(hello)

print(repr(hello))
