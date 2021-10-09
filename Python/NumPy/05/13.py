import pandas as pd
import numpy as np

df = pd.DataFrame({'normal': np.random.normal(size=50), 'gamma': np.
                  random.gamma(1, size=50)})
df.plot()
