import pandas as pd
import numpy as np
df4 = pd.DataFrame(np.arange(9).reshape(3,3),
index = ['a','c','d'],columns = ['one','two','four'])
df4.reindex(index = ['a','b','c','d'],columns = ['one','two','three','four'],
fill_value = 100)
print(df4)