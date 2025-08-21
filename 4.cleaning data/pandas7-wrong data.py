import pandas as pd

df = pd.read_csv('data1.csv')

df.loc[7,'Duration'] = 45

print(df.to_string())

df1 = pd.read_csv('data1.csv')

for x in df1.index:
  if df1.loc[x, "Duration"] > 120:
    df1.loc[x, "Duration"] = 120

print(df1.to_string())

df2 = pd.read_csv('data1.csv')

for x in df2.index:
  if df2.loc[x, "Duration"] > 120:
    df2.drop(x, inplace = True)

#remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy

print(df2.to_string())