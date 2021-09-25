from IPython.display import display
import pandas as pd
import numpy as np
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
    'key2' : ['yes', 'no', 'yes', 'yes', 'no'],
    'data1' : np.random.randn(5),
    'data2' : np.random.randn(5)})
display(df)
wlist = ['w','w','y','w','y']
print(df.groupby(wlist).sum())