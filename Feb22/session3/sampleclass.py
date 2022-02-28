class BankAccount:
    total_count = 0
    
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
        self.account_number = f"{branch}-{self.total_count}"
        self.balance = 0
        

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    @classmethod
    def increment_count(cls):
        cls.total_count += 1

    @staticmethod
    def print_hello():
        print("hello")

if __name__ == '__main__':
    BankAccount.increment_count()
    b = BankAccount('bhawana', 'ameerpet')
    b.deposit(10000)
