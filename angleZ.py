import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import math
from functions import *

xvals = np.linspace(-5.12, 5.12, 300)
yvals = np.linspace(-5.12, 5.12, 300)

X, Y = np.meshgrid(xvals, yvals)
mc = np.vectorize(rastrigin)
Z = mc(X,Y, 10)

#plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.8)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

angles = np.linspace(45, 45, 3)
i=0
z_we_want = 0.1
for a in angles:
    xarr=[]#these arrays are for showing the points in the plot
    yarr=[]
    zarr=[]
    
    x=random.uniform(-1, 1)
    y=random.uniform(-1, 1)
    if a>0:
        z = math.sqrt((-(x**2)*(math.sin(math.radians(a))**2) - (y**2)*(math.sin(math.radians(a))**2))/((math.sin(math.radians(a))**2) - 1))
    else:
        z = -math.sqrt((-(x**2)*(math.sin(math.radians(a))**2) - (y**2)*(math.sin(math.radians(a))**2))/((math.sin(math.radians(a))**2) - 1))
    
    f = z_we_want/z
    print(" initial vector (",x,",",y,",",z,") and angle",a)
    x=f*x
    y=f*y
    z=f*z
    print("vector (",x,",",y,",",z,") and angle",a)
    
    xarr.append(0)
    yarr.append(0)
    zarr.append(0)
    
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    
    if i==0:
        ax.plot(xarr, yarr, zarr, color='b')    #connecting the points
    elif i==1:
        ax.plot(xarr, yarr, zarr, color='g')    #connecting the points
    else:
        ax.plot(xarr, yarr, zarr, color='r')    #connecting the points
    i+=1
plt.show()