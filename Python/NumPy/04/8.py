import pandas as pd

obj = pd.Series([4, 7, -3, 2])
print("修改前：\n", obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print("修改后：\n", obj)
