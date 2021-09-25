import numpy as np

arr1 = np.array([1, 3, 5, 7])
arr2 = np.array([2, 4, 6, 8])
cond = np.array([True, False, True, False])
result = [(x if c else y) for x, y, c in zip(arr1, arr2, cond)]
result
