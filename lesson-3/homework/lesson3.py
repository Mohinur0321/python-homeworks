#1
my_list = ['banana', 'apple', 'strawberry', 'orange', 'raspberry']
print(my_list[2])
#2
s1 = [23, 65, 31, 99]
s2 = [54, 976, 20]
s3 = s1+s2
print(s3)
#3
my_list = [14,2,3,1,43,5,95,4,10]
print(my_list[0], my_list[(len(my_list)//2)], my_list[-1])
#4
my_list = [2524, 9965, 986, 569, 2085]
tup = tuple(my_list)
print(tup, type(tup))
#5
cities = ['London', 'France', 'Spain']
print('Paris' in cities)
#6
my_list = [1,4,7,2,16]
my_list_2 = my_list[:]
print(my_list_2)
#7
numbers = [3,7,41,9,441]
numbers[0] = numbers [-1]
numbers[-1] = numbers[0]
print(numbers)
#8
my_tuple = (1,2,3,4,5,6,7,8,9,10)
print(my_tuple[3:7])
#9
colors = ['yellow', 'green', 'red', 'blue', 'blue', 'blue']
cnt = colors.count('blue')
print(cnt)
#10
animals = ['tiger', 'elephant', 'your_classmate', 'lion']
print(animals.index('lion'))
#11
tup_1 = (1,2,3,4,5)
tup_2 = (6,7,8,9,10)
print(tup_1+tup_2)
#12
list_1 = [3,6,8,8,72,7,27]
tuple_1 = [2,7,0,6,4,3,5,8,13]
print(len(list_1), len(tuple_1))
#13
tup = (2,6,8,9,17,7)
lst = list(tup)
print(lst, type(lst))
#14
tup = (2,4,8,-1,6,0,26,7,4)
print(max(tup), min(tup))
#15
tup = ('alsfksaljf', 'alsdfls', 'ssls', 'kfskfksf')
rvrsd = tup[::-1]
print(rvrsd)
