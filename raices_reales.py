import numpy as np
import scipy as sp

def f1(x):
    return x**3 - 19

def f2(x):
    return x**5 - 7.3 * x**4 + 2.24 * x**3 + 30.106 * x**2 - 42.1 * x + 15.94

def f3(x):
    return (x - 0.9) * np.exp(-4 * (x - 0.9)**2)

F = [f1,f2,f3]

for i in range(0,3):
    print('Raiz ' + str(i+1) + ': ' + str(sp.optimize.brentq(F[i], 0, 3)))