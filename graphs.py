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

funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann']

xls = pd.ExcelFile("results_RMSD.xls")
lenOfExcel = 74
sheetX = xls.parse(0)

BP_res = []
BP_res.append(sheetX.columns[0])
SA_res = []
SA_res.append(sheetX.columns[0])
TA_res = []
TA_res.append(sheetX.columns[0])
for i in range(0,lenOfExcel):
    BP_res.append(sheetX.values[i][0])
    SA_res.append(sheetX.values[i][1])
    TA_res.append(sheetX.values[i][2])
    
xls = pd.ExcelFile("times.xls")
sheetX = xls.parse(0)

BP_times = []
BP_times.append(sheetX.columns[0])
SA_times = []
SA_times.append(sheetX.columns[0])
TA_times = []
TA_times.append(sheetX.columns[0])
for i in range(0,lenOfExcel):
    BP_times.append(sheetX.values[i][0])
    SA_times.append(sheetX.values[i][1])
    TA_times.append(sheetX.values[i][2])
i=0
k=0
while i<=lenOfExcel:
    if BP_res[i] in funcs:
        if i!=0:
            for j in range(0, len(times0)):
                plt.plot(times0[j], results0[j], markerfacecolor='b', markeredgecolor='b', marker='o', markersize=5)
                plt.plot(times1[j], results1[j], markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)
                plt.plot(times2[j], results2[j], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
            plt.plot(times0, results0, 'b', label='Buggy Pinball')
            plt.plot(times1, results1, 'orange', label='Simulated Annealing')
            plt.plot(times2, results2, 'g', label='Threshold Accepting')
             
            plt.legend()
             
            plt.title(funcs[k]+' function')
            plt.xlabel('time (seconds)')
#             plt.ylabel('Mean Absolute Error')
            plt.ylabel('Root-mean-square deviation')
            k+=1
            plt.show()
        times0 = []
        results0 = []
        times1 = []
        results1 = []
        times2 = []
        results2 = []
    else:
        if not BP_res[i]=='\\variantTR3':
            times0.append(BP_times[i])
            results0.append(BP_res[i])
            times1.append(SA_times[i])
            results1.append(SA_res[i])
            times2.append(TA_times[i])
            results2.append(TA_res[i])
    i+=1
for j in range(0, len(times0)):
    plt.plot(times0[j], results0[j], markerfacecolor='b', markeredgecolor='b', marker='o', markersize=5)
    plt.plot(times1[j], results1[j], markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)
    plt.plot(times2[j], results2[j], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
plt.plot(times0, results0, 'b', label='Buggy Pinball')
plt.plot(times1, results1, 'orange', label='Simulated Annealing')
plt.plot(times2, results2, 'g', label='Threshold Accepting')
             
plt.legend()
             
plt.title(funcs[k]+' function')
plt.xlabel('time (seconds)')
# plt.ylabel('Mean Absolute Error')
plt.ylabel('Root-mean-square deviation')
plt.show()
