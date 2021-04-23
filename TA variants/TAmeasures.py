import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]
A = 10      # rastrigin factor
init_T = 1             # initial threshold
rounds = 430000           # number of parts that the threshold sequence will contain
neighbor_distance = 4   # the distance that a possible neighbor can have in x or y dimension
T = np.linspace(init_T, 0, rounds)  #all threshold values for the TA
num_of_iter=100 #number of experiment iterations

# low_x=-5.12 #limits of dimensions that we move around
# up_x=5.12    #rastrigin
# low_y=-5.12  #dropwave
# up_y=5.12
# low_x=-5 #ackley
# up_x=5
# low_y=-5
# up_y=5
# low_x=-512
# up_x=512    #eggholder
# low_y=-512
# up_y=512
# low_x=-500  #schwefel
# up_x=500
# low_y=-500
# up_y=500
# low_x=-10  #easom#shubert#holdertable
# up_x=10
# low_y=-10
# up_y=10
# low_x=-2  #sphere
# up_x=2
# low_y=-2
# up_y=2
low_x=0  #langermann
up_x=10
low_y=0
up_y=10

for exp in range(0, num_of_iter):
    x = random.uniform(low_x, up_x) # initial solutions
    y = random.uniform(low_y, up_y)
#     z=rastrigin(x, y, A)
#     z=ackley(x, y)
#     z=eggholder(x, y)
#     z=schwefel(x,y)
#     z = easom(x, y)
#     z = sphere(x, y)
#     z = shubert(x, y)
#     z=holdertable(x, y)
#     z = dropwave(x, y)
    z = langermann(x, y)
    
    start_time=time.process_time()
    
    for t in T:
#         if time.process_time()-start_time>=0.5:
#             break
        
        if x-neighbor_distance>low_x: #setting lower limits
            lower = x - neighbor_distance
        else:
            lower = low_x
            
        if x+neighbor_distance<up_x: #setting upper limits
            upper = x + neighbor_distance
        else:
            upper=up_x
        neighbor_x = random.uniform(lower, upper)
        
        if y-neighbor_distance>low_y: #setting lower limits
            lower = y - neighbor_distance
        else:
            lower = low_y
          
        if y+neighbor_distance<up_y: #setting upper limits
            upper = y + neighbor_distance
        else:
            upper = up_y
        neighbor_y = random.uniform(lower, upper)
            
#         DE = z - rastrigin(neighbor_x, neighbor_y, A) #cost difference
#         DE = ackley(x, y) - ackley(neighbor_x, neighbor_y)
#         DE = eggholder(x, y) - eggholder(neighbor_x, neighbor_y)
#         DE = schwefel(x, y) - schwefel(neighbor_x, neighbor_y)
#         DE = easom(x, y) - easom(neighbor_x, neighbor_y)
#         DE = sphere(x, y) - sphere(neighbor_x, neighbor_y)
#         DE = shubert(x, y) - shubert(neighbor_x, neighbor_y)
#         DE = holdertable(x, y) - holdertable(neighbor_x, neighbor_y)
#         DE = dropwave(x, y) - dropwave(neighbor_x, neighbor_y)
        DE = langermann(x, y) - langermann(neighbor_x, neighbor_y)
        
        if DE > -t:    # if the new solution is better, accept it
            x = neighbor_x
            y = neighbor_y
            
#         z=rastrigin(x, y, A)
#         z=ackley(x, y)
#         z=eggholder(x, y)
#         z = schwefel(x,y)
#         z = easom(x, y)
#         z = sphere(x, y)
#         z = shubert(x, y)
#         z=holdertable(x, y)
#         z = dropwave(x, y)
        z = langermann(x, y)

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
      
sheet1 = wb.add_sheet('TA_langermann_3_secs_7')
i=0
for wr in results:
    sheet1.write(i, 0, wr)
    sheet1.write(i, 1, times[i])
    i+=1
         
wb.save('..\..\Results\TA_langermann_3_secs_7.xls')
print("All saved")