import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]
A = 10      # rastrigin factor
init_T = 800            # initial threshold
rounds = 4000000           # number of parts that the threshold sequence will contain
neighbor_distance = 300   # the distance that a possible neighbor can have in x or y dimension
T = np.linspace(init_T, 0, rounds)  #all threshold values for the TA
dimensions= 2

# low=-5.12 #limits of dimensions that we move around
# up=5.12    #rastrigin
# low=-5 #ackley
# up=5
low=-500  #schwefel
up=500
# low=-2  #sphere
# up=2
num_of_iter=10 #number of experiment iterations

for exp in range(0, num_of_iter):
    xvals=[]
    for i in range(0, dimensions):
        xvals.append(random.uniform(low, up))
#     z = rastrigin_d(xvals)
#     z = ackley_d(xvals)
    z = schwefel_d(xvals)
#     z = sphere_d(xvals)
    
    start_time=time.process_time()
    
    for t in T:
        neighbors=[]
        for i in xvals:
            if i - neighbor_distance > low: #setting lower limits
                lower = i - neighbor_distance
            else:
                lower = low
            
            if i + neighbor_distance < up: #setting upper limits
                upper = i + neighbor_distance
            else:
                upper = up
            neighbors.append(random.uniform(lower, upper))
            
#         DE = z - rastrigin_d(neighbors) #cost difference
#         DE = z - ackley_d(neighbors)
        DE = z - schwefel_d(neighbors)
#         DE = z - sphere_d(neighbors)
        
        if DE > -t:    # if the new solution is better, accept it
            for i in range(0, dimensions):
                xvals[i] = neighbors[i]
            
#         z = rastrigin_d(xvals)
#         z = ackley_d(xvals)
        z = schwefel_d(xvals)
#         z = sphere_d(xvals)
    print(exp)
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.process_time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of Threshold Accepting it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")
 
import xlwt 
from xlwt import Workbook 
    
wb = Workbook() 
     
sheet1 = wb.add_sheet('TA_schwefel4')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
        
wb.save('TA_schwefel4.xls')
print("All saved")