import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]

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

for exp in range(0, 100000):
    start_time=time.time()
    A = 10      # rastrigin factor
    x = random.uniform(-5, 5) # initial solutions
    y = random.uniform(-5, 5)
    init_T = 1       # initial threshold
    rounds = 100 # number of parts that the threshold sequence will contain
    steps = 10 # iterations that will occur within every threshold value
    neighbor_distance = 1 # the distance that a possible neighbor can have in x or y dimension
    T = np.linspace(init_T, 0, rounds)

    j=1
    change_count=0 # if result does not change for some iterations, the algorithm has reached its best
    for t in T:
        for i in range(0, steps):
            # get random neighbor
            neighbor_x=get_neighbors(x, -5, 5)
            neighbor_y=get_neighbors(y, -5, 5)
            
            # Check if neighbor is best so far
            #cost_diff = rastrigin(x, y, A) - rastrigin(neighbor_x, neighbor_y, A)
            cost_diff = ackley(x, y) - ackley(neighbor_x, neighbor_y)
            
            # if the new solution is better, accept it
            if cost_diff > -t:
                x = neighbor_x
                y = neighbor_y
                change_count=0
                
            if change_count==200:
                break
            
            j+=1
    
    print(exp)
    #z=rastrigin(x, y, A)
    z=ackley(x, y)
    results.append(z)
    total_time=time.time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results)
time_average=sum(times)/len(times)
print("After 1000000 iterations of Threshold Accepting it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")