import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *
A = 10      # rastrigin factor
b = 0.001   # slow cooling variable
x = -5.12   # initial solutions
y = -5.12   #
init_T = 1       # initial threshold
rounds = 100 # number of parts that the threshold sequence will contain
steps = 1000 # iterations that will occur within every threshold value

# create the threshold sequence
T = np.linspace(init_T, 0, rounds)

z=rastrigin(x, y, A)
print("Initial values: x =",x," y =",y," z =",z)
for t in T:
    for i in range(1, steps):
        # get random neighbor
        neighbor_x=random.uniform(-5.12, 5.12)
        neighbor_y=random.uniform(-5.12, 5.12)
    
        # Check if neighbor is best so far
        cost_diff = rastrigin(x, y, A) - rastrigin(neighbor_x, neighbor_y, A)
        
        # if the new solution is better, accept it
        if cost_diff > -t:
            x = neighbor_x
            y = neighbor_y
        
        z=rastrigin(x, y, A)
        print("Iteration ",i," of threshold ", t,": x =",x," y =",y," z =",z)
        
print("Final Answer: x = ", x, " y = ", y, " z = ", rastrigin(x, y, A))