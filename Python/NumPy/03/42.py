import numpy as np

a = [1, 5, 7, 2, 3, -2, 4]
b = [9, 5, 2, 0, 6, 8, 7]
ind = np.lexsort((b, a))
print('ind:', ind)
tmp = [(a[i], b[i]) for i in ind]
print('tmp:', tmp)
