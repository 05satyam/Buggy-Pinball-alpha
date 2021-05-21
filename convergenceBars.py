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

funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann'] #3D
# funcs = ['rastrigin', 'ackley', 'sphere', 'schwefel'] #multi-D

xls = pd.ExcelFile("convergence_MAE.xls")
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

i=0
k=0
X = np.arange(7)
while i<=lenOfExcel:
    if BP_res[i] in funcs:
        if i!=0:
            fig, ax = plt.subplots()
            bp_ci = []
            sa_ci = []
            ta_ci = []
            pso_ci = []
            for j in range(0, len(results0)):
                bp_ci.append(1.96*math.sqrt((results0[j])*(1-results0[j])/100))
                sa_ci.append(1.96*math.sqrt((results1[j])*(1-results1[j])/100))
                ta_ci.append(1.96*math.sqrt((results2[j])*(1-results2[j])/100))
                pso_ci.append(1.96*math.sqrt((results3[j])*(1-results3[j])/100))
            
            rects1=ax.bar(X - 0.3, results0, color = 'b', width = 0.2, yerr=bp_ci, capsize=4, label='Buggy Pinball')
            rects2=ax.bar(X - 0.1, results1, color = 'c', width = 0.2, yerr=sa_ci, capsize=4, label='Simulated Annealing')
            rects3=ax.bar(X + 0.1, results2, color = 'g', width = 0.2, yerr=ta_ci, capsize=4, label='Threshold Accepting')
            rects4=ax.bar(X + 0.3, results3, color = 'r', width = 0.2, yerr=pso_ci, capsize=4, label='Particle Swarm Optimization')
                        
            ax.set_xticklabels(['','0.05', '0.1', '0.2', '0.5', '1', '2', '5'])
            autolabel(rects1, "left")
            autolabel(rects2, "left")
            autolabel(rects3, "left")
            autolabel(rects4, "left")
            plt.legend(loc=4)
            plt.ylim([0, 1.15])
            plt.title(funcs[k]+' function')
            plt.xlabel('time (seconds)')
            plt.ylabel('Convergence Percentage')
#             plt.ylabel('Mean Absolute Error')
            k+=1
            
            fig.tight_layout()
            plt.show()
        results0 = []
        results1 = []
        results2 = []
        results3 = []
    else:
        if not BP_res[i]=='\\variantTR4':
            results0.append(BP_res[i]/100)
            results1.append(SA_res[i]/100)
            results2.append(TA_res[i]/100)
            results3.append(PSO_res[i]/100)
    i+=1
fig, ax = plt.subplots()
bp_ci = []
sa_ci = []
ta_ci = []
pso_ci = []
for j in range(0, len(results0)):
    bp_ci.append(1.96*math.sqrt((results0[j])*(1-results0[j])/100))
    sa_ci.append(1.96*math.sqrt((results1[j])*(1-results1[j])/100))
    ta_ci.append(1.96*math.sqrt((results2[j])*(1-results2[j])/100))
    pso_ci.append(1.96*math.sqrt((results3[j])*(1-results3[j])/100))
            
rects1=ax.bar(X - 0.3, results0, color = 'b', width = 0.2, yerr=bp_ci, capsize=4, label='Buggy Pinball')
rects2=ax.bar(X - 0.1, results1, color = 'c', width = 0.2, yerr=sa_ci, capsize=4, label='Simulated Annealing')
rects3=ax.bar(X + 0.1, results2, color = 'g', width = 0.2, yerr=ta_ci, capsize=4, label='Threshold Accepting')
rects4=ax.bar(X + 0.3, results3, color = 'r', width = 0.2, yerr=pso_ci, capsize=4, label='Particle Swarm Optimization')
                        
ax.set_xticklabels(['','0.05', '0.1', '0.2', '0.5', '1', '2', '5'])
autolabel(rects1, "left")
autolabel(rects2, "left")
autolabel(rects3, "left")
autolabel(rects4, "left")
plt.legend(loc=1)
plt.ylim([0, 1.15])
plt.title(funcs[k]+' function')
plt.xlabel('time (seconds)')
plt.ylabel('Convergence Percentage')
# plt.ylabel('Mean Absolute Error')
plt.show()
