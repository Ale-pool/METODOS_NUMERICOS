import numpy as np
import matplotlib.pyplot as plt
import Nivel_3 as N3

'''  En esta parte del desarrollo del codigo se llama a la clase Nivel_3 para obtener los resultados y graficarlos 
     el alias N3 nos permite acceder a las funciones y variables contenidas en el modulo Nivel_3
     Se define cuatro parametros (c1,c2,c3,c4) y se obtienen los resultados de la FBR con cada uno de ellos 
    por ende se utiliza las funciones definidas en el módulo N3 para calcular las soluciones de la ecuación diferencial 
    para cada valor de c.
    
    Utiliza la función N3.aprox_exac() para obtener la solución exacta de la ecuación diferencial y la almacena en las
    variables x e yr.
    tambien quisimos mostrar Calcula el error RMS y el error absoluto para cada solución aproximada 
    (u1, u2, u3, u4) en comparación con la solución exacta (yr). En resumen, este código calcula las 
    soluciones aproximadas de una ecuación diferencial para diferentes valores de un parámetro,
    calcula el error en estas soluciones en comparación con la solución exacta y luego grafica las soluciones y los errores.'''
c1 = 0.6
c2 = 1
c3 = 1.5
c4 = 2

# Grafica las soluciones aproximadas y la solución exacta en una figura utilizando matplotlib.pyplot.
# Grafica el error absoluto en otra figura
# Grafica el error RMS en otra figura.
u1 = N3.FBR(c1,N3.fx,N3.D,N3.fi,N3.dfi,N3.d2fi)
u2 = N3.FBR(c2,N3.fx,N3.D,N3.fi,N3.dfi,N3.d2fi)
u3 = N3.FBR(c3,N3.fx,N3.D,N3.fi,N3.dfi,N3.d2fi)
u4 = N3.FBR(c4,N3.fx,N3.D,N3.fi,N3.dfi,N3.d2fi)
x,yr = N3.aprox_exac()
n = len(u1)
for i in range (n):
    erroRMS1=100*((u1[i]-yr[i])**2/n)**1/2
    erroRMS2=100*((u2[i]-yr[i])**2/n)**1/2
    erroRMS3=100*((u3[i]-yr[i])**2/n)**1/2
    erroRMS4=100*((u4[i]-yr[i])**2/n)**1/2

plt.figure()
plt.plot(x,u1,'b-',label="FBR con parametro c1" + str(c1), color='purple')
plt.plot(x,u2,'c-',label="FBR con parametro c2" + str(c1), color='orange')
plt.plot(x,u3,'g-',label="FBR con parametro c3" + str(c1), color='blue')
plt.plot(x,u4,'y-',label="FBR con parametro c4" + str(c1), color='green')
plt.plot(x,yr,'r',label= "Aproximación de la funcion exacta")
plt.xlabel('x')
plt.ylabel('U(x)')
plt.title('Solución con diferentes parámetros de forma.')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(x,np.abs(u1-yr),'b',label="Error abs con parametro c1") # Aquí se traza el error absoluto para el primer conjunto de soluciones aproximadas (u1) en función de la posición x. Se utiliza el c
plt.plot(x,np.abs(u2-yr),'c',label="Error abs con parametro c2") # Aquí se traza el error absoluto para el segundo conjunto de soluciones aproximadas (u2) en función de la posición x. Se utiliza el c
plt.plot(x,np.abs(u3-yr),'g',label="Error abs con parametro c3")
plt.plot(x,np.abs(u4-yr),'y',label="Error abs con parametro c4")
plt.xlabel('x')
plt.ylabel('Error Absoluto')
plt.title('Error Absoluto, para cada uno de los parametros de forma.')
plt.legend()
plt.grid(True)
# esta figura queremos representar a traves de los puntos el error RMS, lo que se evaluo fue poner en el eje de la "x"
# el mismo punto para que fuese una linea vertical y lo que representara un cambio fuese la "y" la cual representa el valor
# Rms de cada parametro de forma, de esto modo en relacion a la grafica el punto mas bajo corresponderia a la solucion 
# exacta y el punto mas alto corresponde a la solución menos precisa

plt.figure()
plt.plot(1,erroRMS1,'ob',label="Error RMS con parametro c1")
plt.plot(1,erroRMS2,'oc',label="Error RMS con parametro c2")
plt.plot(1,erroRMS3,'og',label="Error RMS con parametro c3")
plt.plot(1,erroRMS4,'oy',label="Error RMS con parametro c4")
plt.xlabel('x')
plt.ylabel('Error RMS')
plt.legend()
plt.grid(True)
plt.title('Error RMS, para cada uno de los metodos de forma.')
plt.tight_layout()
plt.show()

# #imprimir valores de norma RMS: 
print("Errores de norma RMS: \n")
print("Para el parametro de forma: "+str(c1)+" es de: "+str(erroRMS1))
print("Para el parametro de forma: "+str(c2)+" es de: "+str(erroRMS2))
print("Para el parametro de forma: "+str(c3)+" es de: "+str(erroRMS3))
print("Para el parametro de forma: "+str(c4)+" es de: "+str(erroRMS4))

