import numpy as np
import matplotlib.pyplot as plt
from functions import *
from learningRates import *

xarr=[]#these arrays are for showing the points in the plot
yarr=[]
zarr=[]

A=10
xvals = np.linspace(-5.12, 5.12, 30)
yvals = np.linspace(-5.12, 5.12, 30)

X, Y = np.meshgrid(xvals, yvals)
rastr=np.vectorize(rastrigin)
Z = rastr(X, Y, A)

#plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='Greens', alpha=.65)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

#algorithm
x = -5.12
y = -5.12
z = rastrigin(x, y, A)
ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
print("Initial guess: x =",x," y =",y," z =",z)

xarr.append(x)
yarr.append(y)
zarr.append(z)

i=1
while z>0.0001:
    a = simpleLR(0.01)
    x = x - a*rastrigin_dx(x, y, A)
    y = y - a*rastrigin_dy(x, y, A)
    z = rastrigin(x, y, A)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    print("Iteration ",i,": x =",x," y =",y," z =",z)
    print("Learning rate is ", a)
    
    if i==100: #after a thousand iterations, stop
        break
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    i+=1

ax.plot(xarr, yarr, zarr, color='b')
plt.show()