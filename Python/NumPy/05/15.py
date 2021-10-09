import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), index=
{'one', 'two', 'three'}, columns=['I1', 'I2', 'I3'])
df.plot(kind='barh')
