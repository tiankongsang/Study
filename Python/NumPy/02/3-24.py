import numpy as np

arr = np.arange(6).reshape(3, 2)
print(arr)
print(arr.swapaxes(0, 1))
