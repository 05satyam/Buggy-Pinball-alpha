import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *

A=10

def simulated_annealing(x, y):
    initial_temp = 90
    final_temp = .1
    alpha = 0.01
    
    # Start by initializing the current state with the initial state
    solution_x = x
    solution_y = y
    
    i=0
    while initial_temp > final_temp:
        z=rastrigin(solution_x, solution_y, A)
        print("Iteration ",i,": x =",solution_x," y =",solution_y," z =",z)
        
        rand_x = random.randint(0,2)
        rand_y = random.randint(0,2)
        if solution_x<=-5.12 or rand_x==0:
            neighbor_x=solution_x+0.1
        elif solution_x>=5.12 or rand_x==1:
            neighbor_x=solution_x-0.1
        
        if solution_y<=-5.12 or rand_y==0:
            neighbor_y=solution_y+0.1
        elif solution_y>=5.12 or rand_y==1:
            neighbor_y=solution_y-0.1

        # Check if neighbor is best so far
        cost_diff = z - rastrigin(neighbor_x, neighbor_y, A)
        
        # if the new solution is better, accept it
        if cost_diff > 0:
            solution_x = neighbor_x
            solution_y = neighbor_y
        # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        else:
            if random.uniform(0, 1) < math.exp(cost_diff / initial_temp):
                solution_x = neighbor_x
                solution_y = neighbor_y
            
        # decrement the temperature
        initial_temp-=alpha
        i+=1

    return solution_x, solution_y

solution = simulated_annealing(-5.12, -5.12)
print("Answer is: ", solution[0], ", ",solution[1])