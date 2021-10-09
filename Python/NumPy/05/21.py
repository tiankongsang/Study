import pandas as pd
import numpy as np

rice = pd.DataFrame({'fruit': ['apple', 'grape', 'orange', 'orange'],
                     'price': [8, 7, 9, 11]})
amount = pd.DataFrame({'fruit': ['apple', 'grape', 'orange'], 'amout': [5, 11, 8]})
display(price, amount, pd.merge(price, amount))
