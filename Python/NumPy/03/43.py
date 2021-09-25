import numpy as np

names = np.array(['红色', '蓝色', '蓝色', '白色', '红色', '红色'])
print('原数组：', names)
print('去重后的数组:', np.unique(names))
print('数据出现次数:', np.unique(names, return_counts=True))
