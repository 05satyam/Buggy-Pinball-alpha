import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import math
from functions import *

rounds=10
s = 12
e = 2
# x = np.linspace(0, rounds, rounds)

val=s
x, y = 2, 2
z=7.5
onfunc=rastrigin(x, y, 10)
print(x, y, z, onfunc)
inZstep=.1
while abs(z-onfunc)>0.000001 and inZstep!=0:
    inZstep = inZstep/2
    if z>onfunc:
        x = x+inZstep
        y = y+inZstep
        z = z+inZstep
    else:
        x = x-inZstep
        y = y-inZstep
        z = z-inZstep
        
    onfunc=rastrigin(x, y, 10)
    print(x, y, z, onfunc, inZstep)
#     val = s - i*(s-e)/rounds  
#     y.append(val)
    
# plt.plot(x, y)
# 
# plt.show()