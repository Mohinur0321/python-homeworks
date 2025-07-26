#1

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return math.pi * 2 * self.radius
    
r = float(input('Enter the radius of circle: '))
circle = Circle(r)

print(f"Area of circle: {circle.area():.2f}")
print(f"Perimeter of circle: {circle.perimeter():.2f}")

#2

from datetime import datetime
class Person:
    def __init__(self, name, country, date_of_birth):
       self.name = name
       self.country = country
       self.date_of_birth = date_of_birth
    def age(self):
        today = datetime.today()
        return today.year - self.date_of_birth
n = input('Enter your name')
c = input('Whee is your citizenship')    
d = int(input('Enter your year of birth:'))
Person = Person(n, c, d)

print(f" You are {Person.age()} years old")

#3


class Calculator:
    def add_numbers(a,b):
        return a + b
    def subtract_numbers(a,b):
        return a - b
    def multiply_numbers(a,b):
        return a * b
    def divide_numbers(a,b):
        return a / b
    
res = Calculator.divide_numbers(99,9)
print(res)

#4

import math

class Shapes:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Square(Shapes):
    def __init__(self, length):
        self.length = length
       
    def area(self):
        return self.length ** 2

    def perimeter(self):
        return 4 * self.length

class Triangle(Shapes):
    def __init__(self, height, side_1, side_2, base):
        self.height = height
        self.side_1 = side_1
        self.side_2 = side_2
        self.base = base

    def area(self):
        return 0.5 * self.height * self.base

    def perimeter(self):
        return self.side_1 + self.side_2 + self.base

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Test the shapes
square = Square(4)
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())

triangle = Triangle(3, 4, 5, 2.5)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())

circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

#5
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if current is None:
            return Node(value)
        if value < current.value:
            current.left = self._insert_recursive(current.left, value)
        elif value > current.value:
            current.right = self._insert_recursive(current.right, value)
        return current

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

# Example usage
tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5))   # Output: True
print(tree.search(12))  # Output: False

#6
class sd_structure:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item}")
    
    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def display(self):
        print('Stack', self.item[::-1])


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Popped:", stack.pop())
stack.display()

print("Top element:", stack.peek())
print("Is stack empty?", stack.is_empty())
print("Stack size:", stack.size())


#7

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f"({self.first} → {self.second})"

    def __eq__(self, other):
        return isinstance(other, Pair) and self.first == other.first and self.second == other.second

class LinkedList:
    def __init__(self):
        self.ls = []
        self.heads = []

    def insert(self):
        head = input("Enter new item: ")
        if not self.ls:
            self.ls.append(Pair(head, None))
        else:
            last = self.ls[-1].second or self.ls[-1].first
            self.ls.append(Pair(last, head))
        self.heads.append(head)

    def display(self):
        for pair in self.ls:
            print(pair)

    def delete(self):
        target = input("Insert an item you would like to delete: ")
        found_index = None
        for i, pair in enumerate(self.ls):
            if pair.second == target:
                found_index = i
                break

        if found_index is not None:
            for i, pair in enumerate(self.ls):
                if pair.first == target:
                    if found_index + 1 < len(self.ls):
                        self.ls[found_index].second = self.ls[i].second
                    else:
                        self.ls[found_index].second = None
                    self.ls.pop(i)
                    break
        else:
            print("There is no item like this to remove.")
ll = linked_list()
ll.insert()
ll.insert()
ll.display()
ll.delete()
ll.display()

#8
class Shopping:
    def __init__(self):
        self.shopping = {}  # Dictionary to store item name and price

    def insert(self, name, price):
        self.shopping[name] = price

    def delete(self, name):
        if name in self.shopping:
            del self.shopping[name]  # Use 'del' to remove item
        else:
            print('There is no item like this')

    def total_price(self):
        return sum(self.shopping.values())  # Use self.shopping, not self.items

# Example usage
cart = Shopping()
cart.insert("Apple", 2.5)
cart.insert("Bread", 1.8)
cart.delete("Apple")
print("Total price:", cart.total_price())  # Should print: 1.8

#9
class sd_structure:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item}")
    
    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def display(self):
        print('Stack', self.item[::-1])


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Popped:", stack.pop())
stack.display()

print("Top element:", stack.peek())
print("Is stack empty?", stack.is_empty())
print("Stack size:", stack.size())

#10

class QDS:
    def __init__(self):
        self.ls = []

    def enqueue(self, name):
        self.ls.append(name)

    def dequeue(self):
        if self.is_empty():
            self.ls.remove[-1]
        else:
            return "Queue is empty"
        
    def is_empty(self):
        return len(self.ls) == 0 
    
q = QDS()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  

#11

class Banking:
    def __init__(self):
        self.a = {}

    def create_account(self, name, account_number):
        self.a[account_number] = {"name" : name, "balance" :0}

    def deposit(self, account_number, amount):
        if account_number in self.a:
            self.a[account_number]["balance"] += amount
        else:
            print('Account is not found')

    def withdraw(self, account_number, amount):
        if amount> self.a[account_number]["balance"]:
            print(f"you don't have enough money to withdraw.")
        else:
            self.a[account_number]["balance"] -= amount

    def check_balance(self, account_number):
        if account_number in self.a:
            return self.a[account_number]["balance"]
        else:
            return "Account not found"


bank = Banking()
bank.create_account("Alice", 101)
bank.deposit(101, 500)
bank.withdraw(101, 200)
print("Balance:", bank.check_balance(101))
