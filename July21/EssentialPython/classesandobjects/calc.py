class Calculator:
    def __init__(self) -> None:
        self.memory = list()

    def add(self, *args):
        result = 0
        for number in args:
            result += number
        self.append_to_memory(result)
        return result

    def multiply(self, *args):
        result = 1
        for number in args:
            result *= number
        self.append_to_memory(result)
        return result
    
    def sub(self, number1, number2):
        result = number1 - number2
        self.append_to_memory(result)
        return result

    def div(self, number1, number2):
        result = number1/number2
        self.append_to_memory(result)
        return 

    def append_to_memory(self,result):
        self.memory.append(result)
            
    def memory_reset(self):
        self.memory.clear()

    def memory_op(self, index):
        return self.memory[index]


calc = Calculator()
calc.add(1,2,3,4,5)
calc.sub(5,1)
calc.div(4,2)
calc.multiply(1,2,3)
print(calc.memory_op(0))
print(calc.memory_op(-1))
    