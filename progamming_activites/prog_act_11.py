
#activity 1
import math

class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def diagonal(self):
        return self.side * math.sqrt(2)


# Create a square with a side length of 5
square1 = Square(5)

print("Perimeter:", square1.perimeter())
print("Area:", square1.area())
print("Diagonal:", square1.diagonal())


#activity 2

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount


# Create an account with $100
account1 = BankAccount("Andre", 100)

# Deposit $50
account1.deposit(50)

# Display owner and updated balance
print("Owner:", account1.owner)
print("Balance: $", account1.get_balance())


