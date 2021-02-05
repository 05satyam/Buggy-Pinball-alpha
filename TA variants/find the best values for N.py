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
T = np.linspace(init_T, 0, rounds)
snd = np.linspace(2, 3, 5) #starting neighbor distance
fnd = np.linspace(0.1, 2, 20) #ending neighbor distance
low_x=-5.12
up_x=5.12
low_y=-5.12
up_y=5.12
num_of_iter=1000

def get_neighbors(cur_val, func_low, func_up, neighbor_distance): # creating random neighbor on a dimension within a limit
    if cur_val-neighbor_distance>func_low:
        lower=cur_val-neighbor_distance
    else:
        lower=func_low
            
    if cur_val+neighbor_distance<func_up:
        upper=cur_val+neighbor_distance
    else:
        upper=func_up        
    return random.uniform(lower, upper)

for s in snd:
    for f in fnd:
        for exp in range(0, num_of_iter):
            start_time=time.time()
            x = random.uniform(low_x, up_x) # initial solutions
            y = random.uniform(low_y, up_y)
            j=1
            d = np.linspace(s, f, rounds*steps)
            for t in T:
                for i in range(0, steps):
                    # get random neighbor
                    neighbor_x=get_neighbors(x, low_x, up_x, d[j-1])
                    neighbor_y=get_neighbors(y, low_y, up_y, d[j-1])
                    
                    # Check if neighbor is best so far
                    DE = rastrigin(x, y, A) - rastrigin(neighbor_x, neighbor_y, A)
                    
                    # if the new solution is better, accept it
                    if DE > -t:
                        x = neighbor_x
                        y = neighbor_y
                    
                    j+=1
            
            z=rastrigin(x, y, A)
            results.append(z)
            total_time=time.time()-start_time
            times.append(total_time)
        
        results_average=sum(results)/len(results)
        time_average=sum(times)/len(times)
        
        if results_average<1 and time_average<0.01:
            print("Value=",results_average,": snd=",s,"fnd=",f,"time=",time_average)
