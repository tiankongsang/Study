import pandas as pd
import numpy as np

a = np.arange(6).reshape(2, 3)
b = np.arange(4).reshape(2, 2)
df1 = pd.DataFrame(a, columns=['a', 'b', 'e'], index=['A', 'C'])
print('df1:\n', df1)
df2 = pd.DataFrame(b, columns=['a', 'b'], index=['A', 'D'])
print('df2:\n', df2)
print('df1+df2:\n', df1 + df2)
