import pandas as pd
obj1 = pd.Series([5.1,-2.6,7.8,10],index = ['a','c','g','f'])
print('obj1:\n',obj1)
obj2 = pd.Series([2.6,-2.8,3.7,-1.9],index = ['a','b','g','h'])
print('obj2:\n',obj2)
print(obj1+obj2)