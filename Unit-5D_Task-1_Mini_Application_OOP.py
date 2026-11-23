# Example solution: simple bank account mini application
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print(f"Owner: {self.owner}, Balance: {self.__balance}")


acc = BankAccount("Krishna", 1000)
acc.display()
acc.deposit(500)
acc.withdraw(200)
acc.display()