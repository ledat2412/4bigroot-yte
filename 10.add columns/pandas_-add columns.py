import pandas as pd

employees = pd.read_csv('employees.csv')

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*3
    return employees

# Gọi hàm và lưu kết quả
result = createBonusColumn(employees)

# In ra kết quả
print(result)