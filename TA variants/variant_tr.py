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
low_x=-5.12
up_x=5.12
low_y=-5.12
up_y=5.12
percent_traj=0.1 #factor to determine how smaller of the initial value the trajectory step will be
num_of_iter=1000

for exp in range(0, num_of_iter):
    start_time=time.time()
    x = random.uniform(low_x, up_x) # initial solutions
    y = random.uniform(low_y, up_y)
    #print("Initial point: (",x,", ",y,")")
    for t in T:
        step_x = random.uniform(percent_traj*low_x, percent_traj*up_x)
        step_y = random.uniform(percent_traj*low_y, percent_traj*up_y)
        #print("Step of x:",step_x," Step of y:",step_y)
        for i in range(0, steps):
            if i==0:
                neighbor_x = x + step_x
                neighbor_y = y + step_y
            else:
                neighbor_x = neighbor_x + step_x
                neighbor_y = neighbor_y + step_y
            
            if neighbor_x>up_x or neighbor_x<low_x or neighbor_y>up_y or neighbor_y<low_y:
                break
            
            #print("    New neighbor:(",neighbor_x,", ",neighbor_y,")")
            DE = rastrigin(neighbor_x, neighbor_y, A) - rastrigin(x, y, A)
            #DE = ackley(neighbor_x, neighbor_y) - ackley(x, y)
                
            if DE < t:
                x = neighbor_x
                y = neighbor_y
                #print("        New value:(",neighbor_x,", ",neighbor_y,")")
    
    print(exp)
    z=rastrigin(x, y, A)
    #z=ackley(x, y)
    results.append(z)
    total_time=time.time()-start_time
    times.append(total_time)

results_average=sum(results)/len(results)
time_average=sum(times)/len(times)
print("After",num_of_iter,"iterations of TA variant, it is found that it takes",time_average,"seconds and has a distance of",results_average, "from the global minimum")