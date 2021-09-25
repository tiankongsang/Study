import pandas as pd

sdata = {"a": 100, "b": 200, "e": 300}
letter = ["a", "b", "c", "e"]
obj = pd.Series(sdata, index=letter)
print(obj)
