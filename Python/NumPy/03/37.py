import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
print(c)
np.savez('result.npz', a, b, sin_array=c)
r = np.load('result.npz')
r['arr_0']
