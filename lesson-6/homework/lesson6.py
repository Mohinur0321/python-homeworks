#1

txt = input('Enter: ')
cnt = 0
txt2 = []
while len(txt)> cnt:
    txt2.append(txt[cnt])
    
    if cnt ==3:
        next_char = cnt+1
        if next_char < len(txt) and txt[next_char] not in ['a', 'e', 'i', 'o', 'u']:
            txt2.append('_')
        elif next_char + 1< len(txt):
            j = next_char + 1
            while j< len(txt) and txt[j] in ['a', 'e', 'i', 'o', 'u']:
                j += 1
            if j < len(txt):
                txt2.insert (j, '_')
    cnt += 1
if txt2 and txt2[-1] == '_':
    txt2.pop()

print (''. join(txt2)) 

#2

n = int(input('Enter: '))
for i in range(0, n):
    print(i*i)

#3

for i in range(0, 11):
    print(i)

#4

for i in range(1,6):
    for j in range (1, i+1):
        print (j, end= ' ')
    
    print()

#5

nmb = int(input('Enter: '))
smd = 0
for i in range (1, nmb+1):
    smd += i
print(smd)

#6

nmb = int(input('Enter: '))
smd = 0
for i in range (1, 11):
    smd = smd +nmb
    print(smd)

#7

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i in (75, 150, 145):
        print(i)

#8
 
nmb = input('Enter: ')
print(f'Output: {len(list(nmb))} ')

#9

for i in range(5, 0, -1):
    for j in range (i, 0, -1):
        print (j, end= ' ')
    
    print()


#10

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i])

#11

for i in range(-10, 0):
    print(i)

#12

for i in range(0, 5):
    print(i)
print("Done!")

#13

n = int(input("Enter a number: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")

#14
ls = [0, 1]
while len(ls) <= 9
    ls.append(ls[-1]+ ls[-2])

print(ls)

#15

def factorial(number):
    a =1
    for i in range (1, number+1):
        a *= i
    print(f"{number}!= {a}")
factorial(5)

#16
def uncommon(list1, list2):
    result = [x for x in list1 if x not in list2]
    result += [x for x in list2 if x not in list1]

    print(result)

uncommon([1,2,43,5], [1,3,6])





  

  
