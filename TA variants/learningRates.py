import math

# returns the selected value of the learning rate
def simpleLR(value):
    return value

# scalable learning rate takes the initial value and reduces it based on the given rate as the iterations are increasing
# example:
# learning rate=0.5
# reduction = 10% or 0.1
# rate = 10 iterations
# 
# On the first 10 iterations learning rate will be 0.5. On the next 10 it will  
# be reduced by 0.1*1*0.5=0.05 and it will be 0.45 and so on.
def scalableLR(value, iteration, reduction, rate):
    step = int(iteration/rate)
    return value - step*reduction*value

# cosine learning rate returns the value of the cosine decreasing learning rate  on
# the given iteration based on the given period (maximum number of iterations).
# t is the iteration number and T is the period
def cosineLR(value, t, T):
    return value*(1 + math.cos(math.pi*t / T)) / 2

# periodical learning rate is consisted of a number of cosine cycles on a given period
# t is the iteration number, T is the period and M are the cycles
def periodicalLR(value, t, T, M):
    return value*(1 + math.cos(math.pi*((t - 1) % (int(T/M) + 1)) / (int(T/M) + 1))) / 2