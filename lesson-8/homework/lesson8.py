try:
    result = 10/0
except ZeroDivisionError:
    print('You cannot divide by zero')

try:
    nmb = input('Enter the number')
    nmb1 = int(nmb)
except ValueError:
    print('You should input a number')

try:
    with open("myfile.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

try:
    nmb = input('Enter')
    nmb1 = input('Enter')
    if not nmb.isdigit() or not nmb1.isdigit():
        raise TypeError('Input should be number')
    result = int(nmb) + int(nmb1)
except TypeError:
    print('Its not number')

try:
    with open("myfile.txt", 'r') as file:
        content = file.read()
        print(content)
except PermissionError:
    print('You dont have a permission')

try:
    my_lst = [2,5,8,5,3,8]
    print(my_lst[9])
except IndexError:
    print('You are out of index')

try:
    while 5>3:
        print('Go on')
except KeyboardInterrupt:
    print("\n You stopped it manually")

import math
try:
    resut = math.exp(10000)
except ArithmeticError:
    print('There is an Arithmetic Error')

byte_data = b'\xff\xfeH\x00i\x00' 

try:
    text = byte_data.decode('ascii')
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)

class Dog:
    def bark (self):
        print('Woof')
dog = Dog()
try:
    dog.bark()
    dog.meow()
except AttributeError:
    print ("There is no 'meow' attribute")

with  open("lw4.ipynb", "r") as file:
    content = file.read
    print(content)


file = open("lw4.ipynb", "r")
n = int(input())
for i in range(n):
    print(file.readline().strip())

file.close


with open("lw4.ipynb", 'a') as file_handler:
    file_handler.write('Here is more text')
    print(file_handler.read)

file = open("lw4.ipynb", 'r')
n = int(input())
for i in range(-n):
    print(file.readlines().strip())

file.close


ls = []
with open("lw4.ipynb") as file:
    for i in file:
        ls.append(i)
        print(i)


with open("lw4.ipynb") as file:
    content = file.read()
    for i in file:
        print(i)


lines = []

with open("example.txt", "r") as file:  # Replace with your file name
    for line in file:
        lines.append(line.strip())  # strip() removes the newline character

print(lines)



longest = ""

with open("lw4.ipynb") as file:
    for line in file:
        name = line.strip()
        if len(name) > len(longest):
            longest = name

print("Longest name:", longest)



with open('lw4.ipynb') as file:
    nmb = sum(1 for i in file)
print(nmb)


from collections import Counter
import re

with open('RAR.TXT.txt', 'r') as file:
    text = file.read().lower()

words = re.findall(r'\b\w+\b', text)
word_counts = Counter(words)

for word, count in word_counts.items():
    print(f"{word}: {count}")


import os

os.path.getsize("RAR.TXT.txt")

lines = ['alfsj', 'alsfasljdf', 'alkdf']
file1 = open('RAR.TXT.txt', 'w+')
file1.writelines(lines)
file1.close()

print('file written successfully')


file1 = open('lw4.ipynb', 'r')

file2 = open('RAR.TXT.txt', 'w')
file2.writelines(file1)
file2.close()

print('file written successfully')


file1 = open('lw4.ipynb', 'r')
file2 = open('RAR.TXT.txt', 'r')

for line1, line2 in zip(file1, file2):
    print(line1.strip() + ' ' + line2.strip())

file1.close()
file2.close()

import random
with open('RAR.TXT.txt', 'r') as file1:
    lines = file1.readlines()
    line_cnt = len(lines)

    line = random.randint(0, line_cnt-1)
    print(lines[line])


def is_closed(file):
    if file.closed:
        print('the file is closed')
    else:
        print('the file is not closed')

f = open('RAR.TXT.txt', 'r')


is_closed(f)



with open('RAR.TXT.txt', 'r') as file1:
    for line in f:
        print(line.strip(), end ='')


def word_cnt(file):
    with open(file, 'r') as file1:
        c = 0
        text = file1.read()
        w = text.split()
        c += len(w)
    print(c)

word_cnt('RAR.TXT.txt')


with open('RAR.TXT.txt', 'r') as file1:
    content = file1.read()
    ls = []
    for i in content:
        ls.append(i)
        print(i)



import string
unique = set(string.ascii_letters.upper())
for i in sorted(unique):
    print( i + '.txt')




def wrt_lines(filename, per_line):
    from string import ascii_lowercase
    with open(filename, 'w') as f:
        for i in range(0, len(ascii_lowercase)+1, per_line):
            line = ascii_lowercase[i:i+per_line]
            f.write(line + '\n')
             

wrt_lines('RAR.TXT.txt', 4)







