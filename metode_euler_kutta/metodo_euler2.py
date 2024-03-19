
import numpy as np
import matplotlib.pyplot as plt
import math
def funcion(x,y):
    ec=x+2*y
    return ec

def solucion(x, y):
    sol=.25*math.exp(2*x)-.5*x-.25
h=float(input(" Tamaño de paso: "))
s=float(input(" ¿Hata que valor? ")) 
# n=(s/h)+1
n = int(s / h)
x=np.zeros(n)
y=np.zeros(n)
ys=np.zeros(n)
print(x[0], y[0])
for i in np.arange(1,n):
    y[i]=y[i-1]+(funcion(x[i-1],y[i-1]))*h
    x[i]=x[i-1]+h
    ys[i]=solucion(x[i-1],y[i-1])
    print(x[i], y[i])
plt.scatter(x,y)
plt.scatter(x,ys,color='red')

# grafica 
plt.plot(x, y, 'r')
print(x,y)
plt.show()
