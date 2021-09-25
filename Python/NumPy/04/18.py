import pandas as pd
obj = pd.Series([7.2,-4.3,4.5,3.6],index = ['b', 'a', 'd', 'c'])
print(obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value = 0))