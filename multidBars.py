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

def autolabel(rects, xpos='center'):
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

funcs = ['rastrigin', 'ackley', 'sphere', 'schwefel'] #multi-D

xls = pd.ExcelFile("convergence_multi.xls")
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
            if isinstance(BP_res[i], int):
                results0.append(BP_res[i])
                results1.append(SA_res[i])
                results2.append(TA_res[i])
                results3.append(PSO_res[i])
        else:
            if f!=BP_res[i]:
                i+=2
        i+=1
    fig, ax = plt.subplots()
    bp_ci = []
    sa_ci = []
    ta_ci = []
    pso_ci = []
    for j in range(0, len(results0)):
        bp_ci.append(196*math.sqrt((results0[j]/100)*(1-results0[j]/100)/100))
        sa_ci.append(196*math.sqrt((results1[j]/100)*(1-results1[j]/100)/100))
        ta_ci.append(196*math.sqrt((results2[j]/100)*(1-results2[j]/100)/100))
        pso_ci.append(196*math.sqrt((results3[j]/100)*(1-results3[j]/100)/100))
    
    rects1=ax.bar(X - 0.3, results0, color = 'b', width = 0.2, yerr=bp_ci, capsize=4, label='Buggy Pinball')
    rects2=ax.bar(X - 0.1, results1, color = 'c', width = 0.2, yerr=sa_ci, capsize=4, label='Simulated Annealing')
    rects3=ax.bar(X + 0.1, results2, color = 'g', width = 0.2, yerr=ta_ci, capsize=4, label='Threshold Accepting')
    rects4=ax.bar(X + 0.3, results3, color = 'r', width = 0.2, yerr=pso_ci, capsize=4, label='Particle Swarm Optimization')
    ax.set_xticklabels(['', '2D(1 s)', '3D(5 s)', '4D(1 m)', '5D(5 m)', '6D(20 m)'])
    autolabel(rects1, "left")
    autolabel(rects2, "left")
    autolabel(rects3, "left")
    autolabel(rects4, "left")
    plt.legend(loc=6)
    plt.ylim([0, 115])
    plt.title(f+' function')
    plt.ylabel('Accuracy(%)')
    #             plt.ylabel('Mean Absolute Error')
                
    fig.tight_layout()
    plt.show()