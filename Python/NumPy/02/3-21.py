import numpy as np
arr = np.arange(16).reshape(4, 4)
print('横向分割为:\n', np.hsplit(arr, 2))
print('纵向分割为:\n', np.vsplit(arr, 2))
