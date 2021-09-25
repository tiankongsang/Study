import numpy as np

arr = np.array([[4, 2, 9, 5], [6, 4, 8, 3], [1, 6, 2, 4]])
print('原数组：\n', arr)
arr.sort(axis=1)
print('横向排序后：\n', arr)
