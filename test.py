import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *

xvals = np.linspace(-5.12, 5.12, 300)
yvals = np.linspace(-5.12, 5.12, 300)

X, Y = np.meshgrid(xvals, yvals)
mc = np.vectorize(rastrigin)
Z = mc(X,Y, 10)

#plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.35)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

xarr=[]#these arrays are for showing the points in the plot
yarr=[]
zarr=[]

for i in range(0, 2):
    x = random.uniform(-5, 5) # initial solutions
    y = random.uniform(-5, 5)
    z = rastrigin(x, y, 10)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    
ax.plot(xarr, yarr, zarr, color='b')
plt.show()