import pandas as pd
import numpy as np

df2 = pd.DataFrame(np.random.randn(3, 3), columns=['a', 'b', 'c'],
                   index=['app', 'win', 'mac'])
print(df2)
print(df2.applymap(lambda x: '%.3f' % x))
