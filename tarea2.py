# Tarea-2 de metodos numericos
# integrantes : Cristian ocampo, Yeiver, Valentina, Alexander villada
"""
Este código realiza la interpolación de datos utilizando tres métodos diferentes: 
interpolación de Newton, interpolación de Lagrange 
interpolación basada en funciones de base radial (FBR).


"""
import numpy as np
import matplotlib.pyplot as plt

# se define rbffunction que calcula el valor de la funcion de base radial
def rbffunction(xev, xdat, c):
    rbfv = np.sqrt((xev - xdat)**2 + c**2)
    return rbfv

 # se define la funcion interpmat que construye una matriz de interpolacion de FBR
def interpmat(xdat, c):
    nd = len(xdat)
    mat1 = np.zeros((nd, nd), float)
    
    for i in range(nd):
        for j in range(nd):
            mat1[i,j] = rbffunction(xdat[i], xdat[j], c)

    return mat1
  # esto nos permite calcular la superposición de funciones de base radial para un conjunto de puntos 
def rbfsuperposit(x, coef, xdat, c):
  
    y = np.zeros(len(x))

    for i in range(len(x)):
        for j in range(len(xdat)):
            y[i] += coef[j] * rbffunction(x[i], xdat[j], c)
    # Retorna los valores de la superposición de funciones de base radial
    return y

#  implementamos el algoritmo de interpolación de Newton para calcular los coeficientes del polinomio interpolador
def interpolacion_newton(x, y):

    n = len(x)
    coeficientes = np.zeros(n)
    for i in range(n):
        coeficientes[i] = y[i]

    for j in range(1, n):

        for i in range(n-1, j-1, -1):
            coeficientes[i] = (coeficientes[i] - coeficientes[i-1]) / (x[i] - x[i-j])

    return coeficientes


#  evaluamos el  polinomio dados sus coeficientes en un conjunto de puntos dados.
def evaluar_polinomio(coeficientes, x, puntos_interpolacion):

    n = len(coeficientes)
    p = coeficientes[n-1] * np.ones_like(puntos_interpolacion)

    for k in range(n-2, -1, -1):
        p = p * (puntos_interpolacion - x[k]) + coeficientes[k]
   
    return p

# Función para calcular el polinomio de Lagrange
def lagrange_interpolacion(x, y, x_eval):
    # Inicializar la lista de términos del polinomio de Lagrange
    lagrange_terms = []
    
    # Iterar sobre cada punto de datos
    for i in range(len(x)):
        # Inicializar el término del polinomio de Lagrange en el punto i
        term = 1
        
        # Iterar sobre cada punto de datos excepto el punto i
        for j in range(len(x)):
            if j != i:
                # Calcular el término del polinomio de Lagrange en el punto x_eval
                term *= (x_eval - x[j]) / (x[i] - x[j])
        
        # Agregar el término del polinomio de Lagrange a la lista
        lagrange_terms.append(term)
    
    # Inicializar el valor del polinomio de Lagrange en el punto x_eval
    lagrange_value = 0
    
    # Calcular el valor del polinomio de Lagrange en el punto x_eval sumando los términos
    for i in range(len(x)):
        lagrange_value += y[i] * lagrange_terms[i]
    
    # Retornar el valor del polinomio de Lagrange en el punto x_eval
    return lagrange_value

  #  realiza la interpolación utilizando el método de Lagrange para un conjunto de puntos conocidos xi, sus correspondientes valores fxi, y un punto x para el cual queremos interpolar.
def interpolacion(x, xi, fxi):
    # Obtenemos el numero de puntos conocidos
    n = len(xi)
    # Inicializamos el valor de la interpolación
    polinomio = 0
    for i in range(0, n, 1):
        denominador = 1
        numerador = 1
        for j in range(0, n, 1):
            # Para cada punto conocido excepto i
            if (i != j):
                # Calculamos el termino de lagrange y lo multiplicamos por el producto de lagrange
                numerador *= (x - xi[j])
                denominador *= (xi[i] - xi[j])
            termino = (numerador / denominador) * fxi[i]
            # Sumamos el producto de los terminos de lagrange al valor interpolado
        polinomio += termino
    return polinomio


def main():
    # cargar los respectivos datos desde una dirección local
    datos = np.loadtxt(r"C:\Users\ALEXANDER VILLADA\OneDrive - IUE\7 SEMESTRE\BASE DE DATOS NO EXTRUCTURADAS\Documents\quiz\tarea2.txt")
    xdat = datos[:, 0]
    ydat = datos[:, 1]

    # Parámetros para FBR
    c = 0.5

    fbrmat = interpmat(xdat, c)   # construccion de la matriz de interpolacion para el poli de FBR

    #  se calcula los respectivos coeficientes de FBR 
    fbr_co = np.linalg.solve(fbrmat, ydat)

    # Interpolacion de newton algoritmo
    newton_cof = interpolacion_newton(xdat, ydat)

    # se presenta los puntos a evaluar 
    puntos_evaluacion = [1.5, 5.7]

     # realizar puntos de interpolacion
    puntos_interpolacion = np.linspace(min(xdat), max(xdat), 100)

    # se evalua el polinomio de newton en los respectivos puntos 
    int_newton = evaluar_polinomio(newton_cof, xdat, puntos_interpolacion)

    # se evalua el polinomio de lagrange 
    int_lagrange = interpolacion(newton_cof, xdat, puntos_interpolacion)

    # se evalua el polinomio de FBR en los puntos
    int_fbr = rbfsuperposit(puntos_interpolacion, fbr_co, xdat, c)

    # hallar la  interpolación en los puntos de evaluación con FBR
    fbr_interpol = rbfsuperposit(puntos_evaluacion, fbr_co, xdat, c)

    # hallar la  interpolación en los puntos de evaluación con Newton
    newton_interpol = evaluar_polinomio(newton_cof, xdat, puntos_evaluacion)

    # Interpolación de Lagrange en los puntos de evaluación
    lagrange_interpol = [lagrange_interpolacion(xdat, ydat, x_eval) for x_eval in puntos_evaluacion]
    
    print("Desarrollo de los datos")

    print("Interpolación con FBR en x=1.5:", fbr_interpol[0])
    print("Interpolación con FBR en x=5.7:", fbr_interpol[1])
    print()
    print("Interpolación con Newton en x=1.5:", newton_interpol[0])
    print("Interpolación con Newton en x=5.7:", newton_interpol[1])
    print()
    print("Interpolación con Lagrange en x=1.5:", lagrange_interpol[0])
    print("Interpolación con Lagrange en x=5.7:", lagrange_interpol[1])

    # en este parte se calcula cada uno de los errores en base a los polimios (FBR, NEWTON, LAGRANGE), en los puntos dados
    valor_real_x1_5 = np.log(1.5)
    valor_real_x5_7 = np.log(5.7)

    err_ab_fbr_x1_5 = np.abs(valor_real_x1_5 - fbr_interpol[0])
    err_ab_fbr_x5_7 = np.abs(valor_real_x5_7 -  fbr_interpol[1])

    err_ab_newton_x1_5 = np.abs(valor_real_x1_5 - newton_interpol[0])
    err_ab_newton_x5_7 = np.abs(valor_real_x5_7 - newton_interpol[1])

    err_ab_lagrange_x1_5 = np.abs(valor_real_x1_5 - lagrange_interpol[0])
    err_ab_lagrange_x5_7 = np.abs(valor_real_x5_7 - lagrange_interpol[1])

    # se muestra los diferentes datos 
    print()
    print("Precisión de la interpolación FBR:")
    print("Para x = 1.5:", err_ab_fbr_x1_5)
    print("Para x = 5.7:", err_ab_fbr_x5_7)
    print()
    print("Precisión de la interpolación de Newton:")
    print("Para x = 1.5:", err_ab_newton_x1_5)
    print("Para x = 5.7:", err_ab_newton_x5_7)
    print()
    print("Precisión de la interpolación de lagrange")
    print("para x = 1.5:", err_ab_lagrange_x1_5)
    print("para x en 5.7:", err_ab_lagrange_x5_7)

      
    # respectiva grafica de los polinomios a interpolar 
    print("GRAFICAS GENERALES")
    

    
    plt.figure()
    plt.plot(xdat, ydat, 'bo', label='Datos originales')
    plt.plot(puntos_interpolacion, int_fbr, 'r-', label='Interpolación FBR')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación FBR')
    plt.legend()
    plt.grid(True)

   
    plt.figure()
    plt.plot(xdat, ydat, 'bo', label='Datos originales')
    plt.plot(puntos_interpolacion, int_newton, 'g-', label='Interpolación Newton')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación de Newton')
    plt.legend()
    plt.grid(True)

    # plt.subplot(1, 2, 3)  # Este debería ser el tercer subplot
    # plt.figure()
    # plt.plot(xdat, ydat, 'bo', label='Datos originales')
    # plt.plot(puntos_interpolacion, int_lagrange, 'm-', label='Interpolación de Lagrange')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Interpolación de Lagrange')
    # plt.legend()
    # plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()  


