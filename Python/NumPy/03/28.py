import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr)
print('索引结果1：', arr[(0, 1), (1, 3)])
print('索引结果2：', arr[1:2, (0, 2, 3)])
mask = np.array([1, 0, 1], dtype=np.bool_)
print(mask)
# mask是一个布尔数组，它索引第0,2行中第1列元素
print('索引结果3：', arr[mask, 1])
