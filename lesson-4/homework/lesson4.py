# 1
my_dict = {'apple': 10, 'banana': 2, 'cherry': 7, 'date': 4}

# Sort by value (ascending)
asc_sorted = sorted(my_dict.items(), key=lambda item: item[1])

# Sort by value (descending)
desc_sorted = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

print("Ascending by value:", asc_sorted)
print("Descending by value:", desc_sorted)

# 2
dict = {0:10, 1:20}
dict.update ({2:30})
print(dict)
# 3

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
concaneted = {**dict1, **dict2, **dict3}
print(concaneted)
# 4

n = int(input('Enter number:'))

squares_dict = {x: x * x for x in range(1, n + 1)}

print(squares_dict)

# 5

n= 15
squared = {x: x*x for x in range (1, n+1)}
print(squared)

# 1
n = input('Enter')
print(set(n))
# 2
a = set(input('Enter:'))
for i in a:
    print(i)
# 3
my_set = {'a', 'v', 'y'}
my_set.add (input('Enter:'))
print(my_set)
# 4

my_set = {'a', 'v', 'y'}
my_set.pop()
print(my_set)
# 5
my_set1 = {'a', 'v', 'y'}
my_set2 = {'g', 'a', 'v'}

my_set1.difference_update(my_set2)

print(my_set1)
