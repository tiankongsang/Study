import numpy as np
arr1 = np.arange(6).reshape(3, 2)
arr2 = arr1*2
print('横向合并为:', np.concatenate((arr1, arr2), axis=1))
print('纵向合并为:', np.concatenate((arr1, arr2), axis=0))
