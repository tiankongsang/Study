import pandas as pd
import numpy as np

display(pd.merge(price, amount, left_on='fruit', right_on='fruit'))
