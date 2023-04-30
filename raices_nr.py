import numpy as np

def f1(x):
    return x**3 - 19

def f1p(x):
    return 3 * x**2

def f2(x):
    return x**5 - 7.3 * x**4 + 2.24 * x**3 + 30.106 * x**2 - 42.1 * x + 15.94

def f2p(x):
    return 5 * x**4 - 29.2 * x**3 + 6.72 * x**2 + 60.212 * x - 42.1

def f3(x):
    return (x - 0.9) * np.exp(-4 * (x - 0.9)**2)

def f3p(x):
    return ((-8 * x + 7.2) * (x - 0.9) + 1) * np.exp(-4 * (x - 0.9)**2)

def nr(f,fp,x0,tol):
    if fp(x0) == 0:
        return 'Error de convergencia, determinar otra semilla'
    x1 = x0 - f(x0) / fp(x0)

    while np.abs(x1 - x0) > tol :
        if fp(x1) == 0:
            return 'Error de convergencia, determinar otra semilla'
        x0 = x1
        x1 = x0 - f(x0) / fp(x0)

    return x1

F = [f1,f2,f3]
Fp = [f1p,f2p,f3p]

print('Tolerancia = 10^-5')
for i in range(0,3):
    print('Raiz ' + str(i+1) + ': ' + str(nr(F[i],Fp[i],0.65,1e-5)))

print('Tolerancia = 10^-13')
for i in range(0,3):
    print('Raiz ' + str(i+1) + ': ' + str(nr(F[i],Fp[i],0.65,1e-13)))