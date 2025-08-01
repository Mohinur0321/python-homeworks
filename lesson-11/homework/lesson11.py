import math

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def reverse(s):
    return s[::-1]

def count_vowels(s):
    s = s.lower()
    vowels = 'aeiou'
    v = 0

    for char in s:
        if char in vowels:
            v +=1
    return v

print(count_vowels('prin'))

def calculate_area(radius):
    return math.pi * radius **2

def caluculate_circumference(radius):
    return math.pi * radius *2

def read_file(file_path):
    try:    
        with open('file_path', 'r') as file:
            return file.read
    except FileNotFoundError:
        print('File is not found')


def write_into_file(file_path, content):
    try:    
        with open('file_path', 'w') as file:
            return file.write(content)
    except FileNotFoundError:
        print('File is not found')
