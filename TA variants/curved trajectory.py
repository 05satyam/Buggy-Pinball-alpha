import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *
import time

#creating the 3d space and bounds of objective function (currently rastrigin)
xvals = np.linspace(-5.12, 5.12, 300)
yvals = np.linspace(-5.12, 5.12, 300)

X, Y = np.meshgrid(xvals, yvals)
mc = np.vectorize(rastrigin)
Z = mc(X,Y, 10)

#plotting the objective function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

#arrays for showing trajectory plot points
xarr = []
yarr = []
zarr = []

#objective function variables - lower and upper x,y are function bounds
low_x = -5.12
up_x = 5.12
low_y = -5.12
up_y = 5.12
A = 10           
            
####### function to plot each point of trajectory #######
def plotPoint(x, y, z, i, step, color):
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    if i==0:
        ax.plot(x, y, z, markerfacecolor='black', markeredgecolor='black', marker='o', markersize=5)    #plotting the points
    else:
        ax.plot(x, y, z, markerfacecolor=color, markeredgecolor=color, marker='o', markersize=5)    #plotting the points
    print("point ",i," (",x,",",y,",",z,") and step ",step)
####### end of function ######

num_of_iter = 1     #1 full sweep of algorithm. Use multiple iterations for normalizing results

#define hyper-parameters
startStep = -.7
endStep = -.001
startAngle = 18
endAngle = 1
rounds = 1000
radius = 0.8


#for storing and porting to workbook
times=[]
results=[]

for exp in range(0, num_of_iter):
    #get random initial point
    x = random.uniform(low_x, up_x)
    y = random.uniform(low_y, up_y)
    z = rastrigin(x, y, A)
                    
    plotPoint(x, y, z, -1, 0, 'black')
                    
    start_time = time.process_time()
    #the actual procedure of the algorithm starts here
    for i in range(0, rounds):
        #radStep = radius / i + 1  #+1 to prevent divide by zero error
        #setting direction randomly, but not at a similar direction as the previous vector
        if i==0:
            xStep = random.uniform(-1, 1)
            yStep = random.uniform(-1, 1)
        else:
            if xStep>0 and yStep>0: 
                while xStep>0 and yStep>0:
                    xStep = random.uniform(-1, 1)
                    yStep = random.uniform(-1, 1)
            elif xStep>0 and yStep<0:
                while xStep>0 and yStep<0:
                    xStep = random.uniform(-1, 1)
                    yStep = random.uniform(-1, 1)
            elif xStep<0 and yStep<0:
                while xStep<0 and yStep<0:
                    xStep = random.uniform(-1, 1)
                    yStep = random.uniform(-1, 1)
            elif xStep<0 and yStep>0:
                while xStep<0 and yStep>0:
                    xStep = random.uniform(-1, 1)
                    yStep = random.uniform(-1, 1)
            else:
                xStep = random.uniform(-1, 1)
                yStep = random.uniform(-1, 1)
        #define cs for step and angle
        step = startStep - i*(startStep - endStep) / rounds                                                     #linear
#         step = (startStep - endStep)*(1 + math.cos(math.pi*i / rounds)) / 2 + endStep                       #cosine
#         step = (startStep - endStep)/(1 + math.exp(i/(rounds/15) - 7.5)) + endStep                          #sigmoid
#         step = (startStep - endStep)*(1 - (math.exp(math.log10(1 + 10/rounds)*i)) / (math.exp(math.log10(1 + 10/rounds)*rounds))) + endStep #logarithmic
#         step = (startStep-endStep)*math.exp(-i/(0.1*rounds)) + endStep                                      #exponential
                   
        a = startAngle - i*(startAngle-endAngle)/rounds                                                     #linear
#         a = (startAngle - endAngle)*(1 + math.cos(math.pi*i / rounds)) / 2 + endAngle                       #cosine
#         a = (startAngle - endAngle)/(1+math.exp(i/(rounds/15) - 7.5)) + endAngle                            #sigmoid
#         a = (startAngle - endAngle)*(1 - (math.exp(math.log10(1 + 10/rounds)*i)) / (math.exp(math.log10(1 + 10/rounds)*rounds))) + endAngle #logarithmic
#         a = (startAngle-endAngle)*math.exp(-i/(0.1*rounds)) + endAngle                                      #exponential
        
        #calculate z parameter of the vector
        zStep = math.sqrt((-(xStep**2)*(math.sin(math.radians(a))**2) - (yStep**2)*(math.sin(math.radians(a))**2))
                          /((math.sin(math.radians(a))**2) - 1))
        
        #find factor
        f = step/zStep
        
        #calculate steps of the vector for the given direction
        xStep = xStep*abs(f)
        yStep = yStep*abs(f)
        
        #start current vector
        while 1:
            #continue reducing in this direction until crossing the function
            x = x + xStep
            y = y + yStep
            z = z + step
            # hitting a border, instead of the function, stops the trajectory
            if x<low_x or y<low_y or x>up_x or y>up_y:
                x = x - xStep
                y = y - yStep
                z = z - step
                                        
                plotPoint(x, y, z, i, step, 'r')
                break
            onfunc=rastrigin(x, y, A)
            #onfunc=eggholder(x, y)
            # if the line crosses the function stop
            if abs(z-onfunc)<0.000001:# this means z-onfunc==0
                plotPoint(x, y, z, i, step, 'r')
                break
            # if the line is underneath the function, find the point crossing
            elif z<onfunc:
                inXstep = xStep
                inYstep = yStep
                inZstep = step
                #jump in the middle of the step until crossing point is detected
                while abs(z-onfunc)>0.000001 and inZstep!=0:
                    inZstep = inZstep/2
                    inXstep = inXstep/2
                    inYstep = inYstep/2
                    if z>onfunc:
                        x = x+inXstep
                        y = y+inYstep
                        z = z+inZstep
                    else:
                        x = x-inXstep
                        y = y-inYstep
                        z = z-inZstep
                    onfunc=rastrigin(x, y, A)                       
                    #onfunc=eggholder(x, y)
                    #if step gets too small, exit because we have a satisfactory accurate solution
                    if inZstep==0:
                        z=onfunc
                                        
                plotPoint(x, y, z, i, step, 'r')
                break

                        
    print(exp)
    ax.plot(xarr, yarr, zarr, color='b')    #connecting the points
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.process_time()-start_time
    times.append(total_time)
plotPoint(x, y, z, i, step, 'green')        
results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of variant tr3 it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")
plt.show()

import xlwt 
from xlwt import Workbook 
 
wb = Workbook() 
  
sheet1 = wb.add_sheet('variantCT_rastrigin')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
     
wb.save('variantCT_rastrigin.xls')
print("All saved")