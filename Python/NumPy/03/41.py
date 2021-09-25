import numpy as np

arr = np.array([7, 9, 5, 2, 9, 4, 3, 1, 4, 3])
print('原数组：', arr)
print('排序后：', arr.argsort())
print('显示较大的5个数：', arr[arr.argsort()][-5:])
