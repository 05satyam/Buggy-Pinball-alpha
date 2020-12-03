import numpy as np
import matplotlib.pyplot as plt
from math import gamma

#sphere function
# def f(x, y):
#     return x ** 2 + y ** 2
# 
# def fxder(x, y):
#     return 2*x
# 
# def fyder(x, y):
#     return 2*y

#booth function
def f(x, y):
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def fxder(x, y):
    return 10*x + 8*y - 34

def fyder(x, y):
    return 10*y + 8*x - 38

#xvals = np.linspace(-6, 6, 30)
#yvals = np.linspace(-6, 6, 30)
xvals = np.linspace(-10, 10, 30)
yvals = np.linspace(-10, 10, 30)

X, Y = np.meshgrid(xvals, yvals)
Z = f(X, Y)

#plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='Greens', alpha=.65)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#algorithm
x = 6
y = 6
z = f(x, y)
ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
print("Initial guess: x =",x," y =",y," z =",z)

a=0.2 #learning rate
gama=0.85
i=0
e=1e-9
Gx=0
Gy=0
xarr=[]
yarr=[]
zarr=[]
xarr.append(x)
yarr.append(y)
zarr.append(z)
while z>0.0001:
    Gx = gama*Gx + (1-gama)*fxder(x, y)**2
    Gy = gama*Gy + (1-gama)*fyder(x, y)**2
    xnew = x - a*fxder(x, y)/np.sqrt(Gx+e)
    xarr.append(xnew)
    ynew = y - a*fyder(x, y)/(np.sqrt(Gy)+e)
    yarr.append(ynew)
    znew=f(xnew, ynew)
    zarr.append(znew)
    ax.plot(xnew, ynew, znew, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    print("Iteration ",i,": x =",xnew," y =",ynew," z =",znew)
    if i==1000: #after a thousand iterations, stop
        break
    x=xnew
    y=ynew
    z=znew
    i+=1

ax.plot(xarr, yarr, zarr, color='b')
plt.show()