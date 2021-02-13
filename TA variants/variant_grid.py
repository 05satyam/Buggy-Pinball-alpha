import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]

A = 10      # rastrigin factor
init_T = 0.2       # initial threshold
rounds = 100 # number of parts that the threshold sequence will contain
T = np.linspace(init_T, 0, rounds)
low_x=-5.12
up_x=5.12
low_y=-5.12
up_y=5.12
num_of_points=200 #factor to determine how smaller of the initial value the trajectory step will be
num_of_iter=10000
neighbor_distance = 0.2 # the distance that a possible neighbor can have in x or y dimension

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

for exp in range(0, num_of_iter):
    start_time=time.time()
    #create a grid and find the best value
    x_vals = np.linspace(low_x, up_x, num_of_points) # grid points
    y_vals = np.linspace(low_y, up_y, num_of_points)
    best_x = x_vals[0]
    best_y = y_vals[0]
    best_val = rastrigin(best_x, best_y,A)
    #print("Initial point: (",best_x,", ",best_y,")")
    for i in range(1,num_of_points): #grid points comparison
        z = rastrigin(x_vals[i], y_vals[i],A)
        if z < best_val:
            best_val = z
            best_x = x_vals[i]
            best_y = y_vals[i]
    
    x=best_x
    y=best_y
    z=rastrigin(x, y, A)
    #print("Best grid value",x,",",y,"=",best_val)
    for t in T: #TA on the best value to have a more accurate solution
        neighbor_x=get_neighbors(x, -5.12, 5.12)
        neighbor_y=get_neighbors(y, -5.12, 5.12)
        
        DE = z - rastrigin(neighbor_x, neighbor_y, A)# compare neighbors
        
        if DE > -t: # if the new solution is better, accept it
            x = neighbor_x
            y = neighbor_y
        
        z=rastrigin(x, y, A)
        #z=ackley(x, y)
        
    print(exp)
    #print("Best value",x,",",y,"=",z)
    results.append(z)
    total_time=time.time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results)
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of TA variant, it is found that it takes",time_average,"seconds and has a distance of",results_average, "from the global minimum")