import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x**3 - 19

def f2(x):
    return x**5 - 7.3 * x**4 + 2.24 * x**3 + 30.106 * x**2 - 42.1 * x + 15.94

def f3(x):
    return (x - 0.9) * np.exp(-4 * (x - 0.9)**2)

X = np.linspace(0,3,1000)

plt.figure(1)

plt.plot(X, f1(X))
plt.xlabel('x')
plt.ylabel('f1(x)')
plt.title('Gráfico de la función 1')
plt.grid(True)

plt.figure(2)

plt.plot(X, f2(X))
plt.xlabel('x')
plt.ylabel('f2(x)')
plt.title('Gráfico de la función 2')
plt.grid(True)

plt.figure(3)

plt.plot(X, f3(X))
plt.xlabel('x')
plt.ylabel('f3(x)')
plt.title('Gráfico de la función 3')
plt.grid(True)

plt.tight_layout()
plt.show()