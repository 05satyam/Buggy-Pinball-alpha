import numpy as np
import matplotlib.pyplot as plt
from functions import *
from learningRates import *

xarr=[]#these arrays are for showing the points in the plot
yarr=[]
zarr=[]

xvals = np.linspace(-10, 10, 30)
yvals = np.linspace(-10, 10, 30)

X, Y = np.meshgrid(xvals, yvals)
Z = booth(X, Y)

#plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='Greens', alpha=.65)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#algorithm
x = -10
y = -10
z = booth(x, y)
ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
print("Initial guess: x =",x," y =",y," z =",z)

xarr.append(x)
yarr.append(y)
zarr.append(z)

i=1
e=1e-6 #standard value to avoid dividing with 0
Gx=0 #the matrix from the derirative
Gy=0
gama=0.9
arr1=[]
arr2=[]

while z>0.0001:
    a = periodicalLR(0.1, i, 10, 1)
    Gx = gama*Gx + (1-gama)*booth_dx(x, y)**2
    Gy = gama*Gy + (1-gama)*booth_dy(x, y)**2
    x = x - a*booth_dx(x, y)/(np.sqrt(Gy)+e)
    y = y - a*booth_dy(x, y)/(np.sqrt(Gy)+e)
    z = booth(x, y)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    print("Iteration ",i,": x =",x," y =",y," z =",z)
    print("Learning rate is ", a)
    
    if i==1000: #after a thousand iterations, stop
        break
    arr1.append(a)
    arr2.append(i)
    
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    i+=1

ax.plot(xarr, yarr, zarr, color='b')
plt.show()
plt.plot(arr2, arr1)
plt.show()