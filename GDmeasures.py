import numpy as np
import matplotlib.pyplot as plt
from functions import *
from learningRates import *
import random
import time

times=[]
a = simpleLR(0.2)
#gama=0.9
gama1=0.8
gama2=0.999
e=1e-6 #standard value to avoid dividing with 0
algo_trials=100000
low=-10
high=10
for exp in range(0, algo_trials):
    start_time=time.time()
    #algorithm
    x = random.uniform(low, high) # initial solutions
    y = random.uniform(low, high)
    z = booth(x, y)
    #print("Initial guess: x =",x," y =",y," z =",z)
    #i=1
    Dx=0 #difference between last two variable values
    Dy=0
    Gx=0 #the matrix of the derirative
    Gy=0
    limits=False
    while z>0.000001: #z>-1.913222 or z<-1.913223:
        Dx = gama1*Dx + (1-gama1)*booth_dx(x, y)
        Dy = gama1*Dy + (1-gama1)*booth_dy(x, y)
        Gx = gama2*Gx + (1-gama2)*booth_dx(x, y)**2
        Gy = gama2*Gy + (1-gama2)*booth_dy(x, y)**2
        x = x - a*Dx/(np.sqrt(Gx)+e)
        y = y - a*Dy/(np.sqrt(Gy)+e)
        z = booth(x, y)
        #print("Iteration ",i,": x =",x," y =",y," z =",z)
        #print("Learning rate is ", a)
        
        if x<low or x>high or y<low or y>high:
            print("Boundaries have been exceeded. Results not valid. x=",x," y=",y)
            limits=True
            break
        
        #i+=1
    
    if limits==False:
        total_time=time.time()-start_time
        times.append(total_time)
    print(exp)    
time_average=sum(times)/len(times)
print("Algorithm needed an average of ", time_average, " seconds to reach global minimum. Times stuck to local minimum.",algo_trials-len(times))
