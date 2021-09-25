import pandas as pd
wy = pd.Series([1,-2,4,-4],index = ['c','b','a','d'])
print('值排序后的Series:\n',wy.sort_values())