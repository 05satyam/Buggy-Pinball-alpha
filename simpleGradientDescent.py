import numpy as np
import matplotlib.pyplot as plt
from functions import *
from learningRates import *

xarr=[]#these arrays are for showing the points in the plot
yarr=[]
zarr=[]

xvals = np.linspace(-2, 2, 30)
yvals = np.linspace(-2, 2, 30)

X, Y = np.meshgrid(xvals, yvals)
mc = np.vectorize(rosenbrock)
Z = mc(X,Y)

#plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.65)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

#algorithm
x = 2
y = -2
z = rosenbrock(x, y)
ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
print("Initial guess: x =",x," y =",y," z =",z)
 
xarr.append(x)
yarr.append(y)
zarr.append(z)
 
i=1
while z>0.00001:
    a = simpleLR(0.0001)
    x = x - a*rosenbrock_dx(x, y)
    y = y - a*rosenbrock_dy(x, y)
    z = rosenbrock(x, y)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    print("Iteration ",i,": x =",x," y =",y," z =",z)
    print("Learning rate is ", a)
      
    if i==1000: #after a thousand iterations, stop
        break
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    i+=1

ax.plot(xarr, yarr, zarr, color='b')
plt.show()