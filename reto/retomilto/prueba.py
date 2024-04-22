import sympy as sp

# Definición de símbolos
x, A, B, C, D, r1, r2 = sp.symbols('x A B C D r1 r2')

# Valores dados
Dc = 2
Uc = 4
kc = 5
a = 3
b = 6
xa = 1
xb = 2
ca = 0.5
qb = 0.69

# Definición de la ecuación característica
ecuacion_caracteristica = r1**2 - (Uc/Dc)*r1 - (kc/Dc)

# Resolución de la ecuación característica
soluciones_r = sp.solve(ecuacion_caracteristica, (r1, r2))
r1, r2 = soluciones_r[0], soluciones_r[1]

# Definición de las soluciones linealmente independientes
v1 = sp.exp(r1*x)
v2 = sp.exp(r2*x)

# Definición de la función de forzamiento f(x)
f_x = a * sp.sin(b*x)

# Definición de la solución particular
c_p = v1 * sp.integrate(v2 * f_x, x) - v2 * sp.integrate(v1 * f_x, x)

# Definición de la solución homogénea
c_h = A * sp.exp(r1*x) + B * sp.exp(r2*x)

# Aplicación de las condiciones de contorno
sistema_ecuaciones = [c_p.subs(x, xa) - ca, c_p.diff(x).subs(x, xb) - qb]
soluciones_ab = sp.solve(sistema_ecuaciones, (A, B))
A_val, B_val = soluciones_ab[A], soluciones_ab[B]

# Combinación de la solución homogénea y particular
c_x = c_h.subs({A: A_val, B: B_val}) + c_p

# Mostrar la solución analítica
c_x

import numpy as np
import matplotlib.pyplot as plt

# Definir la solución analítica
def solucion_analitica(x):
    return A_val * np.exp(r1*x) + B_val * np.exp(r2*x) + c_p.subs(x, x)

# Generar puntos para graficar
x_eval = np.linspace(xa, xb, 100)
y_analitica = [solucion_analitica(x) for x in x_eval]

# Graficar la solución analítica
plt.figure(figsize=(10, 6))
plt.plot(x_eval, y_analitica, label='Solución Analítica', color='green')
plt.xlabel('x')
plt.ylabel('c(x)')
plt.title('Solución Analítica (Nivel 3)')
plt.axvline(x=xa, color='red', linestyle='--', label=f'c({xa}) = {ca}')
plt.axvline(x=xb, color='blue', linestyle='--', label=f"c'({xb}) = {qb}")
plt.legend()
plt.grid(True)
plt.show()
