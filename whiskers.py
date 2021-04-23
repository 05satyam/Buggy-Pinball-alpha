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

algorithms = ['\\variantTR3', '\\SA', '\\TA']
# functions = ['\\rastrigin', '\\ackley', '\\sphere', '\\easom', '\\shubert', '\\schwefel', '\\holdertable', '\\eggholder', '\\dropwave', '\\langermann']
# funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann']
functions = ['\\dropwave', '\\langermann']
funcs = ['dropwave', 'langermann']

k=0
for f_name in functions:
    all_data = []
    for j in range(0, 8):
        for a in algorithms:
            string = r"..\Results"+f_name+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls"
            if (path.exists("..\Results"+f_name+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls")):
                xls = pd.ExcelFile(string)
            else:
                continue
            sheetX = xls.parse(0)
            
            data = []
            data.append(float(sheetX.columns[0]))
            for i in range(0,99):
                data.append(float(sheetX.values[i][0]))
            all_data.append(data)    
        plt.boxplot(all_data, 0, '') 
    plt.title(funcs[k]+' function')
    plt.ylabel('Values')
    if (funcs[k]=='rastrigin'):
        plt.xlabel('0.05 secs         0.1 secs       0.5 secs       1 sec        2 secs        3 secs')
    elif (funcs[k]=='ackley'):
        plt.xlabel('0.05 secs         0.1 secs       0.5 secs       1 sec        2 secs        3.5 secs')
    elif (funcs[k]=='dropwave'):
        plt.xlabel('0.025 secs        0.06 secs      0.13 secs      0.35 secs    0.75 secs     1 sec')
    elif (funcs[k]=='sphere'):
        plt.xlabel('0.00015 secs       0.0015 secs     0.015 secs     0.15 secs      1.5 secs')
    elif (funcs[k]=='easom'):
        plt.xlabel('0.0015 secs        0.015 secs      0.15 secs      1 sec          2 secs')
    elif (funcs[k]=='shubert'):
        plt.xlabel('0.1 secs           0.25 secs       0.5 secs       1 sec          2 secs')
    elif (funcs[k]=='schwefel'):
        plt.xlabel('0.5 secs           1 sec           2 secs         3 secs         4.1 secs')
    elif (funcs[k]=='holdertable'):
        plt.xlabel('0.01 secs          0.05 secs       0.1 secs       0.5 secs       1 sec')
    elif (funcs[k]=='eggholder'):
        plt.xlabel('5 secs              10 sec              31 secs             60 secs')
    elif (funcs[k]=='langermann'):
        plt.xlabel('0.05         0.1         0.25         0.5          1         2          3.35         11.5')
        
    
    if (funcs[k]=='langermann'):
        plt.xticks(np.arange(25), ['','BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA'])
    elif (funcs[k]=='rastrigin' or funcs[k]=='ackley' or funcs[k]=='dropwave'):
        plt.xticks(np.arange(19), ['','BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA'])
    elif (funcs[k]=='eggholder'):
        plt.xticks(np.arange(13), ['','BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA'])
    else:
        plt.xticks(np.arange(16), ['','BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA', 'BP', 'SA', 'TA'])
        
    plt.show()
    k+=1