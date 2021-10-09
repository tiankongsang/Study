import pandas as pd
import numpy as np

df1 = pd.read_csv("data//sunspots.csv")
# 读取CSV文件到DataFrame中
print(df1.sample(5))

df2 = pd.read_table("data//sunspots.csv", sep=",")
# 使用read_table，并指定分隔符
print("------------------")
print(df2.sample(5))
df3 = pd.read_csv("data//sunspots.csv", names=["a", "b"])
# 文件不包含表头行，允许自动分配默认列名，也可以指定列名
print("------------------")
print(df3.sample(5))
