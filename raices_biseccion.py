import numpy as np

def f1(x):
    return x**3 - 19

def f2(x):
    return x**5 - 7.3 * x**4 + 2.24 * x**3 + 30.106 * x**2 - 42.1 * x + 15.94

def f3(x):
    return (x - 0.9) * np.exp(-4 * (x - 0.9)**2)
        
def biseccion(f,a,b,tol,n):
    
    if f(a) * f(b) >= 0: # No puede ser así (hipotesis del teorema de Bolsano)
        print("No puede existir una raiz en el intervalo dado.")
        return None
    
    x0 = a

    i = 1
    while i < n:
        x1 = (a+b) / 2 
    
        if np.abs(x1 - x0) < tol:
            return x1
        
        if np.sign(f(x1)) == np.sign(f(a)):
            a = x1
        else:
            b = x1    

        x0 = x1
        i = i + 1
    print("Se ha superado la máxima cantidad de iteraciones posibles.")
    return None

F = [f1,f2,f3]
maxIter = 500 # Cant maxima de iteraciones, por si la tolerancia dada es demasiado chica y nunca se alcanza

print('Tolerancia = 10^-5')
for i in range(0,3):
    print('Raiz ' + str(i+1) + ': ' + str(biseccion(F[i],0,3,1e-5,maxIter)))

print('Tolerancia = 10^-13')
for i in range(0,3):
    print('Raiz ' + str(i+1) + ': ' + str(biseccion(F[i],0,3,1e-13,maxIter)))
