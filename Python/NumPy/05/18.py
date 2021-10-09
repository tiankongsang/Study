import pandas as pd
import numpy as np

wd = pd.DataFrame(np.arange(10), columns=['A'])
wd['B'] = 2 * wd['A'] + 4
wd.plot(kind='scatter', x='A', y='B')
