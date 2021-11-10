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
wb2 = Workbook()
sheet1 = wb.add_sheet('times')
sheet2 = wb2.add_sheet('results_MAE')

algorithms = ['\\variantTR4', '\\SA', '\\TA', '\\PSO', '\\GWO', '\\WO']
functions = ['\\rastrigin', '\\ackley', '\\sphere', '\\easom', '\\shubert', '\\schwefel', '\\holdertable', '\\eggholder', '\\dropwave', '\\langermann']
funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann']
f_minimum = [0, 0, 0, -1, -186.7309, 0, -19.2085, -959.6407, -1, -4.15580929184779]
convergeLimit = [0.99, 2.5, 100, -0.1, -49, 118, -18.1, -895, -0.94, -4.127577]

for a in algorithms:
    k=0
    l=0
    for f_name in functions:
        for j in range(7, 8):
            string = r"..\Results"+f_name+"\\3D"+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls"
            if (path.exists("..\Results"+f_name+"\\3D"+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls")):
               xls = pd.ExcelFile(string)
            else:
                string = r"..\Results"+f_name+a+"_"+funcs[k]+"_3_secs_"+str(j)+".xls"
                xls = pd.ExcelFile(string)
            sheetX = xls.parse(0)
                
            data = []
            data.append(float(sheetX.columns[0]))
            for i in range(0,99):
                data.append(float(sheetX.values[i][0]))
                    
            percentage = 0
            resss = 0
            for i in data:
                if i<convergeLimit[k]:
                    percentage+=1
                        
                    resss += abs(f_minimum[k] - i)  #MAE
                
            if percentage==0:
                results_average="null"
            else:
                results_average = resss/100
            if j==7:
                if a==algorithms[0]:
                    sheet1.write(l, 0, funcs[k])
                        
                    sheet2.write(l, 0, funcs[k])
                    l+=1
                    sheet1.write(l, 0, algorithms[0])
                    sheet1.write(l, 1, algorithms[1])
                    sheet1.write(l, 2, algorithms[2])
                    sheet1.write(l, 3, algorithms[3])
                    sheet1.write(l, 4, algorithms[4])
                    sheet1.write(l, 5, algorithms[5])
                        
                    sheet2.write(l, 0, algorithms[0])
                    sheet2.write(l, 1, algorithms[1])
                    sheet2.write(l, 2, algorithms[2])
                    sheet2.write(l, 3, algorithms[3])
                    sheet2.write(l, 4, algorithms[4])
                    sheet2.write(l, 5, algorithms[5])
                    l+=1
                else:
                    l+=2
                    
            if a==algorithms[0]:
                sheet1.write(l, 0, percentage)
                    
                sheet2.write(l, 0, results_average)
            elif a==algorithms[1]:
                sheet1.write(l, 1, percentage)
                    
                sheet2.write(l, 1, results_average)
            elif a==algorithms[2]:
                sheet1.write(l, 2, percentage)
                    
                sheet2.write(l, 2, results_average) 
            elif a==algorithms[3]:
                sheet1.write(l, 3, percentage)
                    
                sheet2.write(l, 3, results_average)
            elif a==algorithms[4]:
                sheet1.write(l, 4, percentage)
                    
                sheet2.write(l, 4, results_average)
            else:
                sheet1.write(l, 5, percentage)
                    
                sheet2.write(l, 5, results_average)

            wb.save('convergence.xls')
            wb2.save('convergence_MAE.xls')
                
            print("Algorithm "+a+" Function "+funcs[k]+" for "+str(j)+" has "+str(percentage)+"%")
            l+=1
        k+=1