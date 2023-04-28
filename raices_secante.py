import numpy as np

def f1(x):
    return x**3 - 19

def f2(x):
    return x**5 - 7.3 * x**4 + 2.24 * x**3 + 30.106 * x**2 - 42.1 * x + 15.94

def f3(x):
    return (x - 0.9) * np.exp(-4 * (x - 0.9)**2)

def biseccion_semillas(f,a,b):
    x0 = (a+b)/2
    return [x0, (x0 + a) / 2 if np.sign(f(x0)) != np.sign(f(a)) else (x0 + b) / 2]
        
def secante(f,a,b,tol):
    semillas = biseccion_semillas(f,a,b)
    x0 = semillas[0]
    x1 = semillas[1]

    while(np.abs(x1 - x0) > tol):
        aux = x1
        x1 = x1 - f(x1) * (x1-x0) / (f(x1) - f(x0))
        x0 = aux

    return x1

F = [f1,f2,f3]

print('Tolerancia = 10^-5')
for i in range(0,3):
    print('Raiz ' + str(i+1) + ': ' + str(secante(F[i],0,3,1e-5)))

print('Tolerancia = 10^-13')
for i in range(0,3):
    print('Raiz ' + str(i+1) + ': ' + str(secante(F[i],0,3,1e-13)))