import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *
A = 10            # rastrigin factor
b = 0.00001       # slow cooling variable
x = random.uniform(-5.12, 5.12)         # initial solutions
y = random.uniform(-5.12, 5.12)         #
T = 10000 # starting temperature
final_T = .1   # final temperature
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

z=rastrigin(x, y, A)
print("Initial values: x =",x," y =",y," z =",z)
i=0
while T > final_T:
    # get random neighbor
    neighbor_x=get_neighbors(x, -5.12, 5.12)
    neighbor_y=get_neighbors(y, -5.12, 5.12)

    DE = z - rastrigin(neighbor_x, neighbor_y, A)
    
    if DE > 0:   # if the new solution is better, accept it
        x = neighbor_x
        y = neighbor_y
    else:   # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        if random.uniform(0, 1) < math.exp(DE / T):
            x = neighbor_x
            y = neighbor_y
     
    z=rastrigin(x, y, A)
    #print("Iteration ",i,": x =",x," y =",y," z =",z)
    # decrement the temperature via slow cooling
    T=T/(1+b*T)
    i+=1

print("Final Answer: x = ", x, " y = ", y, " z = ", rastrigin(x, y, A), " i = ", i)