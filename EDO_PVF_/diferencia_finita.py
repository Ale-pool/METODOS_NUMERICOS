# en este codigo se quiere trabajar con problemas de valores iniciales con valores en frontera, mediante
# el esquema de las diferencias finitas
# se esta trabajando el codigo en forma general, pero se toma como base el ejercicio 1

# importaciones de librerias

import numpy as np
import matplotlib.pyplot as plt

n = input(" Digite el numero de puntos interiores: ")
n=int(n) 

# información del problema en especifico
x0 = 0
xf = 0
y0 = 1
yf = -1
h = 0.1    #(xf-x0)/(n+1) 

# procedemos a desarrollar el conjunto de datos < x >
x = np.linspace(x0,xf,n+2)
b= np.zeros(n)     # inicializaremos el vector b como un vector de 0
A= np.eye(n)*(h**2-8)       #np.eye() - permite crear una matriz identidad de tamaño n*n
for k in range(0,n-1):
    A[k][k+1]= -h+4
    A[k+1][k]= h+4
    b[k]=-h**2*x[k+1]

# construccion del vector B
b[0]= -h**2*x[1]-9*y0
b[n-1]= -h**2*x[n]+yf
print(A)
print(b)  
# b se estra presentando como unv vector fila, pero queremos que se muestre como un vector columna
# para solucionar esto procedemos a
y = np.linalg.inv(A).dot(b)
# para agregar los valores faltantes de y para hacer la respectiva operacion, Empleamos:
y = np.insert(y,0,y0)
y = np.insert(y,len(y),yf)

for  k in range(len(y)):
    print('y(',round(x[k],4),')=',y[k])  #.round() para redondear los valores de X en el problema a 4 decimales

plt.plot(x,y)
plt.show()
