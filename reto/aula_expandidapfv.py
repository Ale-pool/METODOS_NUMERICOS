

import numpy as np
import matplotlib.pyplot as plt

x0=1.0  # punto inicial
L=2.0 # punto final
n= 10 # numero de nodos en nuestro dominio
x=np.linspace(x0,L,n)
c=0.1

# datos en relacion al ejercicio evaluado
h=10.
B=0.02
w=0.2
p= 2*B+2*w
Ac= B*w
k=20.
m=np.sqrt(h*p/k/Ac) 
thb=0.
thl=0.638961
# definicion de la funcion multicuadrica
# r(distancia euclidiana) ; c(parametro de forma)
def fmq(r,c):
    f=np.sqrt(r**2+c**2)
    return f

def d2fmq(r, c):
    f= 1./fmq(r,c)-r**2/fmq(r,c)**3
    return f


def d1fmq(r, dx, c):
    f=dx/fmq(r,c)
    return f

# vamos a recorrer los nodos con el indicador i

psi= np.zeros((n,n))
A=np.zeros((n,n))
B=np.zeros(n)

for i in range(n):
    xi= x[i]
    for j in range(n):
        ej=x[j]           # con este se podra hallar la distacia euclidiana
        # r=np.sqrt(np.dot(xi-ej,xi-ej)) # producto punto - 2d - 3d
        r=np.abs(xi-ej)  # 1-D
        psi[i,j]=fmq(r,c)   # matriz que nos permitira encontrar la solucion a partir de los coeficientes
        if i==0:
            A[i,j]=fmq(r,c)       # matriz colocacion A
        elif i==n-1:             
            A[i,j]=fmq(r,c)
        else:
            A[i,j]=xi**2*d2fmq(r,c)+xi*d1fmq(r,xi-ej,c)+fmq(r,c)

if i==0:
    B[i]=thb
elif i==n-1:
    B[i]= thl  # calcula el vector B
else:
    B[i]=0.0
alpha=np.linalg.solve(A,B) # solucionador para sistemas de ecuaciones lineales
th=np.matmul(psi,alpha)    # matmul - multiplicador matricial  --- solucion numerica


# tha= thb*np.exp(-m*x) # solucion analitica
tha=np.sin(np.log(x))
er=np.abs(tha-th)
plt.figure()
plt.plot(x,th,'b.',label='numerica')
plt.plot(x,tha,label='Analitica')
plt.xlabel('x[m]')
plt.ylabel('th[°C]')
plt.legend()
plt.show()


plt.figure(2)
plt.plot(x,er,'--.',label='numerica')
plt.xlabel('x[m]')
plt.ylabel('error[°C]')
plt.legend()
plt.show()