tup = tuple('bar')
print('输出元组tup:', tup)
nested_tup = (4, 5, 6), (7, 8)
print('输出元组 tup:', nested_tup)
print('元组的连接', tup + tuple('wwy'))
a, b, c = tup
print(a, b, c)
print(tup.count(a))
