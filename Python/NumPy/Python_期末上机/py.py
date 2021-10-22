import pandas as pd
import numpy as np
datetime = pd.date_range('20211201', periods = 6)
print('1')
df = pd.DataFrame(data = np.random.randn(6,4),index = datetime,
                  columns = list('ABCD'))
print(df)

print('2')
df = pd.DataFrame(data = np.random.randn(6,4),index = datetime,
                  columns = list('ABCD'))
def f(x):
    if x > 0:
        return '大于0'
    elif x < 0:
        return '小于0'
    else:
        return '等于0'
print(df)
print("*****************************************************************************")
print(df.applymap(f))

print('3')
df3 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
print(df3)

print('4')
print(df.sort_values(by='B'))

print('5')
df5 = df.loc[:,['A']]
print(df5)

print('6')
df = pd.DataFrame(data = np.random.randn(6,4),index = datetime,
                  columns = list('ABCD'))
print(df)
print("*****************************************************************************")
print(df.iloc[[1,2],[2,3]])

print('7')
print(df[df>0])

print('8')
df = pd.DataFrame(data = np.random.randn(6,4),index = datetime,
                  columns = list('ABCD'))
df[df < 0] ='2021'
print(df)