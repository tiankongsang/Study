import pandas as pd
val = [2, 4, 5, 6]
idx1 = range(10, 14)
idx2 = "hello the cruel world".split()
s0 = pd.Series(val)
s1 = pd.Series(val, index = idx1)
t = pd.Series(val, index = idx2)
print(s0.index)
print(s1.index)
print(t. index)
print(s0[0])
print(s1[10])#,s1[0]   #wrong
print('default:',t[0],'label:' ,t["hello"])