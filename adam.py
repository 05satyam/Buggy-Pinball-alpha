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
e=1e-6 #standard value to avoid dividing with 0
Gx=0 #the matrix of the derirative
Gy=0
gama1=0.9
gama2=0.999
while z>0.0001:
    a = simpleLR(0.05)
    Dx = gama1*Dx + (1-gama1)*rastrigin_dx(x, y, A)
    Dy = gama1*Dy + (1-gama1)*rastrigin_dy(x, y, A)
    Gx = gama2*Gx + (1-gama2)*rastrigin_dx(x, y, A)**2
    Gy = gama2*Gy + (1-gama2)*rastrigin_dy(x, y, A)**2
    x = x - a*Dx/(np.sqrt(Gx)+e)
    y = y - a*Dy/(np.sqrt(Gy)+e)
    z = rastrigin(x, y, A)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    print("Iteration ",i,": x =",x," y =",y," z =",z)
    
    if i==1000: #after a thousand iterations, stop
        break
    
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    i+=1

ax.plot(xarr, yarr, zarr, color='b')
plt.show()