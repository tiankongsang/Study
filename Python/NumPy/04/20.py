import pandas as pd
import numpy as np

obj2 = pd.Series(['blue', 'red', 'black'], index=[0, 2, 4])
print(obj2.reindex(np.arange(6), method='backfill'))
