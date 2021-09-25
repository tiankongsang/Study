import pandas as pd

i = ["a", "c", "d", "a"]
v = [2, 4, 5, 7]
t = pd.Series(v, index=i, name="col")
print(t)
