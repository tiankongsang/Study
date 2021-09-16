import numpy as np
a = np.arange(0,12,0.5).reshape(4,-1)
np.savetxt("a1-out.txt", a)  
#缺省按照'%.18e'格式保存数值
np.loadtxt("a1-out.txt")
np.savetxt("a2-out.txt", a, fmt = "%d", delimiter = ",") 
#改为保存为整数，以逗号分隔
np.loadtxt("a2-out.txt",delimiter = ",") 
# 读入的时候也需要指定逗号分隔