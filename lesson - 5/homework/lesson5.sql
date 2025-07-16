#1

year = int(input('Enter year:'))
isinstance(year, int)
if year % 4 == 0 and (year % 100 !=0 or (year % 100 == 0 and year % 400 == 0)):
    print('True')
else:
    print('False')

#2

ntgr = int(input('Your number:'))
if ntgr%2 == 1:
    print('Weird')
elif ntgr%2 == 0:
    if 2<=ntgr<=5:
        print('Not weird')
    if 6<ntgr<= 20:
        print('Weird')
    if ntgr> 20:
        print('Not weird')

#3

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a % 2 != 0:
    a += 1  # Make 'a' even if it's odd

if a <= b:
    print(list(range(a, b + 1, 2)))

