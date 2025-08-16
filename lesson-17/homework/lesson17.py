import pandas as pd
import random as rn

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
df = df.rename(columns = {'First Name': 'first_name', 'Age':'age'})

df.head(3)
df['age'].mean().astype(int)

print(df[['first_name', 'City']])

df['Salary'] = [rn.randint(100, 100000),rn.randint(100, 100000),rn.randint(100, 100000),rn.randint(100, 100000)]

df.describe()
df.describe(include = 'all')


dataframe = {'Month':['Jan', 'Feb', 'Mar', 'Apr'], 'Sales': [5000, 6000, 7500, 8000], 'Expenses': [3000, 3500, 4000, 4500]}

data2 = pd.DataFrame(dataframe)

print('The maximum sale was', data2['Sales'].max())
print('The maximum expense was', data2['Expenses'].max())

print('The minimum sale was', data2['Sales'].min())
print('The minimum expense was', data2['Expenses'].min())


print('The average sale was', data2['Sales'].mean())
print('The average expense was', data2['Expenses'].mean())



a = {'Category':['Rent', 'Utilities', 'Groceries', 'Entertainment'],
                          'January':[1200, 200, 300, 150], 
                          'February':[1300, 220, 320, 160], 
                          'March':[1400, 240, 330, 170], 
                          'April':[1500, 250, 350, 180]}

expenses = pd.DataFrame(a)

expenses = expenses.set_index('Category')


max_expenses = expenses.max(axis=1)
min_expenses = expenses.min(axis = 1)
avg_expenses = expenses.mean(axis = 1)


max_expenses
min_expenses
avg_expenses


