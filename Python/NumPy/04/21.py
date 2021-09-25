import pandas as pd
import numpy as np

df4 = pd.DataFrame(np.arange(9).reshape(3, 3),
                   index=['a', 'c', 'd'], columns=['one', 'two', 'four'])
print(df4)
