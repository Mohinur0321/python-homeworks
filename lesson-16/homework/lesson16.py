import numpy as np
#1
lst = [12.23, 13.32, 100, 36.32]
one_d  = np.array(lst)

print(one_d)
#2
a = np.arange(2, 11).reshape(3, 3)
print(a)


#3
arr = np.zeros(10)
arr[6] = 11 
print(arr)


#4
arr = np.arange(12, 38)
print(arr)


#5
arr = np.array([1, 2, 3, 4])

float_arr = arr.astype(float)

print(float_arr)


#6

F = np.array([0, 12, 45.21, 34, 99.91])

C = (F - 32) * 5/9

print('Values in Fahrenheit degrees:', F)
print('Values in Centigrade degrees:', np.round(C, 2))


#7
append = np.arange(40, 100, 10)
value = np.array([10, 20 , 30])
after = np.append(value, append)

#8
np.random.seed(123)
data = np.random.randn(10)
mean = np.mean(data)
median = np.median(data)
stdev = np.std(data)
print(f"Mean: {mean} \nMedian: {median} \nStandart Deviation: {stdev}")

#9
data = np.random.randn(10, 10)
print(f"Minimum: {data.min()} \nMaximum: {data.max()}") 

#10
data  = np.random.randn(3, 3, 3)
print(data)
