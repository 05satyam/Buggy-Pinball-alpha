import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from functions import *

A = 10      # rastrigin factor
init_T = 1       # initial threshold
rounds = 100 # number of parts that the threshold sequence will contain
T = np.linspace(init_T, 0, rounds)
low_x=-5.12
up_x=5.12
low_y=-5.12
up_y=5.12
num_of_iter=1000

pt = np.linspace(0.01, 0.2, 20)
st = np.linspace(5, 50, 46)

for steps in st:
    for percent_traj in pt:
        times=[]
        results=[]
        for exp in range(0, num_of_iter):
            start_time=time.time()
            x = random.uniform(low_x, up_x) # initial solutions
            y = random.uniform(low_y, up_y)
            for t in T:
                step_x = random.uniform(percent_traj*low_x, percent_traj*up_x)
                step_y = random.uniform(percent_traj*low_y, percent_traj*up_y)
                for i in range(0, int(steps)):
                    if i==0:
                        neighbor_x = x + step_x
                        neighbor_y = y + step_y
                    else:
                        neighbor_x = neighbor_x + step_x
                        neighbor_y = neighbor_y + step_y
                    
                    if neighbor_x > up_x or neighbor_x < low_x or neighbor_y > up_y or neighbor_y < low_y:
                        break
                    
                    DE = rastrigin(neighbor_x, neighbor_y, A) - rastrigin(x, y, A)
                        
                    if DE < t:
                        x = neighbor_x
                        y = neighbor_y
            
            z=rastrigin(x, y, A)
            results.append(z)
            total_time=time.time()-start_time
            times.append(total_time)
        
        results_average=sum(results)/len(results)
        time_average=sum(times)/len(times)
            
        if results_average<0.7 and time_average<0.007:
            print("Value=",results_average,": percentage=",percent_traj,"steps=",steps,"time=",time_average)
