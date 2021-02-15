import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *
from mpl_toolkits.axes_grid1.axes_size import AxesX
from numpy.core.setup_common import sym2def
from PIL.PcfFontFile import sz

times=[]
results=[]

A = 10      # rastrigin factor
rounds = 3500
low_x=-5.12
up_x=5.12
low_y=-5.12
up_y=5.12
num_of_iter=1
step=0.1

xarr=[]#these arrays are for showing the points in the plot
yarr=[]
zarr=[]
xvals = np.linspace(-5.12, 5.12, 300)
yvals = np.linspace(-5.12, 5.12, 300)
    
X, Y = np.meshgrid(xvals, yvals)
mc = np.vectorize(rastrigin)
Z = mc(X,Y, 10)
    
    #plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.3)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

def find_t_in_rastrigin(sx, sy, sz, a, b, c):
    return 0

def line_intersection(sx, sy, sz, ex, ey, ez):
    a = ex - sx
    b = ey - sy
    c = ez - sz
    #points = find_t_in_rastrigin(sx, sy, sz, a, b, c)
    T = np.linspace(0.1, 10, 300)
    xmem=[]
    for t in T:
        for i in range(0, 100): #Newton-Raphson method
            f = (a**2 + b**2)*(t**2) + (2*sx*a + 2*sy*b - c)*t - A*math.cos(2*math.pi*(sx+a*t)) - A*math.cos(2*math.pi*(sy+b*t)) + 2*A + sx**2 + sy**2 - sz 
            df = 2*(a**2 + b**2)*t + 2*sx*a + 2*sy*b - c + 2*A*math.pi*a*math.sin(2*math.pi*(sx+a*t)) + 2*A*math.pi*b*math.sin(2*math.pi*(sy+b*t))
            t = t - (f/df)
            
        x = sx + a*t
        y = sy + b*t
        z = sz + c*t
        if abs(z)-abs(rastrigin(x, y, A))<0.001 and x>low_x and x<up_x and y>low_y and y<up_y and (round(x, 4) not in xmem):
            ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
            print("point (",x,",",y,",",z,")")
            xmem.append(round(x, 4))
    #TBD which point is closer to starting point
    
    return 0

for exp in range(0, num_of_iter):
    start_time=time.time()
    #x = random.uniform(low_x, up_x)
    #y = random.uniform(low_y, up_y)
    
    #TBD how to find local max
    
    #TBD how many trajectories will be sent out and their direction
    
    for i in range(0, 1): #TBD when and how to finish the descent
        #starting point of trajectory
        startline_x = 4.5
        startline_y = 4.5
        startline_z=rastrigin(startline_x, startline_y, A)
        
        xarr.append(startline_x)
        yarr.append(startline_y)
        zarr.append(startline_z)
        
        #the point where the trajectory will hit a border
        endline_x = low_x   
        endline_y = low_y   #TBD
        endline_z = 79
        
        xarr.append(endline_x)
        yarr.append(endline_y)
        zarr.append(endline_z)
        
        point = line_intersection(startline_x, startline_y, startline_z, endline_x, endline_y, endline_z)
        
        ax.plot(xarr, yarr, zarr, color='b')    #connecting the points
        plt.show()
       
        #code TBD for getting the first point crossing 
        
        #code TBD for reversing trajectory
        
    #print(exp)
    
    #results.append(z)
    total_time=time.time()-start_time
    times.append(total_time)

#results_average=sum(results)/len(results)
#time_average=sum(times)/len(times)
#print("After",num_of_iter,"iterations of TA variant, it is found that it takes",time_average,"seconds and has a distance of",results_average, "from the global minimum")