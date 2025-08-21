import pandas as pd

data = {
  "calories": [420, 380, 390, 999],
  "duration": [50, 40, 45, 000]
}

#load data into a DataFrame object đọc trực tiếp khi khao báo biến
df = pd.DataFrame(data)
#đọc file theo đuôi 1.csv
df1 = pd.read_csv('store.csv')

print(df)
print(df1)
#đọc file từ đoạn index 0 tới 1
print(pd.DataFrame(data).loc[[0,1]])

#khai báo biến index qua format day i + 1
# index = [i+1 for i in range(len(data["duration"]))]
index = [f"day {i+1}" for i in range(len(data["duration"]))]

print(pd.DataFrame(data, index = index))

# print(range(len(data["calories"])))
# print(len(data["calories"]))

# ------------------------------------------------------------------------------------------------------

# f là viết tắt của "formatted string literal" — còn gọi là f-string.
# Đây là cú pháp mới từ Python 3.6 trở lên, dùng để nhúng biến hoặc biểu thức trực tiếp vào chuỗi.
name = "Đạt"
print(f"Chào bạn {name}!")

x = 5
y = 10
print(f"Tổng của {x} và {y} là {x + y}")