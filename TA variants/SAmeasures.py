import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

times=[]
results=[]
A = 10      # rastrigin factor
final_temp = .01   # final temperature
b = 0.9985 # reducing factor of temperature
neighbor_distance = 1 # the distance that a possible neighbor can have in x or y dimension
low_x=-5.12 #limits of dimensions that we move around
up_x=5.12
low_y=-5.12
up_y=5.12
num_of_iter=1000 #number of experiment iterations

def get_neighbors(cur_val, func_low, func_up): # creating random neighbor on a dimension within a limit
    if cur_val-neighbor_distance>func_low: #setting lower limits
        lower=cur_val-neighbor_distance
    else:
        lower=func_low
        
    if cur_val+neighbor_distance<func_up: #setting upper limits
        upper=cur_val+neighbor_distance
    else:
        upper=func_up
        
    return random.uniform(lower, upper) #get random neighbor

for exp in range(0, num_of_iter):
    start_time=time.time()
    T = 10 # starting temperature
    x = random.uniform(low_x, up_x) # initial solutions
    y = random.uniform(low_y, up_y)
    
    z=rastrigin(x, y, A)
    #z=ackley(x, y)
    while T>final_temp:
        neighbor_x=get_neighbors(x, low_x, up_x)
        neighbor_y=get_neighbors(y, low_y, up_y)
    
        DE = z - rastrigin(neighbor_x, neighbor_y, A) #cost difference
        #DE = ackley(x, y) - ackley(neighbor_x, neighbor_y)
        
        if DE > 0:   # if the neighbor is better, accept it
            x = neighbor_x
            y = neighbor_y
        else:   # if not, accept it with a probability
            if random.uniform(0, 1) < math.exp(DE / T):
                x = neighbor_x
                y = neighbor_y
        
        z=rastrigin(x, y, A)
        #z=ackley(x, y)
        T=b*T
        #print("Iteration ",i,": x =",x," y =",y," z =",z)
    print(exp)
    results.append(z) #collect accuracy and time results of each algorithm run
    total_time=time.time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results) #get an average
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of Simulated Annealing it is found that it takes ",time_average," seconds and to have an accuracy of ",results_average, " from the global minimum")