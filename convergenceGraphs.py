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

funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann'] #3D
# funcs = ['rastrigin', 'ackley', 'sphere', 'schwefel'] #multi-D

xls = pd.ExcelFile("convergence.xls")
lenOfExcel = 89    #3D
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
    
xls = pd.ExcelFile("times.xls")
sheetX = xls.parse(0)

BP_times = []
BP_times.append(sheetX.columns[0])
SA_times = []
SA_times.append(sheetX.columns[0])
TA_times = []
TA_times.append(sheetX.columns[0])
PSO_times = []
PSO_times.append(sheetX.columns[0])
for i in range(0,lenOfExcel):
    BP_times.append(sheetX.values[i][0])
    SA_times.append(sheetX.values[i][1])
    TA_times.append(sheetX.values[i][2])
    PSO_times.append(sheetX.values[i][3])
i=0
k=0
while i<=lenOfExcel:
    if BP_res[i] in funcs:
        if i!=0:
            for j in range(0, len(times0)):
                uci = results0[j]+1.96*math.sqrt(results0[j]*(1-results0[j])/100)
                lci = results0[j]-1.96*math.sqrt(results0[j]*(1-results0[j])/100)
                boxplot = [uci, results0[j], lci]
                timeboxplot = [times0[j], times0[j], times0[j]]
                plt.plot(timeboxplot, boxplot, 'b')
                plt.plot(times0[j], uci, markerfacecolor='b', markeredgecolor='b', marker='_', markersize=5)
                plt.plot(times0[j], results0[j], markerfacecolor='b', markeredgecolor='b', marker='o', markersize=5)
                plt.plot(times0[j], lci, markerfacecolor='b', markeredgecolor='b', marker='_', markersize=5)                
                
                uci = results1[j]+1.96*math.sqrt(results1[j]*(1-results1[j])/100)
                lci = results1[j]-1.96*math.sqrt(results1[j]*(1-results1[j])/100)
                boxplot = [uci, results1[j], lci]
                timeboxplot = [times1[j], times1[j], times1[j]]
                plt.plot(timeboxplot, boxplot, 'c')
                plt.plot(times1[j], uci, markerfacecolor='c', markeredgecolor='c', marker='_', markersize=5)
                plt.plot(times1[j], results1[j], markerfacecolor='c', markeredgecolor='c', marker='o', markersize=5)
                plt.plot(times1[j], lci, markerfacecolor='c', markeredgecolor='c', marker='_', markersize=5)
                
                uci = results2[j]+1.96*math.sqrt(results2[j]*(1-results2[j])/100)
                lci = results2[j]-1.96*math.sqrt(results2[j]*(1-results2[j])/100)
                boxplot = [uci, results2[j], lci]
                timeboxplot = [times2[j], times2[j], times2[j]]
                plt.plot(timeboxplot, boxplot, 'g')
                plt.plot(times2[j], uci, markerfacecolor='g', markeredgecolor='g', marker='_', markersize=5)
                plt.plot(times2[j], results2[j], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
                plt.plot(times2[j], lci, markerfacecolor='g', markeredgecolor='g', marker='_', markersize=5)
                
                uci = results3[j]+1.96*math.sqrt(results3[j]*(1-results3[j])/100)
                lci = results3[j]-1.96*math.sqrt(results3[j]*(1-results3[j])/100)
                boxplot = [uci, results3[j], lci]
                timeboxplot = [times3[j], times3[j], times3[j]]
                plt.plot(timeboxplot, boxplot, 'r')
                plt.plot(times3[j], uci, markerfacecolor='r', markeredgecolor='r', marker='_', markersize=5)
                plt.plot(times3[j], results3[j], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
                plt.plot(times3[j], lci, markerfacecolor='r', markeredgecolor='r', marker='_', markersize=5)
            
            blue_patch = mpatches.Patch(color='b', label='Buggy Pinball')
            cyan_patch = mpatches.Patch(color='c', label='Simulated Annealing')
            green_patch = mpatches.Patch(color='g', label='Threshold Accepting')
            red_patch = mpatches.Patch(color='r', label='Particle Swarm Optimization')
             
            plt.legend(loc=4, handles=[blue_patch, cyan_patch, green_patch, red_patch])
            plt.ylim([-.05, 1.05]) 
            plt.title(funcs[k]+' function')
            plt.xlabel('time (seconds)')
            plt.ylabel('Convergence Percentage')
#             plt.ylabel('Mean Absolute Error')
            k+=1
            plt.show()
        times0 = []
        results0 = []
        times1 = []
        results1 = []
        times2 = []
        results2 = []
        times3 = []
        results3 = []
    else:
        if not BP_res[i]=='\\variantTR4':
            times0.append(BP_times[i])
            results0.append(BP_res[i]/100)
            times1.append(SA_times[i])
            results1.append(SA_res[i]/100)
            times2.append(TA_times[i])
            results2.append(TA_res[i]/100)
            times3.append(PSO_times[i])
            results3.append(PSO_res[i]/100)
    i+=1
for j in range(0, len(times0)):
    uci = results0[j]+1.96*math.sqrt(results0[j]*(1-results0[j])/100)
    lci = results0[j]-1.96*math.sqrt(results0[j]*(1-results0[j])/100)
    boxplot = [uci, results0[j], lci]
    timeboxplot = [times0[j], times0[j], times0[j]]
    plt.plot(timeboxplot, boxplot, 'b')
    plt.plot(times0[j], uci, markerfacecolor='b', markeredgecolor='b', marker='_', markersize=5)
    plt.plot(times0[j], results0[j], markerfacecolor='b', markeredgecolor='b', marker='o', markersize=5)
    plt.plot(times0[j], lci, markerfacecolor='b', markeredgecolor='b', marker='_', markersize=5)
                
    uci = results1[j]+1.96*math.sqrt(results1[j]*(1-results1[j])/100)
    lci = results1[j]-1.96*math.sqrt(results1[j]*(1-results1[j])/100)
    boxplot = [uci, results1[j], lci]
    timeboxplot = [times1[j], times1[j], times1[j]]
    plt.plot(timeboxplot, boxplot, 'c')
    plt.plot(times1[j], uci, markerfacecolor='c', markeredgecolor='c', marker='_', markersize=5)
    plt.plot(times1[j], results1[j], markerfacecolor='c', markeredgecolor='c', marker='o', markersize=5)
    plt.plot(times1[j], lci, markerfacecolor='c', markeredgecolor='c', marker='_', markersize=5)
                
    uci = results2[j]+1.96*math.sqrt(results2[j]*(1-results2[j])/100)
    lci = results2[j]-1.96*math.sqrt(results2[j]*(1-results2[j])/100)
    boxplot = [uci, results2[j], lci]
    timeboxplot = [times2[j], times2[j], times2[j]]
    plt.plot(timeboxplot, boxplot, 'g')
    plt.plot(times2[j], uci, markerfacecolor='g', markeredgecolor='g', marker='_', markersize=5)
    plt.plot(times2[j], results2[j], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
    plt.plot(times2[j], lci, markerfacecolor='g', markeredgecolor='g', marker='_', markersize=5)
                
    uci = results3[j]+1.96*math.sqrt(results3[j]*(1-results3[j])/100)
    lci = results3[j]-1.96*math.sqrt(results3[j]*(1-results3[j])/100)
    boxplot = [uci, results3[j], lci]
    timeboxplot = [times3[j], times3[j], times3[j]]
    plt.plot(timeboxplot, boxplot, 'r')
    plt.plot(times3[j], uci, markerfacecolor='r', markeredgecolor='r', marker='_', markersize=5)
    plt.plot(times3[j], results3[j], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    plt.plot(times3[j], lci, markerfacecolor='r', markeredgecolor='r', marker='_', markersize=5)

blue_patch = mpatches.Patch(color='b', label='Buggy Pinball')
cyan_patch = mpatches.Patch(color='c', label='Simulated Annealing')
green_patch = mpatches.Patch(color='g', label='Threshold Accepting')
red_patch = mpatches.Patch(color='r', label='Particle Swarm Optimization')
             
plt.legend(loc=4, handles=[blue_patch, cyan_patch, green_patch, red_patch])
             
plt.legend(loc=4)
plt.ylim([-.05, 1.05])
             
plt.title(funcs[k]+' function')
plt.xlabel('time (seconds)')
plt.ylabel('Convergence Percentage')
# plt.ylabel('Mean Absolute Error')
plt.show()
