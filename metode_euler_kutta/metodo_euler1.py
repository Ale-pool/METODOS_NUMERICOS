# ECUACIONES DIFERENCIALES ORDINARIAS - METODO DE EULER
 
import numpy as np
import matplotlib.pyplot as plt

#metodo de euler para la aproximacion de 1er orden de y dado y' = f(x, y) 

#Funcion ecuacion diferencial de primer orden f(x,y)
def f1(x,y):
    dvy1 = -2*x + y*x  #para modificar o incluir la funcion de tu problema
    return (dvy1)

# solucion Analitica
def y(x, y):
    fx = 0
    return (fx)    # en este caso en el problema evaluado no tiene solución Analitica

#Valores iniciales

xi = 1   # valor inicial de "x"
yi = -3  # valor inicial de "y"
xf = 2   # valor final de "x"
h = 0.1  # tamaño de paso

n = (xf - xi)/h       # cantidad de pasos o iteraciones
x = np.linspace(xi, xf, int(n+1))
# fx = y(x)      # solucion analitica de integral de f'x
yf=[]            # aproximacion de la integral de f'x
yf.append(yi)
fi= []
fi.append(f1(xi, yi))    # derivada de f'x

for i in range (int(n)):
    fi.append(f1(x[i], yf[i]))
    yf.append(yi + fi[i]*h)
    yi = yf[i+1]


#grafica
plt.plot(x, yf, 'r')
print(x,yf)
plt.show()
