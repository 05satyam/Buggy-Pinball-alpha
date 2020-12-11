import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *
A = 10            # rastrigin factor
b = 0.001         # slow cooling variable
x = -5.12         # initial solutions
y = -5.12         #
initial_temp = 50 # starting temperature
final_temp = .1   # final temperature

z=rastrigin(x, y, A)
print("Initial values: x =",x," y =",y," z =",z)
i=0
while initial_temp > final_temp:
    # get random neighbor
    neighbor_x=random.uniform(-5.12, 5.12)
    neighbor_y=random.uniform(-5.12, 5.12)

    # Check if neighbor is best so far
    cost_diff = z - rastrigin(neighbor_x, neighbor_y, A)
    
    # if the new solution is better, accept it
    if cost_diff > 0:
        x = neighbor_x
        y = neighbor_y
    # if the new solution is not better, accept it with a probability of e^(-cost/temp)
    else:
        if random.uniform(0, 1) < math.exp(cost_diff / initial_temp):
            x = neighbor_x
            y = neighbor_y
    
    z=rastrigin(x, y, A)
    print("Iteration ",i,": x =",x," y =",y," z =",z)
    # decrement the temperature via slow cooling
    initial_temp=initial_temp/(1+b*initial_temp)
    i+=1

print("Final Answer: x = ", x, " y = ", y, " z = ", rastrigin(x, y, A))