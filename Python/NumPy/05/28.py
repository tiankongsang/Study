import pandas as pd
import numpy as np

data1 = pd.DataFrame(np.arange(6).reshape(2, 3), columns=list('abc'))
data2 = pd.DataFrame(np.arange(20, 26).reshape(2, 3), columns=list('ayz'))
data = pd.concat([data1, data2], axis=0, sort=False)
display(data1, data2, data)
