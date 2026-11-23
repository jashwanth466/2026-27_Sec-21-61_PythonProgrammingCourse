# Example solution: private and protected attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._branch = "Main"  # protected (convention)
        self.__balance = balance  # private (name-mangled)

    def get_balance(self):
        return self.__balance


acc = BankAccount("Sita", 1000)
print(acc.owner, acc._branch)
print("Balance:", acc.get_balance())