import math

def sphere(x, y):   # limits -inf <= x,y <= inf
    return x ** 2 + y ** 2

def sphere_d(xvals):
    result = 0
    for x in xvals:
        result += x**2
    return result
 
def sphere_dx(x, y):
    return 2*x

def sphere_dy(x, y):
    return 2*y
#########################################
def booth(x, y):   # limits -10 <= x,y <= 10
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def booth_dx(x, y):
    return 10*x + 8*y - 34

def booth_dy(x, y):
    return 10*y + 8*x - 38
#########################################
def rastrigin(x, y):
    return 20 + x**2 - 10*math.cos(2*math.pi*x) + y**2 - 10*math.cos(2*math.pi*y)
def rastrigin_d(xvals):
    result = len(xvals)*10
    for x in xvals:
        result += x**2 - 10*math.cos(2*math.pi*x)
    return result

def rastrigin_dx(x, y, A):
    return 2*x + 2*math.pi*A*math.sin(2*math.pi*x)

def rastrigin_dy(x, y, A):
    return 2*y + 2*math.pi*A*math.sin(2*math.pi*y)
#########################################
def beale(x, y):    # limits -4.5 <= x,y <= 4.5
    return (1.5 -x +x*y)**2 + (2.25 -x +x*y**2)**2 + (2.625 -x + x*y**3)**2

def beale_dx(x, y):
    return (y - 1)*((8*y**5 + 8*y**4 + 16*y**3 - 8*y - 24)*x + 21*y**2 + 39*y + 51) / 4
    
def beale_dy(x, y):
    return x*(24*x*y**5 + 16*x*y**3 + (63 - 24*x)*y**2 + (36 - 8*x)*y - 8*x + 12) / 4
#########################################
def mcCormick(x, y):    # limits -1.5 <= x <= 4, -3 <= y <= 4
    return math.sin(x+y) + (x-y)**2 + -1.5*x + 2.5*y + 1

def mcCormick_dx(x, y):
    return math.cos(x+y) + 2*(x-y) - 1.5
    
def mcCormick_dy(x, y):
    return math.cos(x+y) - 2*(x-y) + 2.5
#########################################
def eggholder1(x, y):    # limits -512 <= x <= 512, -512 <= y <= 512
    return -(y + 47)*math.sin(math.sqrt(abs(x/2 + y + 47))) - x*math.sin(math.sqrt(abs(x - y - 47)))

def eggholder(x):    # limits -512 <= x <= 512, -512 <= y <= 512
    return -(x[1] + 47)*math.sin(math.sqrt(abs(x[0]/2 + x[1] + 47))) - x[0]*math.sin(math.sqrt(abs(x[0] - x[1] - 47)))

def eggholder_dx(x, y):
    return -math.sin(math.sqrt(abs(x - y - 47))) - (x*(x - y - 47)* math.cos(math.sqrt(abs(x - y - 47)))) / (2*abs(x - y - 47)**(3/2)) + ((- y - 47)*math.cos(math.sqrt(abs(x/2 + y + 47)))*(x/2 + y + 47)) / (4*abs(x/2 + y + 47)**(3/2))

def eggholder_dy(x, y):
    return -math.sin(math.sqrt(abs(x/2 + y + 47))) + ((- y - 47)*(x/2 + y + 47)*math.cos(math.sqrt(abs(x/2 + y + 47)))) / (2*abs(y + x/2 + 47)**(3/2)) - (x*(y - x + 47)*math.cos(math.sqrt(abs(y - x + 47)))) / (2*abs(y - x + 47)**(3/2))
#########################################
def ackley(x, y):
    return -20*math.exp(-0.2*math.sqrt(0.5*(x**2 + y**2))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20

def ackley_d(xvals):
    sum1 = 0
    sum2 = 0
    for x in xvals:
        sum1 += x**2
        sum2 += math.cos(2*math.pi*x)
    return -20*math.exp(-0.2*math.sqrt((1/len(xvals))*sum1)) - math.exp((1/len(xvals))*sum2) + 20 + math.exp(1)
#########################################
def rosenbrock(x, y):
    return 100*(y - x**2)**2 + (x - 1)**2

def rosenbrock_dx(x, y):
    return 400*x**3 + (2 - 400*y)*x - 2

def rosenbrock_dy(x, y):
    return 200*(y - x**2)
#########################################
def goldsteinPrince(x, y):
    return (1 + ((x + y + 1)**2)*(19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2))*(30 + ((2*x - 3*y)**2)*(18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))

def goldsteinPrince_dx(x, y):
    return (2*(x + y + 1)*(3*x**2 + 6*x*y + - 14*x +3*y**2 - 14*y + 19) + ((x + y + 1)**2)*(6*x + 6*y - 14))*(((2*x - 3*y)**2)*(12*x**2 - 36*x*y - 32*x + 27*y**2 + 48*y + 18) + 30) + (((x + y + 1)**2)*(3*x**2 + 6*x*y + - 14*x + 3*y**2 - 14*y + 19) + 1)*(4*(2*x - 3*y)*(12*x**2  - 36*x*y - 32*x + 27*y**2 + 48*y + 18) + ((2*x - 3*y)**2)*(24*x - 36*y - 32))
#########################################
def schwefel(x, y):
    return 2*418.9829 + x*math.sin(math.sqrt(abs(x))) + y*math.sin(math.sqrt(abs(y)))

def schwefel_d(xvals):
    result = len(xvals)*418.9829
    for x in xvals:
        result += x*math.sin(math.sqrt(abs(x)))
    return result 
#########################################
def easom1(x, y):        # limits -10 <= x <= 10, -10 <= y <= 10
    return -math.cos(x)*math.cos(y)*math.exp(-((x - math.pi)**2 + (y - math.pi)**2))

def easom(x):        # limits -10 <= x <= 10, -10 <= y <= 10
    return -math.cos(x[0])*math.cos(x[1])*math.exp(-((x[0] - math.pi)**2 + (x[1] - math.pi)**2))
#########################################
def shubert1(x, y):
    xval = 0
    yval = 0
    for i in range(1, 6):
        xval += i*math.cos((i + 1)*x + i)
        yval += i*math.cos((i + 1)*y + i)
    return xval*yval

def shubert(x):
    xval = 0
    yval = 0
    for i in range(1, 6):
        xval += i*math.cos((i + 1)*x[0] + i)
        yval += i*math.cos((i + 1)*x[1] + i)
    return xval*yval
#########################################
def alpine(x, y):
    return abs(x*math.sin(x) + 0.1*x) + abs(y*math.sin(y) + 0.1*y)
#########################################
def griewank(x, y):
    return (x**2)/4000 + (y**2)/4000 - (math.cos(x)*math.cos(y)/math.sqrt(2)) + 1
#########################################
def holdertable1(x, y):
    return -abs(math.sin(x)*math.cos(y)*math.exp(abs(1 - math.sqrt(x**2 + y**2) / math.pi)))

def holdertable(x):
    return -abs(math.sin(x[0])*math.cos(x[1])*math.exp(abs(1 - math.sqrt(x[0]**2 + x[1]**2) / math.pi)))
#########################################
def langermann1(x, y):
    m = 5
    c = [1, 2, 5, 2, 3]
    A = {
        0 : {
            0 : 3,
            1 : 5            
            },
        1 : {
            0 : 5,
            1 : 2            
            },
        2 : {
            0 : 2,
            1 : 1            
            },
        3 : {
            0 : 1,
            1 : 4            
            },
        4 : {
            0 : 7,
            1 : 9            
            }
        }
    res = 0
    for i in range(0, m):
        res += c[i]*math.exp((-1/math.pi)*((x - A[i][0])**2 + (y - A[i][1])**2))*math.cos(math.pi*((x - A[i][0])**2 + (y - A[i][1])**2))
    return res
        
def langermann(x):
    m = 5
    c = [1, 2, 5, 2, 3]
    A = {
        0 : {
            0 : 3,
            1 : 5            
            },
        1 : {
            0 : 5,
            1 : 2            
            },
        2 : {
            0 : 2,
            1 : 1            
            },
        3 : {
            0 : 1,
            1 : 4            
            },
        4 : {
            0 : 7,
            1 : 9            
            }
        }
    res = 0
    for i in range(0, m):
        res += c[i]*math.exp((-1/math.pi)*((x[0] - A[i][0])**2 + (x[1] - A[i][1])**2))*math.cos(math.pi*((x[0] - A[i][0])**2 + (x[1] - A[i][1])**2))
    return res
#########################################
def dropwave1(x, y):
    return -(1 + math.cos(12*math.sqrt(x**2 + y**2))) / (0.5*(x**2 + y**2) + 2)

def dropwave(x):
    return -(1 + math.cos(12*math.sqrt(x[0]**2 + x[1]**2))) / (0.5*(x[0]**2 + x[1]**2) + 2)
##########################################
def michalewicz(x, y):
    m=10
    return -math.sin(x)*(math.sin(1*x**2/math.pi))**(2*m)-math.sin(y)*(math.sin(2*y**2/math.pi))**(2*m)