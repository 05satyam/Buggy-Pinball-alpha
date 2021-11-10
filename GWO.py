# python implementation of Grey wolf optimization (GWO)
# minimizing rastrigin and sphere function
import random
import math    # cos() for Rastrigin
import copy    # array-copying convenience
import sys     # max float
from functions import *
import time
import xlwt 
from xlwt import Workbook
 
# wolf class
class wolf:
  def __init__(self, fitness, dim, minx, maxx, seed):
#     self.rnd = random.Random(seed)
    self.position = [random.uniform(minx, maxx) for i in range(dim)]
    self.fitness = fitness(self.position) # curr fitness
    
# grey wolf optimization (GWO)
def gwo(fitness, max_iter, n, dim, minx, maxx):
    # create n random wolves
    population = [ wolf(fitness, dim, minx, maxx, i) for i in range(n)]
    # On the basis of fitness values of wolves
    # sort the population in asc order
    population = sorted(population, key = lambda temp: temp.fitness)
    # best 3 solutions will be called as
    # alpha, beta and gama
    alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])
    # main loop of gwo
    Iter = 0
    while Iter < max_iter:
        # after every 10 iterations
        # print iteration number and best fitness value so far
#         if Iter % 10 == 0 and Iter > 1:
#             print(str(population[0].position)+"-"+str(population[1].position))
#             print("Iter = " + str(Iter) + " best fitness = %.3f" % alpha_wolf.fitness)
        # linearly decreased from 2 to 0
        a = 2*(1 - Iter/max_iter)
        # updating each population member with the help of best three members
        for i in range(n):            
            X1 = [0.0 for i in range(dim)]
            X2 = [0.0 for i in range(dim)]
            X3 = [0.0 for i in range(dim)]
            Xnew = [0.0 for i in range(dim)]
            j=0
            while j<dim:
                A1, A2, A3 = a * (2 * random.uniform(0,1) - 1), a * (2 * random.uniform(0,1) - 1), a * (2 * random.uniform(0,1) - 1)
                C1, C2, C3 = 2 * random.uniform(0,1), 2*random.uniform(0,1), 2*random.uniform(0,1)
                X1[j] = alpha_wolf.position[j] - A1 * abs(C1 * alpha_wolf.position[j] - population[i].position[j])
                X2[j] = beta_wolf.position[j] - A2 * abs(C2 *  beta_wolf.position[j] - population[i].position[j])
                X3[j] = gamma_wolf.position[j] - A3 * abs(C3 * gamma_wolf.position[j] - population[i].position[j])
                Xnew[j] = (X1[j] + X2[j] + X3[j])/3
                if (Xnew[j]>=minx and Xnew[j]<=maxx):
                    j+=1
#                 if (i==0):
#                     print("dim: "+str(j)+" X1: "+str(alpha_wolf.position[j])+" X2: "+str(A1)+" X3: "+str(C1))
#                     print("dim: "+str(j)+" X1: "+str(X1[j])+" X2: "+str(X2[j])+" X3: "+str(X3[j]))
#             
#             if (i==0):
#                 print(Xnew)
            # fitness calculation of new solution
            fnew = fitness(Xnew)
 
            # greedy selection
            if fnew < population[i].fitness:
                population[i].position = Xnew
                population[i].fitness = fnew
                 
        # On the basis of fitness values of wolves
        # sort the population in asc order
        population = sorted(population, key = lambda temp: temp.fitness)
 
        # best 3 solutions will be called as
        # alpha, beta and gama
        alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])
         
        Iter+= 1
    # end-while
 
    # returning the best solution
    return alpha_wolf.position
           
#----------------------------
# low=-5.12    #rastrigin
# up=5.12      #dropwave
# low=-512  #eggholder
# up=512
# low=-500  #schwefel
# up=500
# low=-10  #easom#holdertable
# up=10    #shubert
# low=-5  #ackley
# up=5
# low=-2  #sphere
# up=2
# low=0  #langermann
# up=10

num_of_iter=100

###########3D Measures###############################
dim = 2
# low = [-5.12, -5.12, -512, -500, -10,  -10, -10, -5, -2, 0]
# up = [5.12, 5.12, 512, 500, 10,  10, 10, 5, 2, 10]
# num_particles = [400, 400, 500, 200, 50, 100, 200, 300, 25, 100]
# rounds = [1400, 1400, 850, 2600, 11200, 4200, 2200, 1800, 23000, 3000]
# fitnessTable = [rastrigin, dropwave, eggholder, schwefel, easom, holdertable, shubert, ackley, sphere, langermann]
low = [0]
up = [10]
num_particles = [100]
rounds = [600]
fitnessTable = [langermann]
######################################################
###########Multi-D Measures###########################
# rastrigin: 2D: 200-600  4D: 400-9000  5D: 400-33300  6D: 400-110000
# schwefel:  2D: 200-600  4D: 400-8000  5D: 400-31000  6D: 600-66000
# ackley:    2D: 200-550  4D: 300-12000 5D: 300-43000  6D: 300-149000
# sphere:    2D: 10-13000 4D: 50-79000  5D: 100-140000 6D: 100-465000
# dim = [1, 3, 4, 5]
# low = [-5.12]
# up = [5.12]
# num_particles = [200, 400, 400, 400]
# rounds = [550, 11300, 48400, 151000]
# fitnessTable = [rastrigin, schwefel, ackley, sphere]
for k in range(len(fitnessTable)):
    fitness=fitnessTable[k]
#     for j in range(len(dim)):
#         for j in range(1):
    exp=0
    times=[]
    results=[]
    while exp<num_of_iter:
        start_time=time.process_time()
        
        best_position = gwo(fitness, rounds[k], num_particles[k], dim, low[k], up[k])
        err = fitness(best_position)
        
        results.append(err)
#         print(exp)
        total_time=time.process_time()-start_time
        times.append(total_time)
        exp+=1
    #     print("fitness of best solution = %f" % err)
    results_average=sum(results)/len(results) #get an average
    time_average=sum(times)/len(times)
#         print("Function: "+str(fitness.__name__)+" particles: "+str(num_particles[j])+" dimension:", dim," result:", results_average," time: ",time_average)
    print(num_of_iter,"iterations of",fitness.__name__,"function on",dim,"dimesions takes ",time_average," secs and err ",results_average)
    #--- END ----------------------------------------------------------------------+       
    wb = Workbook() 
               
    sheet1 = wb.add_sheet('file')
    i=0
    for wr in results:
        sheet1.write(i, 0, wr)
        sheet1.write(i, 1, times[i])
        i+=1
#     dimensions=dim[j]+1             
    wb.save('GWO_'+str(fitness.__name__)+'_'+str(dim)+'_secs_5.xls')
#     wb.close()
    print("All saved")