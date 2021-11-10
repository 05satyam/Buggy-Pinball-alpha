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
# functions = ['\\rastrigin', '\\ackley', '\\sphere', '\\schwefel']
# funcs = ['rastrigin', 'ackley', 'sphere', 'schwefel']
# f_minimum = [0, 0, 0, 0]
# convergeLimit = [0.99, 2.5, 100, 118]
functions = ['\\schwefel']
funcs = ['schwefel']
f_minimum = [0]
convergeLimit = [118]

for a in algorithms:
    l=0
    k=0
    for f_name in functions:
        for d in range(2, 7):
            for j in range(1, 2):
                string = r"..\Results"+f_name+a+"_"+funcs[k]+"_"+str(d)+"_secs.xls"
                if (path.exists("..\Results"+f_name+a+"_"+funcs[k]+"_"+str(d)+"_secs.xls")):
                    xls = pd.ExcelFile(string)
                else:
                    continue
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
                if j==1:
                    if a==algorithms[0]:
                        sheet1.write(l, 0, funcs[k])
                        sheet1.write(l, 1, d)
                        
                        sheet2.write(l, 0, funcs[k])
                        sheet2.write(l, 1, d)
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
                elif a==algorithms[4]:
                    sheet1.write(l, 4, percentage)
                    
                    sheet2.write(l, 4, results_average)
                elif a==algorithms[5]:
                    sheet1.write(l, 5, percentage)
                     
                    sheet2.write(l, 5, results_average)
                else:
                    sheet1.write(l, 3, percentage)
                    
                    sheet2.write(l, 3, results_average)
                         
                wb.save('convergence_multi2.xls')
                wb2.save('convergence_MAE_multi2.xls')
                
                print("Algorithm "+a+" Function "+funcs[k]+" in "+str(d)+" dimensions has "+str(percentage)+"% and "+str(results_average)+" MAE")
                l+=1
        k+=1