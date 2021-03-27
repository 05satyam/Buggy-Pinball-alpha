import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *
import time

low=-5.12    #rastrigin
up=5.12
# low_x=-512  #eggholder
# up_x=512
# low_y=-512
# up_y=512
# low_x=-500  #schwefel
# up_x=500
# low_y=-500
# up_y=500 
# low_x=-50  #griewank
# up_x=50
# low_y=-50
# up_y=50
# low_x=-10  #easom#shubert#alpine
# up_x=10
# low_y=-10
# up_y=10
# low_x=-5  #ackley
# up_x=5    
# low_y=-5
# up_y=5
# low_x=-2  #sphere
# up_x=2
# low_y=-2
# up_y=2
            
#################################functions begin###########################################
def plotPoint(xvals, cost, i, step, a):
    print("point ",i," (", end =" ")
    for x in xvals:
        print(x,",", end =" ")
    print(cost,") step",step,"angle",a)
#################################functions end############################################
num_of_iter=100
dimensions=3 #except cost
#define hyper-parameters
startStep = -.3
endStep = -.001
startAngle = 60
endAngle = 30
rounds = 5000
numOfSteps = 1000

times=[]
results=[]
for exp in range(0, num_of_iter):
    #get random initial point
    xvals=[]
    for i in range(0, dimensions):
        xvals.append(random.uniform(low, up))
    cost = rastrigin_d(xvals)
#     z = eggholder(x, y)
#     z = schwefel(x, y)
#     z = easom(x, y)
#     z = shubert(x, y)
#     z = sphere(x, y)
#     z = ackley(x, y)
#     z = alpine(x, y)
#     z = griewank(x, y)
    
#     plotPoint(xvals, cost, -1, startStep, startAngle)
                    
    start_time=time.process_time()
    i=0
    #the actual procedure of the algorithm starts here
    while i<rounds:
        #setting direction randomly, but not at a similar direction as the previous vector
        xsteps=[]
        for j in range(0, dimensions):
            xsteps.append(random.uniform(-1, 1))
        
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
        numerator=0
        for j in xsteps:
            numerator += -(j**2)*(math.sin(math.radians(a))**2)
        costStep = math.sqrt(numerator/((math.sin(math.radians(a))**2) - 1))
        #find factor
        f=step/costStep
        #calculate steps of the vector for the given direction
        for j in range(0, dimensions):
            xsteps[j] = xsteps[j]*abs(f)
        #start current vector
        firstTime = True
        OutOfBounds = False
        countSteps = 0
   
        while countSteps<numOfSteps:
            #continue reducing in this direction until crossing the function
            for j in range(0, dimensions):
                xvals[j] = xvals[j] + xsteps[j]
                
            cost = cost + step
            
            onfunc=rastrigin_d(xvals)
#             onfunc=eggholder(x, y)
#             onfunc = schwefel(x, y)
#             onfunc = easom(x, y)
#             onfunc = shubert(x, y)
#             onfunc = sphere(x, y)
#             onfunc = ackley(x, y)
#             onfunc = alpine(x, y)
#             onfunc = griewank(x, y)
            
            if firstTime==True:
                if cost < onfunc:
                    isUnderneath = True
                else:
                    isUnderneath = False
                firstTime = False

            for j in xvals:#no possible evaluation of function
                if j<low or j>up:
                    OutOfBounds = True
                    countSteps+=1
                    break
                    
            if OutOfBounds==True:
                continue
            
            if isUnderneath==False:
                # if the line crosses the function stop
                if abs(cost-onfunc)<0.000001:# this means cost-onfunc==0
#                     plotPoint(xvals, cost, i, step, a)
                    break
                # if the line is underneath the function, find the point crossing
                elif cost<onfunc:
                    inVals=[]
                    for j in xsteps:
                        inVals.append(j)
                    inCost = step
                    #jump in the middle of the step until crossing point is detected
                    while abs(cost-onfunc)>0.000001 and inCost!=0:
                        for j in range(0, dimensions):
                            inVals[j] = inVals[j]/2
                        inCost = inCost/2
                        if cost>onfunc:
                            for j in range(0, dimensions):
                                xvals[j] = xvals[j] + inVals[j]
                            cost = cost + inCost
                        else:
                            for j in range(0, dimensions):
                                xvals[j] = xvals[j] - inVals[j]
                            cost = cost - inCost
                        
                        onfunc = rastrigin_d(xvals)
#                         onfunc = eggholder(x, y)
#                         onfunc = schwefel(x, y)
#                         onfunc = easom(x, y)
#                         onfunc = shubert(x, y)
#                         onfunc = sphere(x, y)
#                         onfunc = ackley(x, y)   
#                         onfunc = alpine(x, y)
#                         onfunc = griewank(x, y)
                        
                        #if step gets too small, exit because we have a satisfactory accurate solution
                        if inCost==0:
                            cost=onfunc
                                            
#                     plotPoint(xvals, cost, i, step, a)
                    break
                countSteps+=1
            else:
                # if the line crosses the function stop
                if abs(cost-onfunc)<0.000001:# this means z-onfunc==0
#                     plotPoint(xvals, cost, i, step, a)
                    break
                # if the line is over the function, find the point crossing
                elif cost>onfunc:
                    inVals=[]
                    for j in xsteps:
                        inVals.append(j)
                    inCost = step
                    #jump in the middle of the step until crossing point is detected
                    while abs(cost-onfunc)>0.000001 and inCost!=0:
                        for j in range(0, dimensions):
                            inVals[j] = inVals[j]/2
                        inCost = inCost/2
                        if cost<onfunc:
                            for j in range(0, dimensions):
                                xvals[j] = xvals[j] + inVals[j]
                            cost = cost + inCost
                        else:
                            for j in range(0, dimensions):
                                xvals[j] = xvals[j] - inVals[j]
                            cost = cost - inCost
                        
                        onfunc = rastrigin_d(xvals)
#                         onfunc = eggholder(x, y)
#                         onfunc = schwefel(x, y)
#                         onfunc = easom(x, y)
#                         onfunc = shubert(x, y)
#                         onfunc = sphere(x, y)
#                         onfunc = ackley(x, y)   
#                         onfunc = alpine(x, y)
#                         onfunc = griewank(x, y)
                        
                        #if step gets too small, exit because we have a satisfactory accurate solution
                        if inCost==0:
                            cost = onfunc
#                     plotPoint(xvals, cost, i, step, a)
                    break
                countSteps+=1
        i=i+1
        
        if countSteps==numOfSteps or OutOfBounds==True:
            for j in range(0, dimensions):
                xvals[j] = xvals[j] - countSteps*xsteps[j]
            cost = cost - countSteps*step
                        
    print(exp)
    results.append(cost) #collect accuracy and time results of each algorithm run
    total_time=time.process_time()-start_time
    times.append(total_time)
# plotPoint(xvals, cost, i, step, a)
results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of variant tr3 it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")

import xlwt 
from xlwt import Workbook 
        
wb = Workbook() 
         
sheet1 = wb.add_sheet('variantTR3_rastrigin4')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
            
wb.save('variantTR3_rastrigin4.xls')
print("All saved")