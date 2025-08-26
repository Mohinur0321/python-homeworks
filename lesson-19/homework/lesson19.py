import sqlite3 as sql
import pandas as pd
# pip install openpyxl
data = pd.read_csv('sales_data.csv')

data.sort_values(by = ['Quantity'], ascending = False, inplace= True)

dg = data.groupby('Category')

gr_cat = dg.agg(total = ('Quantity', 'sum'), average = ('Price', 'mean'), max = ('Quantity', 'max'))

k = data.groupby(['Category', 'Product'])

prod_sales = k.agg(total = ('Quantity', 'sum')).sort_values(['Category', 'total'], ascending = False)

top_sellers = prod_sales.groupby("Category")["total"].idxmax()
result = prod_sales.loc[top_sellers].reset_index()

result
# top_sellers = (
#     dg.groupby(["Category", "Product"])["Quantity"].sum()
#       .reset_index()
#       .sort_values(["Category", "Quantity"], ascending=[True, False])
#       .drop_duplicates("Category")
# )

data['sales'] = data['Price'] * data['Quantity']

daily = data.groupby('Date')['sales'].sum()

print(daily.nlargest(n=1))

orders = pd.read_csv('customer_orders.csv')

grouped = orders.groupby('CustomerID').size()

filter = grouped[grouped >= 20]

df = orders[orders['CustomerID'].isin(filter)]

print(df)

prd =(
    orders.groupby('Product').
      agg(average = ('Price', 'mean'))
)

prd = prd[prd['average'] >= 120]



prd = prd.reset_index()
orders = orders.reset_index()


orders = orders[orders['Product'].isin(prd['Product'])]

print(orders)

a = (orders.groupby('Product').agg(
    total_quant = ('Quantity', 'sum'),
    total_price = ('Price', 'sum')
)
     
     
)



fltr = a['total_quant'] >=5

a = a[fltr]
print(a)

conn = sql.connect('population.db')

population = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table';", conn)

df = pd.read_sql("SELECT * FROm population", conn)
df2 = pd.read_sql("select * from sqlite_sequence", conn)

conn.close()

excel = pd.read_excel('population_salary_analysis.xlsx')
excel
df

def category(salary):
    if salary <= 200000:
        return 'till $200,000'
    elif salary <= 400000:
        return '$200,001 - $400,000'
    elif salary <= 600000:
        return '$400,001 - $600,000'
    elif salary <= 800000:
        return '$600,001 - $800,000'
    elif salary <= 1000000:
        return '$800,001 - $1,000,000'
    elif salary <= 1200000:
        return '$1,000,001 - $1,200,000'
    elif salary <= 1400000:
        return '$1,200,001 - $1,400,000'
    elif salary <= 1600000:
        return '$1,400,001 - $1,600,000'
    elif salary <= 1800000:
        return '$1,600,001 - $1,800,000'
    else:
        return '$1,800,001 and over'
    
df['category'] = df['salary'].apply(category)

cat_count = df.groupby('category').agg(
    average = ('salary', 'mean'),
    median = ('salary', 'median'),
    count = ('category', 'count')
)
    
cat_count['sum'] = cat_count['count'].sum()


cat_count['percentage'] = (cat_count['count'] / cat_count['sum']).round(4) * 100


df


state_count  = df.groupby(['state']).agg(
    average = ('salary', 'mean'),
    median = ('salary', 'median'),
    population = ('id', 'count')
)

state_count['percentage'] =(state_count['population']/ state_count['population'].sum()).round(4) * 100
state_count

