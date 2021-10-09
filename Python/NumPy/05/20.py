import pandas as pd
import numpy as np

xlsx = "data//data_test.xlsx"
df1 = pd.read_excel(xlsx, "Sheet1")
print(df1)
# 也可以直接利用：
df2 = pd.read_excel("data//data_test.xlsx", "Sheet1")
print("-------------------------------")
print(df2)
