import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *
from _ctypes import sizeof
import time

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

low_x=-5.12
up_x=5.12
low_y=-5.12
up_y=5.12

step=-3
endingStep = .7
rounds=50

x = random.uniform(low_x, up_x)
y = random.uniform(low_y, up_y)   
z = rastrigin(x, y, 10)

xarr.append(x)
yarr.append(y)
zarr.append(z)
ax.plot(x, y, z, markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)    #plotting the points

def stepChange(i):
    global step
    if i==0:
        step=step+2
    elif i<2:
        step=step+(1+endingStep/1)
        
def plotPoint(x, y, z, i):
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
    print("point ",i," (",x,",",y,",",z,") and step ",step)
        
i=0
start_time=time.time()
while i<rounds:
    if x>0:
        xtr = random.uniform(0.15*low_x, 0)
    else:
        xtr = random.uniform(0, 0.15*up_x)
    
    if y>0:
        ytr = random.uniform(0.15*low_y, 0)
    else:
        ytr = random.uniform(0, 0.15*up_y)
#     xtr = random.uniform(0.15*low_x, 0.15*up_x)#changing direction
#     ytr = random.uniform(0.15*low_y, 0.15*up_y)
    
    while True:
        x = x + xtr#continue reducing in this direction until crossing the function
        y = y + ytr
        z = z-step
        if x<low_x or y<low_y or x>up_x or y>up_y:
            x = x - xtr
            y = y - ytr
            z = z + step
            
            #plotPoint(x, y, z, i)
            stepChange(i)
            i=i+1
            break
        onfunc=rastrigin(x, y, 10)
                       
        if abs(z-onfunc)<0.000001:
            #plotPoint(x, y, z, i)            
            stepChange(i)
            i=i+1
            break
        elif z<onfunc:
            instep=step
            inxtr=xtr
            inytr=ytr
            while abs(z-onfunc)>0.000001 and instep!=0:
                instep=instep/2
                inxtr=inxtr/2
                inytr=inytr/2
                if z>onfunc:
                    x = x+inxtr
                    y = y+inytr
                    z = z+instep
                else:
                    x = x-inxtr
                    y = y-inytr
                    z = z-instep
                
                onfunc=rastrigin(x, y, 10)
                if instep==0:
                    z=onfunc
            
            #plotPoint(x, y, z, i)
            stepChange(i)
            i=i+1
            break

print("Estimated time",(time.time()-start_time))
print("point ",i," (",x,",",y,",",z,") and step ",step)
ax.plot(xarr, yarr, zarr, color='b')    #connecting the points

#plt.show()