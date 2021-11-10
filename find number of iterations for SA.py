import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
from functions import *

T=10
i=0
b=0.9999713
while T>0.01:
    T=b*T
    i+=1
print(i)