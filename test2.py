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
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.1)
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
    step = -step
    while True:
        x = x+step
        y = y+step
        z = z-abs(step)
        xarr.append(x)
        yarr.append(y)
        zarr.append(z)
        #print("x:",x,"y:",y,"z=",z)
        onfunc=rastrigin(x, y, 10)
        if abs(z-onfunc)<0.0001:
            ax.plot(x, y, rastrigin(x, y, 10), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
            print(rastrigin(x, y, 10))
            break
        elif z<onfunc:
            while abs(z-onfunc)>0.000001:
                step=step/2
                print("step is",step)
                print("z is ", z)
                print("onfunc is",onfunc)
                if z>onfunc:
                    x = x+step
                    y = y+step
                    z = z+step
                else:
                    x = x-step
                    y = y-step
                    z = z-step
                
                onfunc=rastrigin(x, y, 10)
                
            print("point (",x,",",y,",",z,")")
            break
            
ax.plot(xarr, yarr, zarr, color='b')    #connecting the points


plt.show()