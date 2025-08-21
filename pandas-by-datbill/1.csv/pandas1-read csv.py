import pandas as pd

df = pd.read_csv('data.csv')

# dòng to_string() dùng để in ra hết các dữ liệu có trong file mà không bị giới hạn
print(df.to_string())

# dùng để tăng giới hạng trần hiển thị số dòng số cột
pd.options.display.max_rows = 9999
print(pd.options.display.max_rows)