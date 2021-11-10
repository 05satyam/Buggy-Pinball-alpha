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
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from bioinfokit.analys import stat

algorithms = ['\\variantTR4', '\\SA', '\\TA', '\\PSO']
functions = ['\\rastrigin', '\\ackley', '\\sphere', '\\easom', '\\shubert', '\\schwefel', '\\holdertable', '\\eggholder', '\\dropwave', '\\langermann']
funcs = ['rastrigin', 'ackley', 'sphere', 'easom', 'shubert', 'schwefel', 'holdertable', 'eggholder', 'dropwave', 'langermann']
f_minimum = [0, 0, 0, -1, -186.7309, 0, -19.2085, -959.6407, -1, -4.15580929184779]
convergeLimit = [0.99, 2.5, 100, -0.1, -49, 118, -18.1, -895, -0.94, -4.127577]
# functions = ['\\schwefel']
# funcs = ['schwefel']
# f_minimum = [0]
# convergeLimit = [118]

for k in range(0, len(functions)):
    for d in range(2, 7):
        dataACC = {'BP' : [], 'SA' : [], 'TA' : [], 'PSO' : [], }
        dataPRE = {'BP' : [], 'SA' : [], 'TA' : [], 'PSO' : [], }
        weGotSomethin = False
        for a in algorithms:
            string = r"..\Results"+functions[k]+a+"_"+funcs[k]+"_"+str(d)+"_secs.xls"
            if (path.exists("..\Results"+functions[k]+a+"_"+funcs[k]+"_"+str(d)+"_secs.xls")):
                xls = pd.ExcelFile(string)
                weGotSomethin = True
                sheetX = xls.parse(0)
                if a=='\\variantTR4':
                    algo='BP'
                else:
                    algo=a.replace('\\', '')
                  
                if  float(sheetX.columns[0])<convergeLimit[k]:
                    dataACC[algo].append(1)
                    dataPRE[algo].append(float(sheetX.columns[0]))
                else:
                    dataACC[algo].append(0)
                    dataPRE[algo].append(None)
                     
                for i in range(0,99):
                    if  float(sheetX.values[i][0])<convergeLimit[k]:
                        dataACC[algo].append(1)
                        dataPRE[algo].append(float(sheetX.values[i][0]))
                    else:
                        dataACC[algo].append(0)
                        dataPRE[algo].append(None)
            elif(path.exists("..\Results"+functions[k]+a+"_"+funcs[k]+"_"+str(d)+"_secs_7.xls")):
                weGotSomethin = True
                for j in range(7, 8):
                    string = r"..\Results"+functions[k]+a+"_"+funcs[k]+"_"+str(d)+"_secs_"+str(j)+".xls"                    
                    xls = pd.ExcelFile(string)
                    sheetX = xls.parse(0)
                    if a=='\\variantTR4':
                        algo='BP'
                    else:
                        algo=a.replace('\\', '')
                      
                    if  float(sheetX.columns[0])<convergeLimit[k]:
                        dataACC[algo].append(1)
                        dataPRE[algo].append(float(sheetX.columns[0]))
                    else:
                        dataACC[algo].append(0)
                        dataPRE[algo].append(None)
                         
                    for i in range(0,99):
                        if  float(sheetX.values[i][0])<convergeLimit[k]:
                            dataACC[algo].append(1)
                            dataPRE[algo].append(float(sheetX.values[i][0]))
                        else:
                            dataACC[algo].append(0)
                            dataPRE[algo].append(None)
            
#             for j in range(1, 8):
#                 string = r"..\Results"+functions[k]+"\\3D"+a+"_"+funcs[k]+"_"+str(d)+"_secs_"+str(j)+".xls"
#                 if (path.exists("..\Results"+functions[k]+"\\3D"+a+"_"+funcs[k]+"_"+str(d)+"_secs_"+str(j)+".xls")):
#                     xls = pd.ExcelFile(string)
#                     weGotSomethin = True
#                     sheetX = xls.parse(0)
#                     if a=='\\variantTR4':
#                         algo='BP'
#                     else:
#                         algo=a.replace('\\', '')
#                      
#                     if  float(sheetX.columns[0])<convergeLimit[k]:
#                         dataACC[algo].append(1)
#                         dataPRE[algo].append(float(sheetX.columns[0]))
#                     else:
#                         dataACC[algo].append(0)
#                         dataPRE[algo].append(None)
#                         
#                     for i in range(0,99):
#                         if  float(sheetX.values[i][0])<convergeLimit[k]:
#                             dataACC[algo].append(1)
#                             dataPRE[algo].append(float(sheetX.values[i][0]))
#                         else:
#                             dataACC[algo].append(0)
#                             dataPRE[algo].append(None)
                else:
                    continue

        if(weGotSomethin):
            print("--------------",funcs[k],"function,",d,"dimensions--------------")
            print("accuracy")
            df = pd.DataFrame(dataACC)
            df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['BP', 'SA', 'TA', 'PSO'])
            df_melt.columns = ['index', 'algorithm', 'value']
            fvalue, pvalue = stats.f_oneway(df['BP'], df['SA'], df['TA'], df['PSO'])
            print("F value is",fvalue,"P value overall is",pvalue)
            
            model = ols('value ~ C(algorithm)', data=df_melt).fit()
            anova_table = sm.stats.anova_lm(model, typ=2)
            res = stat()
            res.anova_stat(df=df_melt, res_var='value', anova_model='value ~ C(algorithm)')
        #     print(res.anova_summary)
        
            res = stat()
            res.tukey_hsd(df=df_melt, res_var='value', xfac_var='algorithm', anova_model='value ~ C(algorithm)')
            print(res.tukey_summary.to_latex())
            
            #print("precision")
            df = pd.DataFrame(dataPRE)
            df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['BP', 'SA', 'TA', 'PSO'])
            df_melt.columns = ['index', 'algorithm', 'value']
            fvalue, pvalue = stats.f_oneway(df['BP'], df['SA'], df['TA'], df['PSO'])
            #print("F value is",fvalue,"P value overall is",pvalue)
            if funcs[k]=="ackley":    
                print(df)
            model = ols('value ~ C(algorithm)', data=df_melt).fit()
            anova_table = sm.stats.anova_lm(model, typ=2)
            res = stat()
            res.anova_stat(df=df_melt, res_var='value', anova_model='value ~ C(algorithm)')
        #     print(res.anova_summary)
        
            res = stat()
            res.tukey_hsd(df=df_melt, res_var='value', xfac_var='algorithm', anova_model='value ~ C(algorithm)')
            print(res.tukey_summary.to_latex())

