import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *
import time

###############limits of variables for each function#####################
low=-5.12    #rastrigin
up=5.12     #dropwave
# low=-500  #schwefel
# up=500
# low=-5  #ackley
# up=5
# low=-2  #sphere
# up=2
# low=0  #langermann
# up=10
# low=-10  #easom
# up=10
# low=-512  #eggholder
# up=512
#################################functions begin###########################################
def plotPoint(xvals, cost, i, step, a):
    print("point ",i," (", end =" ")
    for x in xvals:
        print(x,",", end =" ")
    print(cost,") step",step,"angle",a)
#################################functions end############################################
num_of_iter=30
dimensions = 2  #without y axis
#define hyper-parameters
startResultant = -.5
endResultant = -.0001
startAngle = 20
endAngle = 40
rounds = 1100
numOfSteps = 30
fitness = rastrigin

times=[]
results=[]
exp=0
while exp<num_of_iter:#number of experiments
    #get random initial point
    xvals=[]
    for i in range(0, dimensions):
        xvals.append(random.uniform(low, up))
    y = fitness(xvals)

#     plotPoint(xvals, y, -1, startResultant, startAngle)
                    
    start_time=time.process_time()
    i=0
    #the actual procedure of the algorithm starts here
    while i<rounds:
        #setting direction randomly     
        xsteps=[]
        for j in range(0, dimensions):
            xsteps.append(random.uniform(-1, 1))
        #define cooling schedules for resultant and angle
        resultant = startResultant - i*(startResultant-endResultant)/rounds
        a = startAngle - i*(startAngle-endAngle)/rounds
        
        numerator=0
        for j in xsteps:
            numerator += -(j**2)*(math.sin(math.radians(a))**2)
        yStep = -math.sqrt(numerator/((math.sin(math.radians(a))**2) - 1))      
        #find resultant
        resultant_step = 0
        for j in xsteps:
            resultant_step+=j**2
        resultant_step = math.sqrt(resultant_step + yStep**2)
        #find factor
        f=resultant/resultant_step
        #calculate steps of the vector for the given direction
        for j in range(0, dimensions):
            xsteps[j] = xsteps[j]*abs(f)
        yStep = yStep*abs(f)
        #start current vector
        countSteps = 0
        xcurs = []
        for j in range(0, dimensions):
            xcurs.append(xvals[j] + xsteps[j])
        yCur = y + yStep
        
        onfunc = fitness(xcurs)
        
        if yCur < onfunc:
            isUnderneath = True
        else:
            isUnderneath = False
        
        OutOfBounds=False
        while countSteps<numOfSteps:          
            for j in xcurs:#no possible evaluation of function
                if j<low or j>up:
                    OutOfBounds=True
                    break
            if OutOfBounds==True:
                countSteps+=1
                break
            if isUnderneath==False:
                if yCur<onfunc or abs(yCur-onfunc)<0.000001:####crossing detected implementation
                    ####recursive refining implementation
                    inSteps=[]
                    for j in xsteps:
                        inSteps.append(j)
                    inYstep = yStep
                    #jump in the middle of the step until crossing point is detected
                    while abs(yCur-onfunc)>0.000001 and inYstep!=0:
                        for j in range(0, dimensions):
                            inSteps[j] = inSteps[j]/2
                        inYstep = inYstep/2
                        if yCur>onfunc:
                            for j in range(0, dimensions):
                                xcurs[j] += inSteps[j]
                            yCur += inYstep
                        else:
                            for j in range(0, dimensions):
                                xcurs[j] -= inSteps[j]
                            yCur -= inYstep
                        
                        onfunc = fitness(xcurs)
                        #if step gets too small, exit because we have a satisfactorily accurate solution
                        if inYstep==0:
                            yCur = onfunc
                    for j in range(0, dimensions):
                        xvals[j] = xcurs[j]
                    y = onfunc                
#                     plotPoint(xvals, y, i, resultant, a)
                    break
            else:
                if yCur>onfunc or abs(yCur-onfunc)<0.000001:####crossing detected implementation
                    ####recursive refining implementation
                    inSteps=[]
                    for j in xsteps:
                        inSteps.append(j)
                    inYstep = yStep
                    #jump in the middle of the step until crossing point is detected
                    while abs(yCur-onfunc)>0.000001 and inYstep!=0:
                        for j in range(0, dimensions):
                            inSteps[j] = inSteps[j]/2
                        inYstep = inYstep/2
                        if yCur<onfunc:
                            for j in range(0, dimensions):
                                xcurs[j] += inSteps[j]
                            yCur += inYstep
                        else:
                            for j in range(0, dimensions):
                                xcurs[j] -= inSteps[j]
                            yCur -= inYstep
                        
                        onfunc = fitness(xcurs)
                        #if step gets too small, exit because we have a satisfactorily accurate solution
                        if inYstep==0:
                            yCur = onfunc
                    for j in range(0, dimensions):
                        xvals[j] = xcurs[j]
                    y = onfunc                
#                     plotPoint(xvals, y, i, resultant, a)
                    break
            countSteps+=1
            for j in range(0, dimensions):
                xcurs[j] += xsteps[j]
            yCur += yStep
            onfunc = fitness(xcurs)
        i=i+1
    print(exp)
    total_time=time.process_time()-start_time
#     if total_time<60:
    results.append(y) #collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp+=1
#     print("Time:",total_time,"Precision:",y)
# plotPoint(xvals, y, i, resultant, a)
results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of variant tr3 it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")
###############store results to xls file##############
# import xlwt 
# from xlwt import Workbook 
#                        
# wb = Workbook() 
# 
# sheet1 = wb.add_sheet('file')
# i=0
# for wr in results:
#     sheet1.write(i, 0, wr)
#     sheet1.write(i, 1, times[i])
#     i+=1
# 
# wb.save('..\Results\\variantTR4_schwefel_3_secs_1.xls')
# print("All saved")