import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.normal(size = (6,5)),index = ['a','b','c','A','B','c'])
print("数据为:\n",df)
wdict = {'a':'one','A':'one','b':'two','B':'two','c':'three'}
print("分组汇总后的结果为:\n",df.groupby(wdict).sum())