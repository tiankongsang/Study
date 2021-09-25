import numpy as np

a = np.arange(0, 12, 0.5).reshape(4, -1)
np.savetxt("a1-out.txt", a)
np.loadtxt("a1-out.txt")
np.savetxt("a2-out.txt", a, fmt="%d", delimiter=",")
np.loadtxt("a2-out.txt", delimiter=",")
