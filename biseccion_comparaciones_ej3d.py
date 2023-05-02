import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def f1(x):
    return x**3 - 19

def f2(x):
    return x**5 - 7.3 * x**4 + 2.24 * x**3 + 30.106 * x**2 - 42.1 * x + 15.94

def f3(x):
    return (x - 0.9) * np.exp(-4 * (x - 0.9)**2)
    
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

def comparacionesBiseccion(f,a,b,tol,n,r):
    
    if f(a) * f(b) >= 0: # No puede ser así (hipotesis del teorema de Bolsano)
        print("No puede existir una raiz en el intervalo dado.")
        return None
    
    x0 = a
    x_1 = 0
    x_2 = 0
    
    comparacion = []
    
    i = 1
    while i < n:
        x1 = (a+b) / 2 
    
        if np.abs(x1 - x0) < tol:
            return x1, i, comparacion
        
        if np.sign(f(x1)) == np.sign(f(a)):
            a = x1
        else:
            b = x1    
        
        log_relativo = np.abs(np.log(np.abs(x1-x0)))
        log_absoluto = np.abs(np.log(np.abs(x1-r)))

        if i > 2:
            x1_x0_x_1 = np.abs((x1-x0)/(x0-x_1))
            x0_x_1_x_2 = np.abs((x0-x_1)/(x_1-x_2))
            alfa = np.abs(np.log(x1_x0_x_1) / np.log(x0_x_1_x_2))
            lambda_ = np.abs((x1-r)/(x0-r)**alfa)
            
            comparacion.append((i, alfa, lambda_, log_relativo, log_absoluto))
        else:
            comparacion.append((i, 0, 0, log_relativo, log_absoluto))
        
        x_2 = x_1
        x_1 = x0
        x0 = x1
        i = i + 1
        
    print("Se ha superado la máxima cantidad de iteraciones posibles.")
    return None

################################################
maxIter = 500 # Cant maxima de iteraciones, por si la tolerancia dada es demasiado chica y nunca se alcanza
tol1 = 1e-5
tol2 = 1e-13

r_real_f1 = sp.optimize.brentq(f1, 0, 3)
raiz1, i1, comparacion1 = comparacionesBiseccion(f1, 0, 3, tol2, maxIter, r_real_f1)

x1 = []
converg1 = []
asintota1 = []
relativo1 = []
absoluto1 = []
print("-----------------------------------------------------")
for elemento in comparacion1:
    x1.append(elemento[0])
    converg1.append(elemento[1])
    asintota1.append(elemento[2])
    relativo1.append(elemento[3])
    absoluto1.append(elemento[4])
    #print(elemento[0], "\t\t", elemento[1], "\t\t", elemento[2], "\t\t", elemento[3], "\t\t", elemento[4])

plt.figure(1)
plt.plot(x1, converg1, color = "red", linewidth = 3)
plt.grid()
plt.title("f1: Orden de convergencia (P) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("P")
plt.xlim(1,45) 
plt.ylim(0,2)
plt.savefig("convergencia_biseccion_f1.png")
plt.show()

plt.figure(2)
plt.plot(x1, asintota1, color = "green", linewidth = 3)
plt.grid()
plt.title("f1: Constante asintótica (λ) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("λ")
plt.xlim(1,45) 
plt.ylim(0,41)
plt.savefig("asintota_biseccion_f1.png")
plt.show()

plt.figure(3)
plt.plot(x1, relativo1, color = "blue", linewidth = 3)
plt.grid()
plt.title("f1: log(/∆x/) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("log(/∆x/)")
plt.xlim(1,45) 
plt.ylim(0,35)
plt.savefig("relativo_biseccion_f1.png")
plt.show()

plt.figure(4)
plt.plot(x1, absoluto1, color = "purple", linewidth = 3)
plt.grid()
plt.title("f1: log(/x_candidata - x_real/) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("log(/x_candidata - x_real/")
plt.xlim(1,45) 
plt.ylim(0,35)
plt.savefig("absoluto_biseccion_f1.png")
plt.show()


##########################################
r_real_f2 = sp.optimize.brentq(f2, 0, 3)
raiz2, i2, comparacion2 = comparacionesBiseccion(f2, 0, 3, tol2, maxIter, r_real_f2)

x2 = []
converg2 = []
asintota2 = []
relativo2 = []
absoluto2 = []
print("-----------------------------------------------------")
for elemento in comparacion2:
    x2.append(elemento[0])
    converg2.append(elemento[1])
    asintota2.append(elemento[2])
    relativo2.append(elemento[3])
    absoluto2.append(elemento[4])
    #print(elemento[0], "\t\t", elemento[1], "\t\t", elemento[2], "\t\t", elemento[3], "\t\t", elemento[4])

plt.figure(5)
plt.plot(x2, converg2, color = "red", linewidth = 3)
plt.grid()
plt.title("f2: Orden de convergencia (P) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("P")
plt.xlim(1,45) 
plt.ylim(0,2)
plt.savefig("convergencia_biseccion_f2.png")
plt.show()

plt.figure(6)
plt.plot(x2, asintota2, color = "green", linewidth = 3)
plt.grid()
plt.title("f2: Constante asintótica (λ) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("λ")
plt.xlim(1,45) 
plt.ylim(0,41)
plt.savefig("asintota_biseccion_f2.png")
plt.show()

plt.figure(7)
plt.plot(x2, relativo2, color = "blue", linewidth = 3)
plt.grid()
plt.title("f2: log(/∆x/) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("log(/∆x/)")
plt.xlim(1,45) 
plt.ylim(0,35)
plt.savefig("relativo_biseccion_f2.png")
plt.show()

plt.figure(8)
plt.plot(x2, absoluto2, color = "purple", linewidth = 3)
plt.grid()
plt.title("f2: log(/x_candidata - x_real/) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("log(/x_candidata - x_real/")
plt.xlim(1,45) 
plt.ylim(0,35)
plt.savefig("absoluto_biseccion_f2.png")
plt.show()

###################################################
r_real_f3 = sp.optimize.brentq(f3, 0, 3)
raiz3, i3, comparacion3 = comparacionesBiseccion(f3, 0, 3, tol2, maxIter, r_real_f3)

x3 = []
converg3 = []
asintota3 = []
relativo3 = []
absoluto3 = []
print("-----------------------------------------------------")
for elemento in comparacion1:
    x3.append(elemento[0])
    converg3.append(elemento[1])
    asintota3.append(elemento[2])
    relativo3.append(elemento[3])
    absoluto3.append(elemento[4])
    #print(elemento[0], "\t\t", elemento[1], "\t\t", elemento[2], "\t\t", elemento[3], "\t\t", elemento[4])

plt.figure(9)
plt.plot(x3, converg3, color = "red", linewidth = 3)
plt.grid()
plt.title("f3: Orden de convergencia (P) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("P")
plt.xlim(1,45) 
plt.ylim(0,2)
plt.savefig("convergencia_biseccion_f3.png")
plt.show()

plt.figure(10)
plt.plot(x3, asintota3, color = "green", linewidth = 3)
plt.grid()
plt.title("f3: Constante asintótica (λ) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("λ")
plt.xlim(1,45) 
plt.ylim(0,41)
plt.savefig("asintota_biseccion_f3.png")
plt.show()

plt.figure(11)
plt.plot(x3, relativo3, color = "blue", linewidth = 3)
plt.grid()
plt.title("f3: log(/∆x/) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("log(/∆x/)")
plt.xlim(1,45) 
plt.ylim(0,35)
plt.savefig("relativo_biseccion_f3.png")
plt.show()

plt.figure(12)
plt.plot(x3, absoluto3, color = "purple", linewidth = 3)
plt.grid()
plt.title("f3: log(/x_candidata - x_real/) vs iteraciones \n Tolerancia = 1e-13")
plt.xlabel("i")
plt.ylabel("log(/x_candidata - x_real/")
plt.xlim(1,45) 
plt.ylim(0,35)
plt.savefig("absoluto_biseccion_f3.png")
plt.show()
