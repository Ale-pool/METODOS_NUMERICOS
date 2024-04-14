# xi = np.array([0, 0.2, 0.3, 0.4])
# fi = np.array([1, 1.6, 1.7, 2.0])
# http://blog.espol.edu.ec/analisisnumerico/interpolacion-de-lagrange/
# Algoritmo en Python
"""
    valores de fi:  [1.  1.6 1.7 2. ]
divisores en L(i):  [-0.024  0.004 -0.003  0.008]

Polinomio de Lagrange, expresiones
400.0*x*(x - 0.4)*(x - 0.3) 
  - 566.666666666667*x*(x - 0.4)*(x - 0.2) 
  + 250.0*x*(x - 0.3)*(x - 0.2) 
  - 41.6666666666667*(x - 0.4)*(x - 0.3)*(x - 0.2)

Polinomio de Lagrange: 
41.666666666667*x**3 - 27.5*x**2 + 6.8333333333334*x + 1.0 """


import matplotlib.pyplot as plt
# Interpolacion de Lagrange
# divisoresL solo para mostrar valores
import numpy as np
import sympy as sym

# INGRESO , Datos de prueba
xi = np.array([0, 0.2, 0.3, 0.4])
fi = np.array([1, 1.6, 1.7, 2.0])

# PROCEDIMIENTO
# Polinomio de Lagrange
n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)
for i in range(0,n,1):
    
    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador

# simplifica el polinomio
polisimple = polinomio.expand()

# para evaluación numérica
px = sym.lambdify(x,polisimple)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

# SALIDA
print('    valores de fi: ',fi)
print('divisores en L(i): ',divisorL)
print()
print('Polinomio de Lagrange, expresiones')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(polisimple)

# Gráfica
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación Lagrange')
plt.show()