import pandas as pd
import numpy as np
def judge(x):
    if x>=0:
        return 'a'
    else:
        return 'b'
df = pd.DataFrame(np.random.randn(4,4))
print(df)
print(df[3].groupby(df[3].map(judge)).sum())