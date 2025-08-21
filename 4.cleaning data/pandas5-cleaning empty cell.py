# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# # dropna() để xoá những dòng trong đó có cell trống
# new_df = df.dropna()
#
# print(new_df.to_string())
#
# df.dropna(inplace = True)
#
# print(df.to_string())
#
# df.fillna(130, inplace = True)
#
# print(df.to_string())
#
import pandas as pd

df = pd.read_csv('data.csv')

# Bước 1: In dữ liệu gốc
print("🔹 Dữ liệu gốc:")
print(df.to_string())
input("\nNhấn Enter để tiếp tục tới bước dropna()...\n")

# Bước 2: Dùng dropna() (tạo new_df)
new_df = df.dropna()
print("🔹 Dữ liệu sau df.dropna() (new_df):")
print(new_df.to_string())
input("\nNhấn Enter để tiếp tục tới bước dropna(inplace=True)...\n")

# Bước 3: dropna inplace
df.dropna(inplace=True)
print("🔹 Dữ liệu sau df.dropna(inplace=True):")
print(df.to_string())
input("\nNhấn Enter để tiếp tục tới bước fillna()...\n")

# Bước 4: fillna
df.fillna(130, inplace=True)
print("🔹 Dữ liệu sau df.fillna(130):")
print(df.to_string())

