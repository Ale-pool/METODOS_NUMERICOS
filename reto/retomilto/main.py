#Importación de las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import Nivel3 as N3
import tkinter
'''
Impresión del mensaje de que hace el código en una ventana emergente con tkinter
'''
# Creación de la ventana
window = tkinter.Tk()
# Creación del mensaje de explicación del código
label = tkinter.Label(window, text='Este código en Python resuelve una ecuación diferencial \n'
                        'ordinaria (EDO) utilizando un método de elementos finitos con funciones\n'
                        'de base radial multicuádricas inversas. A continuación una explicación\n' 
                        'de las partes clave del código:\n\n'
                        '1. Definición de Parámetros:\n'
                        'Aquí se establecen valores para los parámetros de la ecuación diferencial\n'
                        'y otros valores que se utilizarán en el código.\n\n'
                        '2. Definición de Funciones:\n'
                        'funcld(a, b, x): Define una función funcld que calcula una función seno\n' 
                        'con amplitud a, frecuencia b, y valor de entrada x.\n'
                        'ode(x, y): Define una función ode que representa la EDO a resolver. Toma\n' 
                        'un vector x y un vector y como entrada y devuelve un array con las\n'
                        'derivadas de y.\n'
                        'bc(ya, yb): Define una función bc que establece las condiciones de\n'
                        'contorno. Toma los valores en los extremos ya e yb y devuelve un array\n' 
                        'que debe ser igual a cero para cumplir con las condiciones de frontera.\n'
                        'fmqi(r, c), Pdfmqi(r, c), Sdfmqi(r, c): Estas funciones calculan la\n' 
                        'función de base radial multicuádrica inversa y sus derivadas.\n'
                        'sfbd(x, ca, cb, n, c): Esta función resuelve la ecuación diferencial\n'
                        'utilizando funciones de base radial multicuádricas inversas.\n\n'
                        '3. Resolución de la EDO:\n'
                        'Se define un intervalo [Xa, Xb], condiciones de frontera (ca y cb),\n' 
                        'número de puntos (n), y parámetros de forma (c, c2, c3, c4).\n'
                        'Luego se resuelve la EDO utilizando las funciones definidas.\n\n'
                        '4. Solución Exacta:\n'
                        'Se utiliza la función solve_bvp para encontrar la solución exacta de la\n'
                        'EDO.\n\n'
                        '5. Cálculo de Errores:\n'
                        'Se calcula el error local con respecto a la solución exacta para cada\n' 
                        'conjunto de parámetros de forma.\n\n'
                        '6. Gráficos:'
                        'Se generan gráficos para visualizar las soluciones numéricas y la\n'
                        'solución exacta.\n'
                        'También se muestran gráficos de los errores locales y se calcula la\n'
                        'norma L2 de los errores.\n\n'
                        '7. Impresión de Resultados:\n'
                        'Se imprime la norma L2 de los errores para cada conjunto de parámetros\n' 
                        'de forma.')
# Añadir el mensaje a la ventana
label.pack()
# Iniciar la ventana
window.mainloop()


#Datos iniciales  
# Extremo izquierdo del intervalo de solución
Xa=1
# Valor de la condición de frontera en el extremo izquierdo
ca=0.2
# Extremo derecho del intervalo de solución
Xb=2
# Valor de la condición de frontera en el extremo derecho
cb=0.9

# Número de puntos
n=15

#Parametros de forma
c=0.01
c2=-1
c3=0.9
c4=0.86

#Valores que se remplazaran en x.
x = np.linspace(Xa, Xb, n)

'''
Llamar la solución de la función de base radial para cada uno de los parámetros de forma.
'''
#se haya el valor de y, dandole los valores de x, el extremo izquierdo y derecho, núemro de puntos
#y el primer parametro de forma
yt1=N3.sfbd(x,ca,cb,n,c)
#se haya el valor de y, dandole los valores de x, el extremo izquierdo y derecho, núemro de puntos
#y el segundo parametro de forma
yt2=N3.sfbd(x,ca,cb,n,c2)
#se haya el valor de y, dandole los valores de x, el extremo izquierdo y derecho, núemro de puntos
#y el tercer parametro de forma
yt3=N3.sfbd(x,ca,cb,n,c3)
#se haya el valor de y, dandole los valores de x, el extremo izquierdo y derecho, núemro de puntos
#y el cuarto parametro de forma
yt4=N3.sfbd(x,ca,cb,n,c4)
'''
Solución exacta
'''
#se crea un array que se inicializa con unos, lo que significa que todos los elementos del 
# array se establecen en 1.Este array se utiliza como condición inicial para el solucionador de EDO.
y0 = np.ones((2, n))
#la función solve_bvp toma cuatro argumentos:
#`N3.ode`, la función que define la EDO.
#`N3.bc`, la función que define las condiciones de contorno. 
#`x`: Un vector que especifica los puntos de la cuadrícula en los que se resolverá la EDO.
#`y0`: Un vector que especifica los valores iniciales de la solución.
sol = solve_bvp(N3.ode, N3.bc, x, y0)
#Se crea una variable que contiene los valores de la solución exacta
Exacta = sol.y[0]
'''
Se determina el error local con cada uno de los parámetros de forma, con el valor absoluto 
ya que solo se necesita la diferencia 
'''
#Error de la solución 1
Error1=np.abs(Exacta-yt1)
#Error de la solución 2
Error2=np.abs(Exacta-yt2)
#Error de la solución 3
Error3=np.abs(Exacta-yt3)
#Error de la solución 4
Error4=np.abs(Exacta-yt4)

'''
 calcula la norma L2 del error entre la solución numérica y la solución exacta, teniendo en 
 cuenta los errores locales hayados anteriormente.
 La norma L2 es una medida de la magnitud del error, y se calcula tomando la raíz cuadrada 
 de la suma de los cuadrados de los errores individuales.
'''
Er1=np.sqrt(np.dot(Error1,Error1))
Er2=np.sqrt(np.dot(Error2,Error2))
Er3=np.sqrt(np.dot(Error3,Error3))
Er4=np.sqrt(np.dot(Error4,Error4))

'''
Graficación de las soluciones númericas de los 4 parametros de forma y de la solución exacta,
obtenidos estos 5 resultados anteriormente, se les pone un color diferente a cada línea 
de cada parametro de forma, y se pone la exacta como puntos solamente y un color llamativo
para diferenciarla facilmente de las soluciones numericas, se activa tambien las cuadriculas
y por ultimo se pone los titulos correspondientes de la grafica y de los ejes
'''
plt.figure()
#se gráfica la solución del primer parametro de forma con color morado
plt.plot(x,yt1,"--o",label="parámetros de forma c:"+str(c), color = 'purple')
#se gráfica la solución del segundo parametro de forma con color naranjado
plt.plot(x,yt2,"--o",label="parámetros de forma c:"+str(c2), color = 'orange')
#se gráfica la solución del tercer parametro de forma con color azul
plt.plot(x,yt3,"--o",label="parámetros de forma c:"+str(c3), color = 'blue')
#se gráfica la solución del cuarto parametro de forma con color verde
plt.plot(x,yt4,"--o",label="parámetros de forma c:"+str(c4), color = 'green')
#se gráfica la solución exacta con puntos rojos
plt.plot(x,Exacta,"or",label="Solucion exacta")
#Se le pone etiqueta al eje x
plt.xlabel('x')
# Se le pone etiqueta al eje y
plt.ylabel('y')
#se agrega una etiqueta para distinguir entre los distintos colores en la gráfica
plt.legend()
#activamos las cuadrículas
plt.grid(True)
#ponemos el título a la gráfica
plt.title('Solución con diferentes parámetros de forma.')
#mostramos la gráfica
plt.show()

'''
Graficación de los errores calculados anteriormente con la norma L2, al igual que también se activa
las cuadriculas y se pone los titulos correspondientes a la gráfica y a los ejes 
'''
plt.figure()
#se gráfica el primer error con color morado
plt.plot(x,Error1,"--o",label="parámetros de forma c:"+str(c), color = 'purple')
#se gráfica el segundo error con color naranjado
plt.plot(x,Error2,"--o",label="parámetros de forma c:"+str(c2), color = 'orange')
#se gráfica el tercer error con color azul
plt.plot(x,Error3,"--o",label="parámetros de forma c:"+str(c3), color = 'blue')
#se gráfica el cuarto error con color verde
plt.plot(x,Error4,"--o",label="parámetros de forma c:"+str(c4), color = 'green')
#Se le pone etiqueta al eje x
plt.xlabel('x')
#se le pone etiqueta al eje y
plt.ylabel('y')
#se agrega una etiqueta para distinguir entre los distintos colores en la gráfica
plt.legend()
#activamos las cuadrículas
plt.grid(True)
#ponemos el título a la gráfica
plt.title('Error local, con cada uno de los parámetros de forma.')
#mostramos la gráfica
plt.show()

#imprimir valores de norma L2
print("Errores de norma L2: \n")
print("Para el parametro de forma: "+str(c)+" es de: "+str(Er1))
print("Para el parametro de forma: "+str(c2)+" es de: "+str(Er2))
print("Para el parametro de forma: "+str(c3)+" es de: "+str(Er3))
print("Para el parametro de forma: "+str(c4)+" es de: "+str(Er4))