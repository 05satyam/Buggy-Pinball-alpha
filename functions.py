import numpy as np
import matplotlib.pyplot as plt

#sphere function
def f(x, y):
    return x ** 2 + y ** 2
 
def fxder(x, y):
    return 2*x

def fyder(x, y):
    return 2*y

#booth function
def f(x, y):
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def fxder(x, y):
    return 10*x + 8*y - 34

def fyder(x, y):
    return 10*y + 8*x - 38
