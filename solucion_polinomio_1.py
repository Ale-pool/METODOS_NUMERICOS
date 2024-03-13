import matplotlib.pyplot as plt
import numpy as np

 # cargar los respectivos datos desde una dirección local
datos = np.loadtxt(r"C:\Users\ALEXANDER VILLADA\OneDrive - IUE\Desktop\METODOS_NUMERICOS\tarea2.txt")    
valores_x = datos[:, 0]
valores_y = datos[:, 1]

# Calcular los coeficientes del polinomio
grado_polinomio = len(valores_x)-1 # Elegir el grado del polinomio
#Numpy polyfit() es un método que ajusta los datos dentro de una función polinómica
coeficientes = np.polyfit(valores_x, valores_y, grado_polinomio)

# Función para evaluar el polinomio
def interpolacion_polinomio(valor_a_interpolar):
  return np.polyval(coeficientes, valor_a_interpolar)
#https://www.geeksforgeeks.org/numpy-polyval-in-python/

# definir la cantidad de valores a interpolar
cantidad_valores = len(valores_x)

# definir los valores a interpolar
valores_a_interpolar = valores_x

# Interpolar los valores y mostrar los resultados
valores_interpolados = []  # Lista para almacenar los valores interpolados
for valor in valores_a_interpolar:
  valor_interpolado = interpolacion_polinomio(valor)
  valores_interpolados.append(valor_interpolado)
  print(f"Interpolación en {valor}: {valor_interpolado}")

# Rango para la interpolación
valores_x_interpolacion = np.linspace(min(valores_x), max(valores_x), 100)  # Crear 100 puntos entre mínimo y máximo de valores_x
valores_y_interpolados = interpolacion_polinomio(valores_x_interpolacion)

# Diagrama de la interpolación
plt.plot(valores_x, valores_y, 'o', label='Datos muestrales')
plt.plot(valores_x_interpolacion, valores_y_interpolados, label='Curva interpolada')
plt.scatter(valores_a_interpolar, valores_interpolados, marker='x', color='red', label='Valores interpolados')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Interpolación de Polinomio')
plt.legend()
plt.grid(True)

# Mostrar el diagrama
plt.show()
