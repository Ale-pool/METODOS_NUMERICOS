'''
Integrantes :

- Isabela Gomez Ruiz
- CRISTIAN DAVID OCAMPO URIBE
- CRISTIAN TRONCOSO GUERRA
- ALEXANDER VILLADA BERRIO

'''

# Con la solucion de este reto, queremos resolver una ecuación diferencial 
# utilizando el método de la integral de contorno (BVP) y comparar la solución obtenida con una solución aproximada.

# se importan las Bibliotecas necesarias 

import numpy as np
from scipy.integrate import solve_bvp

D_ = 5/2 #Derivada de la funcion D(x)
ca=1.5 # Valor de condicion de frontera izquierda
qb=0 # Valor de condicion de frontera derecho
n=100 # Definimos el numero de puntos, en este caso 100
xa = 1 #Condición de frontera izquierda
xb=3 # #Condición de frontera izquierda
def FBR(c,fx,D,fi,dfi,d2fi):
  xa = 1 #Condición de frontera izquierda
  xb=3 # #Condición de frontera izquierda
  x=np.linspace(xa,xb,n) # coordenadas de los puntos
  # Coeficientes de la función trigonométrica en la funcion fx
  a = 2
  b = 4 
  # se define una matriz (f) que contendra los coeficientes
  F=np.zeros((n,n))   # matriz que contendra las Equivalencias de C sin derivar
  DF=np.zeros((n,n)) #Matriz que contendra las ecuacianes eqivalentes de C sin o con derivadas primeras o segundas
  alfa=np.zeros(n)   # array - vector que contendra los valores de alfa para la FBR
  rhs=np.zeros(n) #Vector que contendra las valores del lado derecho ca,fx(x) o qb
  u=np.zeros(n) #Vactor solución de la FBR equivalente a la funcion C sin derivar
  for i in range (n):
    if i==0:
        for j in range(n):
            DF[i,j]=fi(x[i],x[j],c)
        rhs[i]=ca
    if i>0 and i<n-1:
        for j in range(n):
            DF[i,j]=D(i)*d2fi(x[i],x[j],c)+D_*dfi(x[i],x[j],c)
            rhs[i]=fx(a,b,i)
    if i==n-1:
        for j in range(n):
            DF[i,j]=dfi(x[i],x[j],c)
            rhs[i]=qb

  for i in range(n):
    for j in range(n):
        F[i,j]=fi(x[i],x[j],c)

  alfa=np.linalg.solve(DF,rhs)
  u=np.matmul(F,alfa)
  return u
def fx(a, b, x): #Función del lado derrecho
  y = a*np.tanh(b*((x-1)/2)**2)
  return y 
def D(x): #Fución D(x) simplificada con los valores de g y h
    return (5*x+7)/2
# funcion Multicuadrica Inversa

def fi(x,xepsi,c):
    r=((x-xepsi)**2)**(1.0/2.0)
    y= 1/np.sqrt(c**2 + r**2)
    return y

def dfi(x,xepsi,c):
    r=((x-xepsi)**2)**(1.0/2.0)
    y= (-r / (r**2 + c**2)**3/2)
    return y

def d2fi(x,xepsi,c):
    r=((x-xepsi)**2)**(1.0/2.0)
    y =-((r**2+c**2)-3*r**2)/(r**2+c**2)**5/2
    return y
def ode(x,y):
  return np.array([y[1],(2*np.tanh(4*((x-1)**2))-D_*y[0])/D(x)])
def bc(ya, yb):
  return np.array([ya[0] - ca, yb[0] - qb])  
def aprox_exac():
  x = np.linspace(xa, xb, n)
  y0 = np.ones((2, n))
  sol = solve_bvp(ode, bc, x, y0)
  yr = sol.y[0]
  return x,yr
