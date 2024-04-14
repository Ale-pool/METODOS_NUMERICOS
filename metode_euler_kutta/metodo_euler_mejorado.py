# METODO DE EULER MEJORADO CON RUNGE KUTTA DE CUARTO ORDEN
# importaciones de las librerias a usar
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from sympy import init_printing

# ingreso de los  valores de entrada 
x,y = symbols('x,y')
# recomendaciones

print(" ============================================== ")
print("Dirección de ingreso de los datos")
print(" Los términos de la expresión deben ir con un * entre ellos")
print(" para usar una raiz cuadrada, use sqrt()")
print(" para las funciones trigonometricas, use: cos(), sin(), tan()")
print(" para usar una función exponencial, use exp \n")
print(" =============================================  ")

# ejemplo de implementación
print(" Resolución de la ecuación diferencial ordinaria de la forma y'= f(x,y) ")
while True:
    try:
        z=eval(input("ingrese una funcion f(x,y): "))
        pprint(z)
        break
    except:
        print("la funcion tiene problema en la sintaxis")
        print(" Ingrese de Nuevo la función ")


xi=float(input(' ingrese el valor inicial de xo: '))
yi=float(input('ingrese el valor inicial de yo: '))

while True:
    h=float(input("ingrese el tamaño de paso h:  "))
    if h<=0:
        print(" El tamaño no puede ser cero o negativo")
    else:
        break

xn=float(input(' Ingrese el valor a calcular y(xn): '))
print("")
itc=round(((xn-xi)/h))
vx=[]
vy=[]

# seleccion de evaluacion del metodo a usar

while True:
    while True:
        print("Seleccione el metodo a usar")
        print("1: Metodo de euler mejorado")
        print("2: Metodo de runge kutta (cuarto orden)")
        eleccion=int(input("eleccion: "))
        print("")
        if (eleccion!=1 and eleccion!=2):
            print("Valor incorrecto, ingresele de nuevo")
        else:
            break

# metodo de euler mejorado
    if eleccion==1:
        print("======== Tabla de Valores =====")
        print("{:^10}{:^10}{:^10}".format("i","x","y"))
        for i in range(1,itc+1):
            f1=z.subs([(x,xi+h),(y,yi)])
            u=yi+h*f1
            f2=z.subs([(x,xi+h),(y,u)])
            yn=yi+h*((f1+f2)/2)
            print("{:^10}{:^10}{:^10}".format(i,round(xi+h,5),yn))
            print("")
            yi=yn
            xi=round(xi+h,5)
            vx.append(xi)
            vy.append(yi)
        plt.xticks(vx)
        plt.title("Metodo de euler Mejorado")
    #Metodo de runge kutta de cuarto orden
    else:
        print(" ============== Tabla de valores ======")
        print("{:^10}{:^10}{:^10}".format("i","x","y"))
        for i in range(1,itc+1):
            k1=z.subs([(x,xi),(y,yi)])                # error en el valor de subs
            k2=z.subs([(x,xi+h/2),(y,yi+(h*k1)/2)])   # f1=z.subs([(x,xi+h),(y,yi)])
            k3=z.subs([(x,x+h/2),(y,yi+(h*k2)/2)])
            k4=z.subs([(x,xi+h),(y,yi+h*k3)])
            yn=yi+(k1+2*k2+2*k3+k4)*(h/6)
            print("{:^10}{:^10}{:^10}".format(i,round(xi+h,5),yn))
            print("")
            xi=round(xi+h,5)
            yi=yn
            vx.append(xi)
            vy.append(yi)
        plt.xticks(vx)
        plt.title("metodo de runge kutta de cuarto orden")
        print("===========paso1===================")
        
#proceso de grafica de la función    # por aqui no esta entrando el metodo
        print('Valor aproximado: ',yn)
        plt.xlabel("eje x")
        plt.ylabel("eje y")
        plt.plot(vx,vy,color='red')
        plt.grid()
        plt.show()
        continuar=input(" Quiero validar otro metodo? ")
        if continuar=="S" or continuar=="SI" or continuar=="si" or continuar=="n" or continuar=="N" or continuar=="NO" or continuar=="no":
            while True:
                try:
                    z=eval(input("ingrese una funcion f(x,y): "))
                    pprint(z)
                    break
                except:
                    print("la funcion no tine la sintaxis correcta")
                    print("ingrese de nuevo la función")
            xi=float(input('ingrese el valor inicial xo: '))
            yi=float(input("Ingrese el valor inicial de yo: "))
            h=0
            while True:
                h=float(input("ingrese el tamaño de paso h:  "))
                if h<=0:
                    print(" El tamaño no puede ser cero o negativo")
                else:
                    break
            xn=float(input(' Ingrese el valor a calcular y(xn): '))
            print("")
            itc=round(((xn-xi)/h))
            vx=[]
            vy=[]
        else:
            print("Finalización del prgrama, gracias")
            break

                
                