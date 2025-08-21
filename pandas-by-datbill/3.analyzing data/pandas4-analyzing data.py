import pandas as pd

df = pd.read_csv('data.csv')

# head() để trả về các dòng dữ liệu theo số dòng tính từ dòng đầu tiên
print(df.head(10))

# nếu như head() không có một con số nhất định thì sẽ trả về 5 dòng đầu tiên
print(df.head())

# tail() dùng đê trả về các dòng dữ liệu theo thứ tự từ dưới lên
print(df.tail())

# infor() dùng để hiện thông tin về cơ sở dự liệu của file
print(df.info())

# Hiển thị thống kê tổng quát (mean, std, min, max,...)
# count	            Số lượng giá trị (không bị thiếu)
# mean	            Giá trị trung bình
# std	            Độ lệch chuẩn (standard deviation)
# min	            Giá trị nhỏ nhất
# 25%, 50%, 75%	    Các phần trăm vị (quartiles: Q1, Q2, Q3)
# max	            Giá trị lớn nhất
print(df.describe())

# để xem số dòng số cột của bảng
print([element for element in df.shape])

print([df.sample(frac=0.1, random_state=42).shape for element in df.shape])

print([df.sample(frac=0.1, random_state=42)])