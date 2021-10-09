import pandas as pd
import numpy as np

data = pd.read_excel('data//testdata.xls')
data.groupby('性别')['血小板计数'].agg(np.mean)
