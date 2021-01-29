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
rounds = 100 # number of parts that the threshold sequence will contain
steps = 10 # iterations that will occur within every threshold value
neighbor_distance = 1 # the distance that a possible neighbor can have in x or y dimension
low_x=-5.12
up_x=5.12
low_y=-5.12
up_y=5.12
total_iterations=rounds*steps

def get_neighbors(cur_val, func_low, func_up): # creating random neighbor on a dimension within a limit
    if cur_val-neighbor_distance>func_low:
        lower=cur_val-neighbor_distance
    else:
        lower=func_low
            
    if cur_val+neighbor_distance<func_up:
        upper=cur_val+neighbor_distance
    else:
        upper=func_up        
    return random.uniform(lower, upper)

def exponential_decay(i, T): # i=iteration and T=period
    return init_T*math.e**(-i/(0.1*T))

for exp in range(0, 100000):
    start_time=time.time()
    x = random.uniform(low_x, up_x) # initial solutions
    y = random.uniform(low_y, up_y)
    j=1 # total iterations count for every experiment
    change_count=0 # if result does not change for some iterations, the algorithm has reached its best
    for t in range(0, rounds):
        for i in range(0, steps):
            # get random neighbor
            neighbor_x=get_neighbors(x, low_x, up_x)
            neighbor_y=get_neighbors(y, low_y, up_y)
            
            # Check if neighbor is best so far
            cost_diff = rastrigin(x, y, A) - rastrigin(neighbor_x, neighbor_y, A)
            #cost_diff = ackley(x, y) - ackley(neighbor_x, neighbor_y)
            
            if cost_diff > -exponential_decay(j, total_iterations): # accept or reject neighbor
                x = neighbor_x
                y = neighbor_y
                
            if change_count==(total_iterations/2):
                break
            
            j+=1
            change_count+=1
    
    print(exp)
    z=rastrigin(x, y, A)
    #z=ackley(x, y)
    results.append(z)
    total_time=time.time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results)
time_average=sum(times)/len(times)
print("After 1000000 iterations of Threshold Accepting it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")