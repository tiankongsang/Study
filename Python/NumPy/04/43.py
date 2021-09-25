import pandas as pd
import numpy as np
df2 = pd.DataFrame(np.random.randn(3,3),columns = ['a','b','c'],
index = ['app','win','mac'])
print('按列汇总:\n',df2.sum())
print('按行汇总:\n',df2.sum(axis = 1))