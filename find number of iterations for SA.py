import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *

T=.0001
i=0
b=0.99999955
while T>0.000001:
    T=b*T
    i+=1
print(i)