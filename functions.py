import math
def sphere(x, y):
    return x ** 2 + y ** 2
 
def sphere_dx(x, y):
    return 2*x

def sphere_dy(x, y):
    return 2*y

def booth(x, y):
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def booth_dx(x, y):
    return 10*x + 8*y - 34

def booth_dy(x, y):
    return 10*y + 8*x - 38

def rastrigin(x, y, A):
    return 2*A + x**2 - A*math.cos(2*math.pi*x) + y**2 - A*math.cos(2*math.pi*y)

def rastrigin_dx(x, y, A):
    return 2*x + 2*math.pi*A*math.sin(2*math.pi*x)

def rastrigin_dy(x, y, A):
    return 2*y + 2*math.pi*A*math.sin(2*math.pi*y)
