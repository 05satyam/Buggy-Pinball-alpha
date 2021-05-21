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

algorithms = ['\\variantTR4', '\\SA', '\\TA', '\\PSO']
functions = ['\\rastrigin', '\\ackley', '\\sphere', '\\easom', '\\shubert', '\\schwefel', '\\holdertable', '\\eggholder', '\\dropwave', '\\langermann']
funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann']
# functions = ['\\dropwave', '\\langermann']
# funcs = ['dropwave', 'langermann']

k=0
for f_name in functions:
    all_data = []
    for j in range(1, 10):
        for a in algorithms:
            string = r"..\Results"+f_name+"\\3D"+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls"
            if (path.exists("..\Results"+f_name+"\\3D"+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls")):
                xls = pd.ExcelFile(string)
            else:
                continue
            sheetX = xls.parse(0)
            
            data = []
            data.append(float(sheetX.columns[0]))
            for i in range(0,99):
                data.append(float(sheetX.values[i][0]))
            all_data.append(data)    
        plt.boxplot(all_data) 
    plt.title(funcs[k]+' function')
    plt.ylabel('Values')
    plt.xlabel('0.05 seconds            0.1 seconds            0.2 seconds            0.5 seconds             1 second            2 seconds             5 seconds')    
    
    
    plt.xticks(np.arange(29), ['','BP', 'SA', 'TA', 'PSO','BP', 'SA', 'TA', 'PSO','BP', 'SA', 'TA', 'PSO','BP', 'SA', 'TA', 'PSO','BP', 'SA', 'TA', 'PSO','BP', 'SA', 'TA', 'PSO','BP', 'SA', 'TA', 'PSO'])
        
    plt.show()
    k+=1