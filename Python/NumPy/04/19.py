import pandas as pd
import numpy as np

obj1 = pd.Series(['blue', 'red', 'black'], index=[0, 2, 4])
print(obj1.reindex(np.arange(6), method='ffill'))
