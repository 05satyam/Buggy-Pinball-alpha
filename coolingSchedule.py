import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import math
from functions import *

rounds=100
s = 12
e = 2
x = np.linspace(0, rounds, rounds)
y = []
val=s
for i in range(0, rounds):
    val = (s-e)*math.exp(-i/(0.1*rounds)) + e
    y.append(val)
    print(y[i])
    
plt.plot(x, y)

plt.show()