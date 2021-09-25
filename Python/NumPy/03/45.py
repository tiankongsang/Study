import numpy as np

arr = np.arange(5)
print('原数组：', arr)
wy = np.tile(arr, 3)
print('重复数据处理：\n', wy)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print('重复数据处理：\n', arr2.repeat(2, axis=0))
