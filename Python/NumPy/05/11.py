import pandas as pd
import numpy as np

data = pd.DataFrame({'k1': ['a', 'b', 'a', 'a', 'c', 'c', 'b', 'a', 'c', 'a', 'b', 'c'], 'k2': ['one',
                                                                                                'two', 'three', 'two',
                                                                                                'one', 'one', 'three',
                                                                                                'one', 'two', 'three',
                                                                                                'one', 'two'],
                     'w': np.random.rand(12), 'y': np.random.randn(12)})
pd.crosstab(data.k1, data.k2, margins=True)
