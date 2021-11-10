import random
import math  # cos() for Rastrigin
import copy  # array-copying convenience
import sys  # max float
from functions import *
import time
import xlwt 
from xlwt import Workbook
 
# whale class
class whale:
    def __init__(self, fitness, dim, minx, maxx, seed):
#         self.rnd = random.Random(seed)
        self.position = [random.uniform(minx, maxx) for i in range(dim)]
        self.fitness = fitness(self.position)  # curr fitness
 
# whale optimization algorithm(WOA)
def woa(fitness, max_iter, n, dim, minx, maxx):
    rnd = random.Random(0)
 
    # create n random whales
    whalePopulation = [whale(fitness, dim, minx, maxx, i) for i in range(n)]
 
    # compute the value of best_position and best_fitness in the whale Population
    Xbest = [0.0 for i in range(dim)]
    Fbest = sys.float_info.max
 
    for i in range(n):  # check each whale
        if whalePopulation[i].fitness < Fbest:
            Fbest = whalePopulation[i].fitness
            Xbest = copy.copy(whalePopulation[i].position)
 
    # main loop of woa
    Iter = 0
    while Iter < max_iter:
 
        # after every 10 iterations
        # print iteration number and best fitness value so far
#         if Iter % 10 == 0 and Iter > 1:
#             print("Iter = " + str(Iter) + " best fitness = %.3f" % Fbest)
 
        # linearly decreased from 2 to 0
        a = 2 * (1 - Iter / max_iter)
        a2=-1+Iter*((-1)/max_iter)
 
        for i in range(n):
            A = 2 * a * rnd.random() - a
            C = 2 * rnd.random()
            b = 1
            l = (a2-1)*rnd.random()+1;
            p = rnd.random()
 
            D = [0.0 for i in range(dim)]
            D1 = [0.0 for i in range(dim)]
            Xnew = [0.0 for i in range(dim)]
            Xrand = [0.0 for i in range(dim)]
            if p < 0.5:
                if abs(A) > 1:
                    for j in range(dim):
                        D[j] = abs(C * Xbest[j] - whalePopulation[i].position[j])
                        Xnew[j] = Xbest[j] - A * D[j]
                else:
                    p = random.randint(0, n - 1)
                    while (p == i):
                        p = random.randint(0, n - 1)
 
                    Xrand = whalePopulation[p].position
 
                    for j in range(dim):
                        D[j] = abs(C * Xrand[j] - whalePopulation[i].position[j])
                        Xnew[j] = Xrand[j] - A * D[j]
            else:
                for j in range(dim):
                    D1[j] = abs(Xbest[j] - whalePopulation[i].position[j])
                    Xnew[j] = D1[j] * math.exp(b * l) * math.cos(2 * math.pi * l) + Xbest[j]
 
            for j in range(dim):
                whalePopulation[i].position[j] = Xnew[j]
 
        for i in range(n):
            # if Xnew < minx OR Xnew > maxx
            # then clip it
            for j in range(dim):
                whalePopulation[i].position[j] = max(whalePopulation[i].position[j], minx)
                whalePopulation[i].position[j] = min(whalePopulation[i].position[j], maxx)
 
            whalePopulation[i].fitness = fitness(whalePopulation[i].position)
 
            if (whalePopulation[i].fitness < Fbest):
                Xbest = copy.copy(whalePopulation[i].position)
                Fbest = whalePopulation[i].fitness
 
 
        Iter += 1
    # end-while
 
    # returning the best solution
    return Xbest
# ----------------------------
dim = 2
# low = [-5.12, -5.12, -512, -500, -10,  -10, -10, -5, -2, 0]
# up = [5.12, 5.12, 512, 500, 10,  10, 10, 5, 2, 10]
# num_whales = [100, 50, 800, 800, 50, 50, 50, 50, 25, 600]
# rounds = [7300, 14500, 900, 920, 13500, 15000, 11000, 13700, 33000, 600]
# fitnessTable = [rastrigin, dropwave, eggholder, schwefel, easom, holdertable, shubert, ackley, sphere, langermann]
######################################################
###########Multi-D Measures###########################
# rastrigin: 2D: 200-700  4D: 400-11400 5D: 400-52000  6D: 400-190000
# schwefel:  2D: 200-600  4D: 400-8000  5D: 400-31000  6D: 600-66000
# ackley:    2D: 200-620  4D: 300-15000 5D: 300-56000  6D: 300-220000
# sphere:    2D: 10-13000 4D: 50-79000  5D: 100-140000 6D: 100-465000
# dim = [1, 3, 4, 5]
# low = [-5.12, -500, -5, -2]
# up = [5.12, 500, 5, 2]
# num_whales = [200, 400, 400, 400]
# rounds = [550, 11300, 48400, 151000]
# fitnessTable = [rastrigin, schwefel, ackley, sphere]

num_of_iter=100
for k in range(len(fitnessTable)):
#     for j in range(len(dim)):
#     for j in range(len(num_whales)):
    fitness=fitnessTable[k]
    exp=0
    times=[]
    results=[]
    while exp<num_of_iter:
        start_time=time.process_time()
        
        best_position = woa(fitness, rounds[k], num_whales[k], dim, low[k], up[k])
        err = fitness(best_position)
        
        results.append(err)
#         print(exp)
        total_time=time.process_time()-start_time
        times.append(total_time)
        exp+=1
    #     print("fitness of best solution = %f" % err)
    results_average=sum(results)/len(results) #get an average
    time_average=sum(times)/len(times)
#         print("Function: "+str(fitness.__name__)+" particles: "+str(num_whales[j])+" dimension:", dim+1," result:", results_average," time: ",time_average)
    print(num_of_iter,"iterations of",fitness.__name__,"function on",num_whales[k],"whales takes ",time_average," secs and err ",results_average)
    wb = Workbook() 
                
    sheet1 = wb.add_sheet('file')
    i=0
    for wr in results:
        sheet1.write(i, 0, wr)
        sheet1.write(i, 1, times[i])
        i+=1
    wb.save('..\Results\WO_'+str(fitness.__name__)+'_'+str(dim+1)+'_secs_7.xls')
#         wb.save('WO_'+str(fitness.__name__)+'_'+str(dim+1)+'_secs.xls')
    print("All saved")


 