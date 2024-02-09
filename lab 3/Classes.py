#Python Classes

#Ex.1
class StringManipulator:
    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in uppercase:", self.input_string.upper())

manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

#Ex.2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print("Area of shape:", shape.area())

square = Square(5)
print("Area of square:", square.area())

#Ex.3
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 6)
print("Area of rectangle:", rectangle.area())

#Ex.4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, ",", self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

point1 = Point(3, 4)
point2 = Point(6, 8)

point1.show()
point2.show()

print(point1.dist(point2))

point1.move()
point1.show()

#Ex.5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} accepted. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

account = BankAccount("John Doe", 1000)
print(f"Account owner: {account.owner}, Balance: ${account.balance}")

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
account.withdraw(-100)

#Ex.6
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)