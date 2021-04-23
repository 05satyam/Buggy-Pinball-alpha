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
                 
wb = Workbook() 
                  
# sheet1 = wb.add_sheet('results_RMSD')
# sheet1 = wb.add_sheet('results_MAE')
sheet1 = wb.add_sheet('times')

algorithms = ['\\variantTR3', '\\SA', '\\TA']
functions = ['\\rastrigin', '\\ackley', '\\sphere', '\\easom', '\\shubert', '\\schwefel', '\\holdertable', '\\eggholder', '\\dropwave', '\\langermann']
funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann']
f_minimum = [0, 0, 0, -1, -186.7309, 0, -19.2085, -959.6407, -1, -4.155514681353426]

for a in algorithms:
    k=0
    l=0
    for f_name in functions:
        for j in range(0, 8):
            string = r"..\Results"+f_name+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls"
            if (path.exists("..\Results"+f_name+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls")):
                xls = pd.ExcelFile(string)
            else:
                continue
            sheetX = xls.parse(0)
            
            data = []
            data.append(float(sheetX.columns[1]))
            for i in range(0,99):
                data.append(float(sheetX.values[i][1]))
                
            resss = 0
            for i in data:
#                 resss += (f_minimum[k] - i)**2    #RMSD
#                 resss += abs(f_minimum[k] - i)  #MAE
                resss += i                      #times
#             results_average = math.sqrt(resss/100)#for RMSD
            results_average = resss/100
            if j==0:
                if a==algorithms[0]:
                    sheet1.write(l, 0, funcs[k])
                    l+=1
                    sheet1.write(l, 0, algorithms[0])
                    sheet1.write(l, 1, algorithms[1])
                    sheet1.write(l, 2, algorithms[2])
                    l+=1
                else:
                    l+=2
                
            if a==algorithms[0]:
                sheet1.write(l, 0, results_average)
            elif a==algorithms[1]:
                sheet1.write(l, 1, results_average)
            else:
                sheet1.write(l, 2, results_average)
                     
#             wb.save('results_RMSD.xls')
#             wb.save('results_MAE.xls')
            wb.save('times.xls')
            print("Algorithm "+a+" Function "+funcs[k]+" for "+str(j)+" has "+str(results_average))
            l+=1
        k+=1
        
        
        
        