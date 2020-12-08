import numpy as np
import matplotlib.pyplot as plt
from functions import *
from learningRates import *

xarr=[]#these arrays are for showing the points in the plot
yarr=[]
zarr=[]

A=10
xvals = np.linspace(-5.12, 5.12, 100)
yvals = np.linspace(-5.12, 5.12, 100)

X, Y = np.meshgrid(xvals, yvals)
rastr=np.vectorize(rastrigin)
Z = rastr(X, Y, A)

#plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='Greens', alpha=.65)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

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
Dx=0 #difference between last two variable values
Dy=0
gama=0.1
while z>0.0001:
    a = simpleLR(0.005)
    Dx = a*rastrigin_dx(x, y, A) + gama*Dx
    Dy = a*rastrigin_dy(x, y, A) + gama*Dy
    x = x - Dx
    y = y - Dy
    z = rastrigin(x, y, A)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    print("Iteration ",i,": x =",x," y =",y," z =",z)
    
    if i==100: #after a thousand iterations, stop
        break
    
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    i+=1

ax.plot(xarr, yarr, zarr, color='b')
plt.show()