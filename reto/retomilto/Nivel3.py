#Se importa la libreria necesaria
import numpy as np

# Indicador de tipo de condición de frontera en el etremo derecho del intervalo
ind_bc = 0

# Parámetros de la Ecuación diferencial
D = 2
U = 4
k = 5

# Coeficientes de la función trigonométrica (Caso 3)
a = 3
b = 6

# Valor de la condición de frontera en el extremo izquierdo
ca=0.2
# Valor de la condición de frontera en el extremo derecho
cb=0.9

'''
La función `funcld` toma tres argumentos: `a`, `b` y `x`.
El argumento `a` es la amplitud de la función seno, el argumento `b` es la frecuencia de la 
función seno y el argumento `x` es el valor de entrada.
La función `funcld` devuelve el valor de la función seno en el punto `x`.
'''
def funcld(a, b, x):
    y = a*np.sin(b*x)
    return y
'''
La función `ode` toma dos argumentos, `x` e `y`, y devuelve un array de dos elementos. 
La función `ode` se utiliza para resolver una ecuación diferencial ordinaria (EDO).
'''
def ode(x, y):
    return np.array([y[1], (U/D)*y[1] + (k/D)*y[0] + funcld(a,b,x)/D])

'''
La función `bc` toma dos argumentos, `ya` e `yb`, y devuelve un array de dos elementos. 
El primer elemento es la diferencia entre el primer elemento de `ya` y `ca`, y el segundo 
elemento es la diferencia entre el elemento `ind_bc` de `yb` y `cb`. La función `bc` se utiliza 
para calcular las condiciones de contorno para una ecuación diferencial
'''
def bc(ya, yb):
    return np.array([ya[0] - ca, yb[ind_bc] - cb])

#Se define la función de base radial multicuádrica inversa
def fmqi(r,c):
    return 1/np.sqrt(c**2 + r**2)
#Primera derivada de la funcion de base radial multicuádrica inversa
def Pdfmqi(r,c):
    return (-r / (r**2 + c**2)**3/2)
#Segunda derivada de la funcion de base radial multicuádrica inversa.
def Sdfmqi(r,c):
    return -(1/(r**2 + c**2)**3/2) + ((3*r**2) / (r**2 + c**2)**5/2)

'''
La función `sfbd` toma como entrada un array `x` de valores de la variable independiente, }
un valor `ca` para la condición de frontera en el extremo izquierdo del dominio, un valor `cb` 
para la condición de frontera en el extremo derecho del dominio, un entero `n` que especifica 
el número de puntos a utilizar, y un valor `c` que especifica el parámetro de la función de base 
radial multicuádrica inversa. La función devuelve un array `y` que contiene los valores 
de la solución de la EDO en los puntos.
'''
def sfbd(x,ca,cb,n,c):
    #La línea de código "A=np.zeros((n,n))" crea una matriz de ceros de tamaño n x n. La matriz A 
    # se utiliza para almacenar los coeficientes de la ecuación que se está resolviendo.
    A=np.zeros((n,n))
    #Coeficientes independientes.
    B=np.zeros(n)
    #Valores de r evaluados en la función de base radial.
    Vr=np.zeros((n,n))
    #Ciclo para llenar el vector y la matriz de coeficientes.
    for i in range(n):
        xi=x[i]
        # Valores en la frontera.
        #como es el primer punto va a ser igual a la condición de frontera en el extremo izquierdo
        if i==0: B[i]=ca
        #como es el último punto va a ser igual a la condición de frontera en el extremo derecho
        elif i==n-1:B[i]=cb
        #Si no es un valor de la frontera, se evaluara con el lado derecho de la ecuacion.   
        else: B[i]= a * np.sin(b*x[i])
        #ciclo para la matriz de coeficientes
        for j in range(n):
            #epsilon
            ep=x[j]
            #calcula la distancia radial entre el punto xi y el punto ep. 
            r=np.abs(xi-ep)
            #evalúa la función de base radial multicuádrica inversa en el punto (r,c).
            Vr[i,j]=fmqi(r,c)
            #valores de la frontera
            #al ser el primer valor se evalua solamente con la función sin derivar
            if i==0: A[i,j]=fmqi(r,c)
            #al ser el último valor se evalua solamente con la función sin derivar
            elif i==n-1: A[i,j]=fmqi(r,c)
            
            #Valores entre la frontera
            #Al ubicarse entre las fronteras se evalua con la ecuación correspondiente del ejercicio
            else:
                A[i,j]= (D * Sdfmqi(r,c)) - (U * Pdfmqi(r,c)) - (k * c)
    #Valor de cada alfa.          
    alfa=np.linalg.solve(A,B)
    #Para encontrar los valores de y.
    y=np.matmul(Vr,alfa)
    #Retorna el posicionamiento en Y de la solución.
    return y 
