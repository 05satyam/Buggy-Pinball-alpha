import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *

x = np.linspace(-512, 512, 1000000)
y=[]
for i in range(0, len(x)):
    
    y.append(-math.sin(math.sqrt(abs(x[i]/2 + 47))) - x[i]*math.sin(math.sqrt(abs(x[i] - 47))))

plt.plot(x, y)
plt.show()