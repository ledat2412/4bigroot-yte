import pandas as pd

df = pd.read_csv('data1.csv')

print(df.duplicated())

df1 = pd.read_csv('data1.csv')

df1.drop_duplicates(inplace = True)

print(df1.to_string())

