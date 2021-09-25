import pandas as pd
import numpy as np
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
    'key2' : ['yes', 'no', 'yes', 'yes', 'no'],
    'data1' : np.random.randn(5),
    'data2' : np.random.randn(5)})
groupk1 = df.groupby('key2').mean()
print(groupk1)