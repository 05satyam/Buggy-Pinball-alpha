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
    #A = 10            # rastrigin factor
    b = 0.001       # slow cooling variable
    x = random.uniform(-5, 5) # initial solutions
    y = random.uniform(-5, 5)
    initial_temp = 10 # starting temperature
    final_temp = .1   # final temperature
    neighbor_distance = 1 # the distance that a possible neighbor can have in x or y dimension
    
    #z=rastrigin(x, y, A)
    z=ackley(x, y)
    i=0 
    change_count=0 # if result does not change for some iterations, the algorithm has reached its best
    while initial_temp > final_temp:
        neighbor_x=get_neighbors(x, -5, 5)
        neighbor_y=get_neighbors(y, -5, 5)
    
        #cost_diff = z - rastrigin(neighbor_x, neighbor_y, A)
        cost_diff = z - ackley(neighbor_x, neighbor_y)
        
        if cost_diff > 0:   # if the new solution is better, accept it
            x = neighbor_x
            y = neighbor_y
            change_count=0
        else:   # if the new solution is not better, accept it with a probability of e^(-cost/temp)
            if random.uniform(0, 1) < math.exp(cost_diff / initial_temp):
                x = neighbor_x
                y = neighbor_y
                change_count=0
                
        if change_count==200:
            break
        
        #z=rastrigin(x, y, A)
        z=ackley(x, y) # this result is used in the next iteration to compare cost difference
        #print("Iteration ",i,": x =",x," y =",y," z =",z)
        
        initial_temp=initial_temp/(1+b*initial_temp)# decrement the temperature via slow cooling
        i+=1
        change_count+=1
    print(exp)
    results.append(z)
    total_time=time.time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results)
time_average=sum(times)/len(times)
print("After 1000000 iterations of Simulated Annealing it is found that it takes ",time_average," seconds and has a distance of ",results_average, " from the global minimum")