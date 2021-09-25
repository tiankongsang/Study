from IPython.display import display
import numpy as np
import pandas as pd

np.random.seed(971)
values_1 = np.random.randint(10, size=8)
values_2 = np.random.randint(10, size=8)
years = np.arange(2010, 2018)
groups = ['A', 'A', 'B', 'A', 'B', 'C', 'A', 'C']
df = pd.DataFrame({'group': groups, 'year': years, 'value_1': values_1, 'value_2': values_2})
display(df)
print('group的取值为：', df.group.unique())
print('group的取值个数为：', df.group.nunique())
print('value_1的取值及其个数为：\n', df.value_1.value_counts())
