import random
import matplotlib.pyplot as plt

def fuerza_bruta():
    candado = random.randint(0,999)
    intentos = 1

    while (intentos-1 != candado):
        intentos+=1

    return intentos

muestra = [0] * 100000
for i in range (0, 100000):
    muestra[i] = fuerza_bruta()

plt.hist(muestra, 100, color = 'lightgray', ec = 'black')
plt.xlabel('Cantidad de intentos')
plt.ylabel('Frecuencia')
plt.show()