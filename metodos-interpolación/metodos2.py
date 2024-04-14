# Importación las bibliotecas NumPy y Matplotlib, que se utilizan para usar matrices y realizar gráficos, respectivamente.
import numpy as np
import matplotlib.pyplot as plt

# Función de evaluación de la función de base radial (FBR) multicuadrática
def rbffunction(xev, xdat, c):
  #Calcula la distancia entre xev y xdat en la dimensión dada por la fórmula de la función de base radial multicuadrática
    rbfv = np.sqrt((xev - xdat)**2 + c**2)
    # Retorna el valor de la función de base radial.
    return rbfv

# Función construye la matriz de interpolación para la FBR.
def interpmat(xdat, c):
  # Crea una matriz cuadrada de ceros con dimensiones nd x nd, donde nd es la longitud de xdat.
    nd = len(xdat)
    mat1 = np.zeros((nd, nd), float)
    # Itera a través de cada par de puntos en xdat, calcula el valor de la función de base radial multicuadrática
    # para esos puntos y los almacena en la matriz mat1.
    for i in range(nd):
        for j in range(nd):
            mat1[i,j] = rbffunction(xdat[i], xdat[j], c)
    # Retorna la matriz de interpolación construida.
    return mat1

# Función realiza la superposición de las funciones de base radial
def rbfsuperposit(x, coef, xdat, c):
  # Inicializa un arreglo de ceros de longitud igual a la cantidad de puntos de interpolación
    y = np.zeros(len(x))
    # Itera sobre cada punto de interpolación y calcula la superposición de las funciones de base radial
    # evaluadas en los puntos xdat, ponderadas por los coeficientes dados.
    for i in range(len(x)):
        for j in range(len(xdat)):
            y[i] += coef[j] * rbffunction(x[i], xdat[j], c)
    # Retorna los valores de la superposición de funciones de base radial
    return y

# Función del algoritmo de interpolación de Newton.
def interpolacion_newton(x, y):
  # Inicializa un arreglo de coeficientes de interpolación de Newton con ceros.
    n = len(x)
    coeficientes = np.zeros(n)
    for i in range(n):
        coeficientes[i] = y[i]

    # Calcula los coeficientes del polinomio de interpolación de Newton utilizando el método recursivo
    for j in range(1, n):
      # n es el numero de puntos datos
      # calcular los coeficientes en orden descendente. Comienza desde el coeficiente de grado más alto (n-1)
      # y avanza hacia el coeficiente constante (grado 0)
        for i in range(n-1, j-1, -1):
            coeficientes[i] = (coeficientes[i] - coeficientes[i-1]) / (x[i] - x[i-j])
    # Retorna los coeficientes calculados.
    return coeficientes

# Función evalúa el polinomio de Newton en los puntos de interpolación
def evaluar_polinomio(coeficientes, x, puntos_interpolacion):
  # Inicializa un arreglo p con el valor del último coeficiente del polinomio de Newton.
    n = len(coeficientes)
    p = coeficientes[n-1] * np.ones_like(puntos_interpolacion)
    # Evalúa el polinomio de Newton en los puntos de interpolación
    for k in range(n-2, -1, -1):
        p = p * (puntos_interpolacion - x[k]) + coeficientes[k]
    # Retorna los valores del polinomio de Newton evaluado en los puntos de interpolación
    return p


# Función main(), se cargan los datos desde un archivo llamado "datos.txt",
# se calculan los coeficientes para la interpolación FBR y de Newton,
# se generan los puntos de interpolación, se evalúan los polinomios en esos puntos y finalmente se grafican los resultados

def main():
    # Cargar datos desde archivo
    datos = np.loadtxt(r"C:\Users\ALEXANDER VILLADA\OneDrive - IUE\Desktop\METODOS_NUMERICOS\dat.log.txt")
    xdat = datos[:, 0]
    ydat = datos[:, 1]

    # Parámetros para FBR
    c = 0.5

    # Construir matriz de interpolación para FBR
    matint = interpmat(xdat, c)

    # Calcular coeficientes de interpolación de FBR
    coef_fbr = np.linalg.solve(matint, ydat)

    # Algoritmo de interpolación de Newton
    coef_newton = interpolacion_newton(xdat, ydat)

    # Puntos donde se quiere evaluar la interpolación
    puntos_evaluacion = [1.5, 5.7]

    # Generar puntos para la interpolación
    puntos_interpolacion = np.linspace(min(xdat), max(xdat), 100)

    # Evaluar el polinomio de Newton en los puntos de interpolación
    p_newton = evaluar_polinomio(coef_newton, xdat, puntos_interpolacion)

    # Evaluar FBR en los puntos de interpolación
    p_fbr = rbfsuperposit(puntos_interpolacion, coef_fbr, xdat, c)

    # Evaluar interpolación en los puntos de evaluación con FBR
    interpolacion_fbr = rbfsuperposit(puntos_evaluacion, coef_fbr, xdat, c)

    # Evaluar interpolación en los puntos de evaluación con Newton
    interpolacion_newton_result = evaluar_polinomio(coef_newton, xdat, puntos_evaluacion)

    # Graficar resultados
    print("Punto 2")
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(xdat, ydat, 'bo', label='Datos originales')
    plt.plot(puntos_interpolacion, p_fbr, 'r-', label='Interpolación FBR')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación FBR')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(xdat, ydat, 'bo', label='Datos originales')
    plt.plot(puntos_interpolacion, p_newton, 'g-', label='Interpolación Newton')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación de Newton')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    print("Punto 3")
    print("Interpolación con FBR en x=1.5:", interpolacion_fbr[0])
    print("Interpolación con FBR en x=5.7:", interpolacion_fbr[1])
    print()
    print("Interpolación con Newton en x=1.5:", interpolacion_newton_result[0])
    print("Interpolación con Newton en x=5.7:", interpolacion_newton_result[1])

    # Calculamos los errores absolutos para cada interpolación
    valor_real_x1_5 = np.log(1.5)
    valor_real_x5_7 = np.log(5.7)

    error_absoluto_fbr_x1_5 = np.abs(valor_real_x1_5 - interpolacion_fbr[0])
    error_absoluto_fbr_x5_7 = np.abs(valor_real_x5_7 - interpolacion_fbr[1])

    error_absoluto_newton_x1_5 = np.abs(valor_real_x1_5 - interpolacion_newton_result[0])
    error_absoluto_newton_x5_7 = np.abs(valor_real_x5_7 - interpolacion_newton_result[1])

    # Mostramos los resultados
    print()
    print("Punto 4")
    print("Precisión de la interpolación FBR:")
    print("Para x = 1.5:", error_absoluto_fbr_x1_5)
    print("Para x = 5.7:", error_absoluto_fbr_x5_7)
    print()
    print("Precisión de la interpolación de Newton:")
    print("Para x = 1.5:", error_absoluto_newton_x1_5)
    print("Para x = 5.7:", error_absoluto_newton_x5_7)

if __name__ == "__main__":
    main()