import pandas as pd
import numpy as np

left = pd.DataFrame({'key1': ['one', 'one', 'two'], 'key2': ['a', 'b', 'a'], 'value1': range(3)})
right = pd.DataFrame({'key1': ['one', 'one', 'two', 'two'], 'key2': ['a', 'a', 'a', 'b'], 'value2': range(4)})
display(left, right, pd.merge(left, right, on=['key1', 'key2'], how='left'))
