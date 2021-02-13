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
neighbor_distance = 1 # the distance that a possible neighbor can have in x or y dimension

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
    
# create the threshold sequence
T = np.linspace(init_T, 0, rounds)

z=rastrigin(x, y, A)
print("Initial values: x =",x," y =",y," z =",z)
j=1
change_count=0 # if result does not change for some iterations, the algorithm has reached its best
for t in T:
    for i in range(0, steps):
        # get random neighbor
        neighbor_x=get_neighbors(x, -5.12, 5.12)
        neighbor_y=get_neighbors(y, -5.12, 5.12)
        
        # Check if neighbor is best so far
        DE = rastrigin(x, y, A) - rastrigin(neighbor_x, neighbor_y, A)
        
        # if the new solution is better, accept it
        if DE < -t:
            x = neighbor_x
            y = neighbor_y
            change_count=0
            
        if change_count==200:
            break
        
        z=rastrigin(x, y, A)
        print("Iteration ",j," of threshold ", t,": x =",x," y =",y," z =",z)
        j+=1
        
print("Final Answer: x = ", x, " y = ", y, " z = ", rastrigin(x, y, A), " with a total of ",j-1," iterations")
