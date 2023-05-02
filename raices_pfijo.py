import numpy as np

def g1(x): # para x e [2.2, 3]
    return np.sqrt(19/x)

def g2(x): # para x e [0.4, 0.9], phi = -0.02375
    return 0.02375 * x**5 - 0.17340 * x**4 + 0.05321 * x**3 + 0.71511 * x**2 + 0.37862

def g3(x): # para x e [0.6, 1.1], phi = 0.4
    return x - 0.4 * (x - 0.9) * np.exp(-4 * (x - 0.9)**2)

# En el informe especificamos existencia y unicidad de las funciones g1, g2 y g3

def puntoFijo(g,a,b,tol,n):
    x0 = (a+b) / 2
    
    i = 1
    while i <= n:
        x1 = g(x0)
        #print("x1: ", x1)
        if np.abs(x1-x0) < tol:
            return x1, i
        
        x0 = x1
        i = i + 1
    
    print("Se ha superado la cantidad de iteraciones permitidas")
    return None

#
maxIter = 450
tol1 = 1e-5
tol2 = 1e-13

raiz11, i11 = puntoFijo(g1,2.2,3,tol1,maxIter)
raiz12, i12 = puntoFijo(g1,2.2,3,tol2,maxIter)

raiz21, i21 = puntoFijo(g2,0.4,0.9,tol1,maxIter)
raiz22, i22 = puntoFijo(g2,0.4,0.9,tol2,maxIter)

raiz31, i31 = puntoFijo(g3,0.6,1.1,tol1,maxIter)
raiz32, i32 = puntoFijo(g3,0.6,1.1,tol2,maxIter)

print('Tolerancia = ', tol1)
print("Raiz f1 = ", raiz11, ", Iteraciones N = ", i11)
print("Raiz f2 = ", raiz21, ", Iteraciones N = ", i21)
print("Raiz f3 = ", raiz31, ", Iteraciones N = ", i31)

print('Tolerancia = ', tol2)
print("Raiz f1 = ", raiz12, ", Iteraciones N = ", i12)
print("Raiz f2 = ", raiz22, ", Iteraciones N = ", i22)
print("Raiz f3 = ", raiz32, ", Iteraciones N = ", i32)
