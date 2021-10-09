import pandas as pd
import numpy as np

data = pd.read_excel('data//testdata.xls')
data.agg({'淋巴细胞计数': np.mean, '血小板计数': [np.mean, np.std]})
