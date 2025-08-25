import pandas as pd
import sqlite3 as sql

conn = sql.connect('chinook.db')
lists = pd.read_sql_query("""SELECT * FROM sqlite_master where type = 'table' """, conn)['name'].tolist()

df = {}
for i in lists:
    
    df[i] = pd.read_sql_query(f'SELECT * FROM {i}', conn)

df['invoice_items'].columns

invoice = df['invoices'].groupby('CustomerId').agg(
    total = ('Total', 'sum'),
)

invoice.sort_values('total', ascending = False, inplace = True)
invoice.head(5)

invoice = invoice.merge(df['customers'], how = 'inner', on='CustomerId')


invoice[['CustomerId', 'total', 'FirstName', 'LastName']].nlargest(n = 5, columns = 'total')

merge_invoice = df['invoices'].merge(df['invoice_items'], how = 'inner', on = 'InvoiceId')


album = df['tracks'].groupby('AlbumId').agg(
    count = ('TrackId', 'count')
)


a = merge_invoice.groupby(['CustomerId', 'TrackId']).agg(
    count = ('TrackId', 'count')
)
a


merge_invoice = a.merge(album, how = 'inner', right_on = 'AlbumId', left_on = 'TrackId', suffixes = ['_bought', '_tracks'])

merge_invoice['equal_flag'] = merge_invoice['count_bought'] == merge_invoice['count_tracks']

k = merge_invoice.groupby('equal_flag').agg(
    flag = ('equal_flag', 'count')
).reset_index()

k['total'] = k['flag'].sum()

k['percentage'] = (k['flag']/ k['total']).round(2) * 100

print(f"The percentage of customer who preferred buying track instead of album is {k['percentage'].iloc[0]}% ")
print(f"""The percentage of customer who bought tracks is {k['percentage'].iloc[0]}% and  the percentage of customer who bought album is {k['percentage'].iloc[1]}% """)
