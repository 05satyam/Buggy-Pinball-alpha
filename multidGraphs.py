import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import math
from functions import *
import pandas as pd
import xlrd
from os import path
import xlwt 
from xlwt import Workbook
import matplotlib.patches as mpatches

funcs = ['rastrigin', 'ackley', 'sphere', 'schwefel'] #multi-D

xls = pd.ExcelFile("convergence_MAE_multi.xls")
lenOfExcel = 59
sheetX = xls.parse(0)

BP_res = []
BP_res.append(sheetX.columns[0])
SA_res = []
SA_res.append(sheetX.columns[0])
TA_res = []
TA_res.append(sheetX.columns[0])
PSO_res = []
PSO_res.append(sheetX.columns[0])
for i in range(0,lenOfExcel):
    BP_res.append(sheetX.values[i][0])
    SA_res.append(sheetX.values[i][1])
    TA_res.append(sheetX.values[i][2])
    PSO_res.append(sheetX.values[i][3])

X = np.arange(5)
for f in funcs:
    results0=[]
    results1=[]
    results2=[]
    results3=[]
    i=0
    while i<=lenOfExcel:
        if not BP_res[i] in funcs:
            if isinstance(BP_res[i], float):
                results0.append(BP_res[i])
                results1.append(SA_res[i])
                results2.append(TA_res[i])
                results3.append(PSO_res[i])
        else:
            if f!=BP_res[i]:
                i+=2
        i+=1
    
    for j in range(0, len(results0)):
        plt.plot(X[j], results0[j], markerfacecolor='b', markeredgecolor='b', marker='o', markersize=5)
                    
        plt.plot(X[j], results1[j], markerfacecolor='c', markeredgecolor='c', marker='o', markersize=5)
                    
        plt.plot(X[j], results2[j], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
                    
        plt.plot(X[j], results3[j], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    
    plt.xticks(X, ['2D(1 s)', '3D(5 s)', '4D(1 m)', '5D(5 m)', '6D(20 m)'])
    
    blue_patch = mpatches.Patch(color='b', label='Buggy Pinball')
    cyan_patch = mpatches.Patch(color='c', label='Simulated Annealing')
    green_patch = mpatches.Patch(color='g', label='Threshold Accepting')
    red_patch = mpatches.Patch(color='r', label='Particle Swarm Optimization')
    
    plt.legend(loc=0, handles=[blue_patch, cyan_patch, green_patch, red_patch])
    
    plt.xlim([-.5, 4.5])
                 
    plt.title(f+' function')
    plt.ylabel('Mean Absolute Error')
    plt.show()
