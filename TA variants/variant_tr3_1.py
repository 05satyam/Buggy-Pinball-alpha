import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *
import time

# low_x=-5.12    #rastrigin
# up_x=5.12      #dropwave
# low_y=-5.12
# up_y=5.12
# A = 10
# low_x=-512  #eggholder
# up_x=512
# low_y=-512
# up_y=512
# low_x=-500  #schwefel
# up_x=500
# low_y=-500
# up_y=500
# low_x=-10  #easom
# up_x=10    #shubert
# low_y=-10  #holdertable
# up_y=10
# low_x=-5  #ackley
# up_x=5    
# low_y=-5
# up_y=5
# low_x=-2  #sphere
# up_x=2
# low_y=-2
# up_y=2
low_x=0  #langermann
up_x=10
low_y=0
up_y=10

# xvals = np.linspace(low_x, up_x, 300)
# yvals = np.linspace(low_y, up_y, 300)
# X, Y = np.meshgrid(xvals, yvals)

# mc = np.vectorize(rastrigin)
# Z = mc(X,Y, 10)
# mc = np.vectorize(eggholder)
# Z = mc(X,Y)
# mc = np.vectorize(schwefel)
# Z = mc(X,Y)
# mc = np.vectorize(easom)
# Z = mc(X,Y)
# mc = np.vectorize(shubert)
# Z = mc(X,Y)
# mc = np.vectorize(sphere)
# Z = mc(X,Y)
# mc = np.vectorize(ackley)
# Z = mc(X,Y)
# mc = np.vectorize(holdertable)
# Z = mc(X,Y)
# mc = np.vectorize(dropwave)
# Z = mc(X,Y)
# mc = np.vectorize(langermann)
# Z = mc(X,Y)
#  
# #plotting the function
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.2)
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
#    
# xarr=[]#these arrays are for showing the points in the plot
# yarr=[]
# zarr=[]
            
#################################functions begin###########################################
def plotPoint(x, y, z, i, step, color, a):
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    if i==0:
        ax.plot(x, y, z, markerfacecolor='black', markeredgecolor='black', marker='o', markersize=5)    #plotting the points
    else:
        ax.plot(x, y, z, markerfacecolor=color, markeredgecolor=color, marker='o', markersize=5)    #plotting the points
    print("point ",i," (",x,",",y,",",z,") step",step,"angle",a)

#################################functions end############################################
num_of_iter=10
#define hyper-parameters
startStep = -.5
endStep = -.001
startAngle = 50
endAngle = 3
rounds = 200000
numOfSteps = 25

times=[]
results=[]
for exp in range(0, num_of_iter):
    #get random initial point
    x = random.uniform(low_x, up_x)
    y = random.uniform(low_y, up_y)
#     z = rastrigin(x, y, A)
#     z = eggholder(x, y)
#     z = schwefel(x, y)
#     z = easom(x, y)
#     z = shubert(x, y)
#     z = sphere(x, y)
#     z = ackley(x, y)
#     z = holdertable(x, y)
#     z = langermann(x, y)
    z = dropwave(x, y)

#     plotPoint(x, y, z, -1, 0, 'black', -1)
                    
    start_time=time.process_time()
    i=0
    #the actual procedure of the algorithm starts here
    while i<rounds:
#         if time.process_time()-start_time>=0.5:
#             break
        #setting direction randomly, but not at a similar direction as the previous vector
        
        xStep = random.uniform(-1, 1)
        yStep = random.uniform(-1, 1)
        
        #define cs for step and angle
        step = startStep - i*(startStep-endStep)/rounds                                                     #linear
#         step = (startStep - endStep)*(1 + math.cos(math.pi*i / rounds)) / 2 + endStep                       #cosine
#         step = (startStep - endStep)/(1 + math.exp(i/(rounds/15) - 7.5)) + endStep                          #sigmoid
#         step = (startStep - endStep)*(1 - (math.exp(math.log10(1 + 10/rounds)*i)) / (math.exp(math.log10(1 + 10/rounds)*rounds))) + endStep #logarithmic
#         step = (startStep-endStep)*math.exp(-i/(0.1*rounds)) + endStep                                      #exponential

        a = startAngle - i*(startAngle-endAngle)/rounds                                                     #linear
#         a = (startAngle - endAngle)*(1 + math.cos(math.pi*i / rounds)) / 2 + endAngle                       #cosine
#         a = (startAngle - endAngle)/(1+math.exp(i/(rounds/15) - 7.5)) + endAngle                            #sigmoid
#         a = (startAngle - endAngle)*(1 - (math.exp(math.log10(1 + 10/rounds)*i)) / (math.exp(math.log10(1 + 10/rounds)*rounds))) + endAngle #logarithmic
#         a = (startAngle-endAngle)*math.exp(-i/(0.05*rounds)) + endAngle                                      #exponential
        
        #calculate z parameter of the vector
        zStep = math.sqrt((-(xStep**2)*(math.sin(math.radians(a))**2) - (yStep**2)*(math.sin(math.radians(a))**2))/((math.sin(math.radians(a))**2) - 1))
        #find factor
        f=step/zStep
        #calculate steps of the vector for the given direction
        xStep = xStep*abs(f)
        yStep = yStep*abs(f)
        #start current vector
        firstTime = True
        OutOfBounds = False
        countSteps = 0
        #print("Elevation",step,"Factor ",f,"Steps are ",xStep,",",yStep,",",zStep)
        while countSteps<numOfSteps:
            #continue reducing in this direction until crossing the function
            x = x + xStep
            y = y + yStep
            z = z + step
            
#             onfunc = rastrigin(x, y, A)
#             onfunc = eggholder(x, y)
#             onfunc = schwefel(x, y)
#             onfunc = easom(x, y)
#             onfunc = shubert(x, y)
#             onfunc = sphere(x, y)
#             onfunc = ackley(x, y)
#             onfunc = holdertable(x, y)
#             onfunc = langermann(x, y)
            onfunc = dropwave(x, y)
            
            if firstTime==True:
                if z < onfunc:
                    isUnderneath = True
                else:
                    isUnderneath = False
                firstTime = False
            
            if x<low_x or y<low_y or x>up_x or y>up_y:#no possible evaluation of function
                OutOfBounds = True
                countSteps+=1
                continue
            
            if isUnderneath==False:
                # if the line crosses the function stop
                if abs(z-onfunc)<0.000001:# this means z-onfunc==0
#                     plotPoint(x, y, z, i, step, 'r', a)
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
                        
#                         onfunc = rastrigin(x, y, A)
#                         onfunc = eggholder(x, y)
#                         onfunc = schwefel(x, y)
#                         onfunc = easom(x, y)
#                         onfunc = shubert(x, y)
#                         onfunc = sphere(x, y)
#                         onfunc = ackley(x, y)
#                         onfunc = holdertable(x, y)
#                         onfunc = langermann(x, y)
                        onfunc = dropwave(x, y)
                        
                        #if step gets too small, exit because we have a satisfactory accurate solution
                        if inZstep==0:
                            z=onfunc                
#                     plotPoint(x, y, z, i, step, 'r', a)
                    break
                countSteps+=1
            else:
                # if the line crosses the function stop
                if abs(z-onfunc)<0.000001:# this means z-onfunc==0
#                     plotPoint(x, y, z, i, step, 'r', a)
                    break
                # if the line is over the function, find the point crossing
                elif z>onfunc:
                    inXstep = xStep
                    inYstep = yStep
                    inZstep = step
                    #jump in the middle of the step until crossing point is detected
                    while abs(z-onfunc)>0.000001 and inZstep!=0:
                        inZstep = inZstep/2
                        inXstep = inXstep/2
                        inYstep = inYstep/2
                        if z<onfunc:
                            x = x+inXstep
                            y = y+inYstep
                            z = z+inZstep
                        else:
                            x = x-inXstep
                            y = y-inYstep
                            z = z-inZstep
                        
#                         onfunc = rastrigin(x, y, A)
#                         onfunc = eggholder(x, y)
#                         onfunc = schwefel(x, y)
#                         onfunc = easom(x, y)
#                         onfunc = shubert(x, y)
#                         onfunc = sphere(x, y)
#                         onfunc = ackley(x, y)
#                         onfunc = holdertable(x, y)
#                         onfunc = langermann(x, y)
                        onfunc = dropwave(x, y)
                        
                        #if step gets too small, exit because we have a satisfactory accurate solution
                        if inZstep==0:
                            z=onfunc                 
#                     plotPoint(x, y, z, i, step, 'r', a)
                    break
                countSteps+=1
        i=i+1
        
        if countSteps==numOfSteps or OutOfBounds==True:
            x = x - countSteps*xStep
            y = y - countSteps*yStep
            z = z - countSteps*step
                        
    print(exp)
#     ax.plot(xarr, yarr, zarr, color='b')    #connecting the points
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.process_time()-start_time
    times.append(total_time)
# plotPoint(x, y, z, i, step, 'green', a)
results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of variant tr3 it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")
# plt.show()

import xlwt 
from xlwt import Workbook 
             
wb = Workbook() 
              
sheet1 = wb.add_sheet('variantTR3_langermann_3_secs_8')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
                 
wb.save('..\..\Results\\variantTR3_langermann_3_secs_8.xls')
print("All saved")