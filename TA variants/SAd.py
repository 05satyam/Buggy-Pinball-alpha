import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]
A = 10      # rastrigin factor
final_temp = 0.01   # final temperature
b = 0.9999996  # reducing factor of temperature
neighbor_distance = 1 # the distance that a possible neighbor can have in x or y dimension
dimensions= 9

low=-5.12    #rastrigin
up=5.12      #dropwave
# low=-512  #eggholder
# up=512
# low=-500  #schwefel
# up=500
# low=-10  #easom#holdertable
# up=10    #shubert
# low=-5  #ackley
# up=5
# low=-2  #sphere
# up=2
# low=0  #langermann
# up=10
num_of_iter=100 #number of experiment iterations

exp=0
while exp<num_of_iter:
    start_time=time.process_time()
    T = 10 # starting temperature
    xvals=[]
    for i in range(0, dimensions):
        xvals.append(random.uniform(low, up))
    
    z = rastrigin_d(xvals)
#     z = ackley_d(xvals)
#     z = schwefel_d(xvals)
#     z = sphere_d(xvals)
#     z = easom(xvals)
#     z = shubert(xvals)
#     z = eggholder(xvals)
#     z = dropwave(xvals)
#     z = langermann(xvals)
#     z = holdertable(xvals)
#     count=0
    while T>final_temp:
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
    
        DE = z - rastrigin_d(neighbors) #cost difference
#         DE = z - ackley_d(neighbors)
#         DE = z - schwefel_d(neighbors)
#         DE = z - sphere_d(neighbors)
#         DE = z - easom(neighbors)
#         DE = z - shubert(neighbors)
#         DE = z - eggholder(neighbors)
#         DE = z - dropwave(neighbors)
#         DE = z - langermann(neighbors)
#         DE = z - holdertable(neighbors)

        if DE > 0:   # if the neighbor is better, accept it
            for i in range(0, dimensions):
                xvals[i] = neighbors[i]
        else:   # if not, accept it with a probability
            if random.uniform(0, 1) < math.exp(DE / T):
                for i in range(0, dimensions):
                    xvals[i] = neighbors[i]
        
        z = rastrigin_d(xvals)
#         z = ackley_d(xvals)
#         z = schwefel_d(xvals)
#         z = sphere_d(xvals)
#         z = easom(xvals)
#         z = shubert(xvals)
#         z = eggholder(xvals)
#         z = dropwave(xvals)
#         z = langermann(xvals)
#         z = holdertable(xvals)
        
        T=b*T
#         count+=1
#         print("Iteration ",count,": x =",xvals[0]," y =",xvals[1],"z = ",xvals[2]," w =",z)
    print(exp)
    total_time=time.process_time()-start_time
#     if (total_time>5):
    results.append(z) #collect accuracy and time results of each algorithm run
    times.append(total_time)
    exp+=1
results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of Simulated Annealing it is found that it takes ",time_average," seconds and to have an accuracy of ",results_average, " from the global minimum")

import xlwt 
from xlwt import Workbook 
         
wb = Workbook() 
          
sheet1 = wb.add_sheet('file')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
             
wb.save('SA_rastrigin_10_secs.xls')
print("All saved")