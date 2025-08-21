import pandas as pd

df = pd.read_csv('data1.csv')
df1 = pd.read_csv('data1.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

df1.dropna(subset=['Date'], inplace = True)
print(df1.to_string())
print(df.to_string())