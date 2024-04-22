from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la Ecuación diferencial
D = 2
U = 4
k = 5

# Coeficientes de la función trigonométrica (Caso 3)
a = 3
b = 6

# Extremo izquierdo del intervalo de solución
x_a = 1.
# Extremo derecho del intervalo de solución
x_b = 2.
# Valor de la condición de frontera en el extremo izquierdo
y_a = 0.5
# Valor de la condición de frontera en el extremo derecho
y_b = 0.69
# Indicador de tipo de condición de frontera en el etremo derecho del intervalo
ind_bc = 1  # 0: función (Caso 1), 1: derivada (Casos 2 y 3)

def funcld(a, b, x):
    # La siguiente línea se activa en el caso 3
    y = a*np.sin(b*x)
    # La siguiente línea se activa en los casos 1 y 2
    # y = 0
    return y

def ode(x, y):
    return np.array([y[1], (U/D)*y[1] + (k/D)*y[0] + funcld(a,b,x)/D])

def bc(ya, yb):
    return np.array([ya[0] - y_a, yb[ind_bc] - y_b])

x_steps = 100
x = np.linspace(x_a, x_b, x_steps)

y0 = np.ones((2, x_steps))

sol = solve_bvp(ode, bc, x, y0)

plt.plot(sol.x, sol.y[0], '.r', label='Solución numérica solve_bvp')
plt.show()