import numpy as np
import matplotlib.pylab as plt
import fmqi as fmqi

xa = 0.
xb = 0.9
n = 10

x=np.linspace(xa,xb,n)
c = 0.29
thb = 1.
thl = 0.


U = np.zeros(n)
si=np.zeros((n,n))
A=np.zeros((n,n))
B=np.zeros(n)
for i in range(n):
    xi=x[i]
    for j in range(n):
        U[j] = (3 * (((x[j] - xa) / (xb - xa))**2)) + 2
        ej=x[j]
        r = np.abs(xi - ej) 
        si[i,j]=fmqi.fmqi(r,c)
        if i==0:
            A[i,j]=fmqi.fmqi(r,c)    
        elif i==n-1:
            A[i,j]=fmqi.fmqi(r,c)
        else:
            A[i,j]= (3 * fmqi.d2fmqi(r,c)) - (U[j] * fmqi.dfmqi(r,c)) - (17 * c)
            
    if i==0:
        B[i]=thb
    elif i==n-1:
        B[i]=thl
    else:
        B[i]=0.0

alpha=np.linalg.solve(A,B)
th=np.matmul(si,alpha)

plt.figure()
plt.plot(x,th,label='Númerica')
plt.xlabel('x')
plt.ylabel('th')
plt.legend()
plt.show()