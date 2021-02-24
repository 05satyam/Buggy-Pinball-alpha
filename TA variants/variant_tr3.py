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
A = 10
rounds=70   #time=0.08619, result=0.62112, eStep=.4, rounds=40
            #time=0.17587, result=0.43454, eStep=.4, rounds=70
times=[]    #time=0.21955, result=0.40299, eStep=.4, rounds=85
results=[]  #time=0.23987, result=0.37431, eStep=.3, rounds=95
num_of_iter=1

x = random.uniform(low_x, up_x)
y = random.uniform(low_y, up_y)   
z = rastrigin(x, y, A)

xarr.append(x)
yarr.append(y)
zarr.append(z)
ax.plot(x, y, z, markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)    #plotting the points

def stepChange(i):
    global zStep
    if i==0:
        zStep=zStep-1
    elif i<2:
        zStep=zStep-1+endingStep/1
        
def plotPoint(x, y, z, i):
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
    print("point ",i," (",x,",",y,",",z,") and step ",zStep)

for exp in range(0, num_of_iter):
    zStep = 2
    endingStep = -.4 
    i=0
    start_time=time.time()
    while i<rounds:
        if x>0: #changing direction from positive to negative 
            xStep = random.uniform(-1, 0)
        else:
            xStep = random.uniform(0, 1)
        
        if y>0:
            yStep = random.uniform(-1, 0)
        else:
            yStep = random.uniform(0, 1)
        
        while True:
            x = x + xStep#continue reducing in this direction until crossing the function
            y = y + yStep
            z = z + zStep
            if x<low_x or y<low_y or x>up_x or y>up_y:# hitting a border stops the trajectory
                x = x - xStep
                y = y - yStep
                z = z - zStep
                
                plotPoint(x, y, z, i)
                stepChange(i)
                i=i+1
                break
            onfunc=rastrigin(x, y, A)
                           
            if abs(z-onfunc)<0.000001:# this means z-onfunc==0
                plotPoint(x, y, z, i)  # if the line crosses the function stop          
                stepChange(i)
                i=i+1
                break
            elif z<onfunc:# if the line is underneath the function, find the point crossing
                instep=zStep
                inxtr=xStep
                inytr=yStep
                while abs(z-onfunc)>0.000001 and instep!=0:#jump in the middle of the step until crossing point is detected
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
                    
                    onfunc=rastrigin(x, y, A)
                    if instep==0:#if step gets too small, exit because we have a satisfactory accurate solution
                        z=onfunc
                
                plotPoint(x, y, z, i)
                stepChange(i)
                i=i+1
                break
    print(exp)
    #print("Estimated time",(time.time()-start_time))
    #print("point ",i," (",x,",",y,",",z,") and step ",step)
    ax.plot(xarr, yarr, zarr, color='b')    #connecting the points
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of variant tr3 it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")

plt.show()