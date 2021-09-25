import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr)
print(arr[0, 1:3])
print(arr[:, 2])
print(arr[:1, :1])
