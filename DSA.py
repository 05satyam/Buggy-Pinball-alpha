import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *
A = 10      # rastrigin factor
x = -5.12   # initial solutions
y = -5.12   #
init_T = 1       # initial threshold
rounds = 100 # number of parts that the threshold sequence will contain
steps = 10 # iterations that will occur within every threshold value
init_nei_dist = 3 # the distance that a possible neighbor can have in x or y dimension

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

def logarithmic_decay(i, T): # i=iteration and T=period
    return init_T*(1 - (math.e**(math.log10(1 + 10/T)*i)) / (math.e**(math.log10(1 + 10/T)*T)))
    
d = np.linspace(init_nei_dist, 0.1, rounds*steps) # decrease the neighbor distance linearly
z=rastrigin(x, y, A)
print("Initial values: x =",x," y =",y," z =",z)
j=1
change_count=0 # if result does not change for some iterations, the algorithm has reached its best
for t in range(0, rounds):
    for i in range(0, steps):
        neighbor_x=get_neighbors(x, -5.12, 5.12, d[j-1])# get neighbor
        neighbor_y=get_neighbors(y, -5.12, 5.12, d[j-1])
        
        cost_diff = rastrigin(x, y, A) - rastrigin(neighbor_x, neighbor_y, A) # calculate neighbor efficiency
        
        if cost_diff > -logarithmic_decay(j, rounds*steps): # accept or reject neighbor
            x = neighbor_x
            y = neighbor_y
        
        z=rastrigin(x, y, A)
        print("Iteration ",j," of threshold ", logarithmic_decay(j, rounds*steps),": x =",x," y =",y," z =",z)
        j+=1
        
print("Final Answer: x = ", x, " y = ", y, " z = ", rastrigin(x, y, A), " with a total of ",j-1," iterations")
