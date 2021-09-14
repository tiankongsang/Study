import numpy as np
arr1 = np.arange(6).reshape(3, 2)
arr2 = arr1*2
arr3 = np.vstack((arr1, arr2))
print(arr3)
