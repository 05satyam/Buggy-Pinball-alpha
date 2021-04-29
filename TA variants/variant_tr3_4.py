import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *
import time

A = 10
# low=-5.12    #rastrigin
# up=5.12      #dropwave
# low=-512  #eggholder
# up=512
# low=-500  #schwefel
# up=500
low=-10  #easom#holdertable
up=10    #shubert
# low=-5  #ackley
# up=5
# low=-2  #sphere
# up=2
# low=0  #langermann
# up=10

xvals = np.linspace(low, up, 300)
yvals = np.linspace(low, up, 300)
X, Y = np.meshgrid(xvals, yvals)

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
mc = np.vectorize(holdertable)
Z = mc(X,Y)
# mc = np.vectorize(dropwave)
# Z = mc(X,Y)
# mc = np.vectorize(langermann)
# Z = mc(X,Y)
  
#plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
    
xarr=[]#these arrays are for showing the points in the plot
yarr=[]
zarr=[]
            
#################################functions begin###########################################
def plotPoint(x, y, z, i, step, color, a):
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    if i==0:
        ax.plot(x, y, z, markerfacecolor='black', markeredgecolor='black', marker='o', markersize=5)    #plotting the points
    else:
        ax.plot(x, y, z, markerfacecolor=color, markeredgecolor=color, marker='o', markersize=5)    #plotting the points
    print("point ",i," (",x,",",y,",",z,") resultant",step,"angle",a)

#################################functions end############################################
num_of_iter=100
#define hyper-parameters
startResultant = -.5
endResultant = -.0001
startAngle = 1
endAngle = 89
rounds = 90000
numOfSteps = 10

times=[]
results=[]
for exp in range(0, num_of_iter):
    #get random initial point
    x, y = random.uniform(low, up), random.uniform(low, up)
#     z = rastrigin(x, y, A)
#     z = eggholder(x, y)
#     z = schwefel(x, y)
#     z = easom(x, y)
#     z = shubert(x, y)
#     z = sphere(x, y)
#     z = ackley(x, y)
    z = holdertable(x, y)
#     z = langermann(x, y)
#     z = dropwave(x, y)

#     plotPoint(x, y, z, -1, 0, 'black', -1)
                    
    start_time=time.process_time()
    i=0
    #the actual procedure of the algorithm starts here
    while i<rounds:
        #setting direction randomly, but not at a similar direction as the previous vector        
        xStep, yStep = random.uniform(-1, 1), random.uniform(-1, 1)
        #define cs for resultant and angle
        resultant = startResultant - i*(startResultant-endResultant)/rounds
        a = startAngle - i*(startAngle-endAngle)/rounds
        #calculate z parameter of the vector
        zStep = -math.sqrt((-(xStep**2)*(math.sin(math.radians(a))**2) - (yStep**2)*(math.sin(math.radians(a))**2))/((math.sin(math.radians(a))**2) - 1))
        #find resultant
        resultant_step = math.sqrt(xStep**2 + yStep**2 + zStep**2)
        factor = resultant / resultant_step
        #calculate steps of the vector for the given direction
        xStep, yStep, zStep = xStep*abs(factor), yStep*abs(factor), zStep*abs(factor)
        
        #start current vector
        countSteps = 0
        x_cur, y_cur, z_cur = x + xStep, y + yStep, z + zStep
#         onfunc = rastrigin(x_cur, y_cur, A)
#         onfunc = eggholder(x_cur, y_cur)
#         onfunc = schwefel(x_cur, y_cur)
#         onfunc = easom(x_cur, y_cur)
#         onfunc = shubert(x_cur, y_cur)
#         onfunc = sphere(x_cur, y_cur)
#         onfunc = ackley(x_cur, y_cur)
        onfunc = holdertable(x_cur, y_cur)
#         onfunc = langermann(x_cur, y_cur)
#         onfunc = dropwave(x_cur, y_cur)
        if z_cur < onfunc:
            isUnderneath = True
        else:
            isUnderneath = False
        while countSteps<numOfSteps:          
            if x_cur<low or y_cur<low or x_cur>up or y_cur>up:#no possible evaluation of function
                countSteps+=1
                continue
            
            if isUnderneath==False:
                # if the line is underneath the function, find the point crossing
                if z_cur<onfunc or abs(z_cur-onfunc)<0.000001:
                    inXstep, inYstep, inZstep = xStep, yStep, zStep
                    #jump in the middle of the step until crossing point is detected
                    while abs(z_cur-onfunc)>0.000001 and inZstep!=0:
                        inXstep, inYstep, inZstep = inXstep/2, inYstep/2, inZstep/2
                        if z_cur>onfunc:
                            x_cur, y_cur, z_cur = x_cur + inXstep, y_cur + inYstep, z_cur + inZstep
                        else:
                            x_cur, y_cur, z_cur = x_cur - inXstep, y_cur - inYstep, z_cur - inZstep
                        
#                         onfunc = rastrigin(x_cur, y_cur, A)
#                         onfunc = eggholder(x_cur, y_cur)
#                         onfunc = schwefel(x_cur, y_cur)
#                         onfunc = easom(x_cur, y_cur)
#                         onfunc = shubert(x_cur, y_cur)
                        onfunc = sphere(x_cur, y_cur)
#                         onfunc = ackley(x_cur, y_cur)
#                         onfunc = holdertable(x_cur, y_cur)
#                         onfunc = langermann(x_cur, y_cur)
#                         onfunc = dropwave(x_cur, y_cur)
                        
                        #if step gets too small, exit because we have a satisfactory accurate solution
                        if inZstep==0:
                            z_cur = onfunc                
#                     plotPoint(x_cur, y_cur, z_cur, i, resultant, 'r', a)
                    x, y, z = x_cur, y_cur, z_cur
                    break
            else:
                # if the line is underneath the function, find the point crossing
                if z_cur>onfunc or abs(z_cur-onfunc)<0.000001:
                    inXstep, inYstep, inZstep = xStep, yStep, zStep
                    #jump in the middle of the step until crossing point is detected
                    while abs(z_cur-onfunc)>0.000001 and inZstep!=0:
                        inXstep, inYstep, inZstep = inXstep/2, inYstep/2, inZstep/2
                        if z_cur<onfunc:
                            x_cur, y_cur, z_cur = x_cur + inXstep, y_cur + inYstep, z_cur + inZstep
                        else:
                            x_cur, y_cur, z_cur = x_cur - inXstep, y_cur - inYstep, z_cur - inZstep
                        
#                         onfunc = rastrigin(x_cur, y_cur, A)
#                         onfunc = eggholder(x_cur, y_cur)
#                         onfunc = schwefel(x_cur, y_cur)
#                         onfunc = easom(x_cur, y_cur)
#                         onfunc = shubert(x_cur, y_cur)
                        onfunc = sphere(x_cur, y_cur)
#                         onfunc = ackley(x_cur, y_cur)
#                         onfunc = holdertable(x_cur, y_cur)
#                         onfunc = langermann(x_cur, y_cur)
#                         onfunc = dropwave(x_cur, y_cur)
                        
                        #if step gets too small, exit because we have a satisfactory accurate solution
                        if inZstep==0:
                            z_cur = onfunc                
#                     plotPoint(x_cur, y_cur, z_cur, i, resultant, 'r', a)
                    x, y, z = x_cur, y_cur, z_cur
                    break
            countSteps+=1
            x_cur, y_cur, z_cur = x_cur + xStep, y_cur + yStep, z_cur + zStep
#             onfunc = rastrigin(x_cur, y_cur, A)
#             onfunc = eggholder(x_cur, y_cur)
#             onfunc = schwefel(x_cur, y_cur)
#             onfunc = easom(x_cur, y_cur)
#             onfunc = shubert(x_cur, y_cur)
            onfunc = sphere(x_cur, y_cur)
#             onfunc = ackley(x_cur, y_cur)
#             onfunc = holdertable(x_cur, y_cur)
#             onfunc = langermann(x_cur, y_cur)
#             onfunc = dropwave(x_cur, y_cur)
        i=i+1
    print(exp)
#     ax.plot(xarr, yarr, zarr, color='b')    #connecting the points
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.process_time()-start_time
    times.append(total_time)
# plotPoint(x, y, z, i, resultant, 'green', a)
results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of variant tr3 it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")
# plt.show()

import xlwt 
from xlwt import Workbook 
                    
wb = Workbook() 
                     
sheet1 = wb.add_sheet('variantTR4_sphere_3_secs_4')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
                        
wb.save('..\..\Results\\variantTR4_sphere_3_secs_4.xls')
print("All saved")