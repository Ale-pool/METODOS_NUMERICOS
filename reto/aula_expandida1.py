import numpy as np
import matplotlib.pyplot as plt

# costantes del problema

# Definir el numero de puntos, en este caso 100

n=100
L=1.0
dx=L/(n-1)  #espaciamiento entre los puntos
x=np.linspace(0,L,n) # coordenadas de los puntos

# constantes del problema

c=0.1
Ts=20.0
q=100.0
h=5.0
Tm=20

# se define una matriz (f) que contendra los coeficientes

F=np.zeros((n,n))   # matriz
DF=np.zeros((n,n))
alfa=np.zeros(n)   # array - vector
rhs=np.zeros(n)
u=np.zeros(n)
u_exact= np.zeros(n)

# funcion Multicuadrica

def fi(x,xepsi):
    r=((x-xepsi)**2)**(1.0/2.0)
    y=(c**2+r**2)**(1.0/2.0)
    return y

def dfi(x,xepsi):
    r=((x-xepsi)**2)**(1.0/2.0)
    y=(x-xepsi)/fi(x,xepsi)
    return y

def d2fi(x,xepsi):
    r=((x-xepsi)**2)**(1.0/2.0)
    y=(x-xepsi)**2/fi(x,xepsi)**3+1.0/fi(x,xepsi)
    return y

def exact_convection(x):
    c1=(q*L+q*L**2*h/2.0-h*(Ts-Tm))/(1*h*L)
    y=-q*x**2/2.0+c1*x*Ts
    return y

# se comenzara a llenar la matriz

for i in range (n):
    if i==0:
        for j in range(n):
            DF[i,j]=fi(x[i],x[j])
        rhs[i]=Ts
    if i>0 and i<n-1:
        for j in range(n):
            DF[i,j]=d2fi(x[i],x[j])
            rhs[i]=-q
    if i==n-1:
        for j in range(n):
            DF[i,j]=-dfi(x[i],x[j])-h*fi(x[i],x[j])
            rhs[i]=h*Tm

for i in range(n):
    for j in range(n):
        F[i,j]=fi(x[i],x[j])

alfa=np.linalg.solve(DF,rhs)
u=np.matmul(F,alfa)

for i in range(n):
    u_exact[i]=exact_convection(x[i])

plt.figure(1)
plt.plot(x,u,'*-')
plt.plot(x,u_exact,'--r')
plt.xlabel('x')
plt.ylabel('u')


plt.figure(2)
plt.plot(x,np.abs(u-u_exact),'r')
plt.xlabel('x')
plt.ylabel('Error Absoluto')

plt.rcParams['figure.figsize'] = (9, 9)
plt.show()

