import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *

xvals = np.linspace(2.7, 3.5, 300)
yvals = []

xarr=[]#these arrays are for showing the points in the plot
yarr=[]

for i in range(0, 300):
    yvals.append(2 + xvals[i]**2 - 2*math.cos(2*math.pi*xvals[i]))
#     xarr.append(x)
#     yarr.append(y)
plt.plot(xvals, yvals)    #plotting the points
xarr.append(2.8)
yarr.append(13.3)

xarr.append(3.4)
yarr.append(13.1)

plt.plot(xarr, yarr, color='g')    #connecting the points

plt.plot(3.2, 13.17, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
plt.plot(3.2, 2 + 3.2**2 - 2*math.cos(2*math.pi*3.2), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points

plt.plot(3.4, 13.1, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
plt.plot(3.4, 2 + 3.4**2 - 2*math.cos(2*math.pi*3.4), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
plt.show()

plt.plot(xvals, yvals)    #plotting the points
plt.plot(xarr, yarr, color='g')    #connecting the points

plt.plot(3.2, 13.17, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
plt.plot(3.2, 2 + 3.2**2 - 2*math.cos(2*math.pi*3.2), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points

plt.plot(3.4, 13.1, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
plt.plot(3.4, 2 + 3.4**2 - 2*math.cos(2*math.pi*3.4), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points

plt.plot(3.3, 13.13, markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)    #plotting the points
plt.plot(3.3, 2 + 3.3**2 - 2*math.cos(2*math.pi*3.3), markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)    #plotting the points
plt.show()

plt.plot(xvals, yvals)    #plotting the points
plt.plot(xarr, yarr, color='g')    #connecting the points

plt.plot(3.2, 13.17, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
plt.plot(3.2, 2 + 3.2**2 - 2*math.cos(2*math.pi*3.2), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points

plt.plot(3.4, 13.1, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
plt.plot(3.4, 2 + 3.4**2 - 2*math.cos(2*math.pi*3.4), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points

plt.plot(3.3, 13.13, markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)    #plotting the points
plt.plot(3.3, 2 + 3.3**2 - 2*math.cos(2*math.pi*3.3), markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)    #plotting the points

xarr=[]#these arrays are for showing the points in the plot
yarr=[]
xarr.append(3.2)
yarr.append(13.17)
xarr.append(3.3)
yarr.append(13.13)

plt.plot(xarr, yarr, color='orange')    #connecting the points
plt.show()
