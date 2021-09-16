import numpy as np
arr = np.arange(12).reshape(3,4)
print(arr)
print(arr[0,1:3])  #索引第0行中第1列到第2列的元素
print(arr[:,2])   #索引第2列元素
print(arr[:1,:1])  #第0行第0列元素