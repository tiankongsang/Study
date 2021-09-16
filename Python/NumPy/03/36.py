import numpy as np
a = np.arange(1,13).reshape(3,4)
print(a)
np.save('arr.npy', a)      # np.save("arr", a)
c = np.load( 'arr.npy' )
print(c)