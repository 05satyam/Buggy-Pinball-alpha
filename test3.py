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
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.8)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

xarr=[]#these arrays are for showing the points in the plot
yarr=[]
zarr=[]
x=4.5
y=4.5
z = rastrigin(x, y, 10)
step=0.1
for i in range(0, 1):
    Z=2*X+2*Y+z
    ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.8)
            
ax.plot(xarr, yarr, zarr, color='b')    #connecting the points


plt.show()