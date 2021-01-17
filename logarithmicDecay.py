import random
import math
import numpy as np
import matplotlib.pyplot as plt

xmax=1000
t=0.1
x = np.linspace(0, xmax, 1000)
y=[]

for i in range(0, 1000):
    y.append(t*(1 - (math.e**(math.log10(1 + 10/xmax)*x[i])) / (math.e**(math.log10(1 + 10/xmax)*xmax))))
    
plt.plot(x, y)

plt.show()

# function created: logarithmic decay
# T=period
# i=current iteration
# t=initial threshold
#
#            ln(1 + 10/T)*i
#    t*(1 - e                )
#           ----------------
#            ln(1 + 10/T)*T
#           e