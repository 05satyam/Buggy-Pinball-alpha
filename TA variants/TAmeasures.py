import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]
A = 10      # rastrigin factor
init_T = 1       # initial threshold
rounds = 80000 # number of parts that the threshold sequence will contain
neighbor_distance = 1 # the distance that a possible neighbor can have in x or y dimension
T = np.linspace(init_T, 0, rounds)  #all threshold values for the TA
low_x=-5.12 #limits of dimensions that we move around
up_x=5.12
low_y=-5.12
up_y=5.12
num_of_iter=1000 #number of experiment iterations

for exp in range(0, num_of_iter):
    start_time=time.process_time()
    x = random.uniform(low_x, up_x) # initial solutions
    y = random.uniform(low_y, up_y)
    #z=rastrigin(x, y, A)
    #z=ackley(x, y)
    z=eggholder(x, y)
    for t in T:
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
            
        #DE = z - rastrigin(neighbor_x, neighbor_y, A) #cost difference
        #DE = ackley(x, y) - ackley(neighbor_x, neighbor_y)
        DE = eggholder(x, y) - eggholder(neighbor_x, neighbor_y)
        
        if DE > -t:    # if the new solution is better, accept it
            x = neighbor_x
            y = neighbor_y
            
        #z=rastrigin(x, y, A)
        #z=ackley(x, y)
        z=eggholder(x, y)
    print(exp)
    
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.process_time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of Threshold Accepting it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")