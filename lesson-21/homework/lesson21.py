#Task 1
import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
#1
df1.set_index('Student_ID', inplace = True)
df1['average'] = df1.mean(axis = 1)
#2
top_id = df1["average"].idxmax()  
top_row = df1.loc[top_id]           

print("Top student ID:", top_id)
print(top_row)
#3
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis = 1)
#4
s_m = df1[['Math', 'English', 'Science']].mean()

s_m.plot(kind = 'bar')
#Task 2
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
df2


df2.set_index('Date', inplace = True)
#1
print(df2.sum())

df2['Total'] = df2.sum(axis = 1)
#2
time = df2['Total'].idxmax()
top = df2.loc[time]

print(f'{time}\n {top}')

#3
df2['Change_A'] = df2['Product_A'].pct_change().round(4) * 100
df2['Change_B'] = df2['Product_B'].pct_change() * 100
df2['Change_C'] = df2['Product_C'].pct_change() * 100
 #4
df2[['Change_A', 'Change_B', 'Change_C']].plot(kind = 'line')

#Task 3
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3).set_index('Employee_ID')

df3
#1
k = df3.groupby('Department').agg(
    average = ('Salary', 'mean')
)
print(k)

#2
top = df3['Experience (Years)'].idxmax()
most = df3.loc[top]
print(f'ID is {top}\n {most}')

#3
df3.sort_values('Salary', inplace = True)

df3['Salary Increase'] = df3['Salary'].pct_change().round(4) * 100

#4

dept_count = df3['Department'].value_counts()

plt.bar(dept_count.index, dept_count.values)
plt.show()

#Task 4

import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4).set_index('Order_ID')

df4

#1
total = df4['Total_Price'].sum()
print(total)

#2
j = df4.groupby('Product').agg(
    ordered = ('Quantity', 'sum'),
    average = ('Quantity', 'mean')
)
top = j['ordered'].idxmax()
print(f'The most ordered product is {top}')
#3
print(f'The average quantity ordered per product id {j['average']}')

#4
prod_count = j['ordered']

plt.pie(prod_count.values, labels = prod_count.index)
plt.show()
