import numpy as np
import Euler as Eu
import matplotlib.pyplot as plt

# def fld (t,y1,y2):
#     return y1-y2+ 2*t-1*t**2-1*t**3
# def fld1 (t,y1,y2):
#     return y1+ y2 -4*t**2+1*t**3
def Func2 (t,y1,y2):
    return -0.6*y2-8*y1
def Func1 (t,y1,y2):
    return y2   
def exac (x):
    return -x**4/2 + 4*x**3-10*x**2+17*x/2+1
def fun3 (x,y):
    return -2*x**3+12*x**2-20*x+8.5
t_0 = 0
y1_0 = 1

T = 4
hp = 0.5
 
nit = int((T-t_0)/hp)

teu,y1eu = Eu.euler_meth1(fun3,t_0,y1_0,nit,hp)
teum,yeum = Eu.euler_Mejorado_meth(fun3,t_0,y1_0,nit,hp)
teum1,yeum1 = Eu.euler_Mejorado_meth1(fun3,t_0,y1_0,nit,hp)
print(teum)
print(yeum)


tex = np.linspace(t_0,T,200)
yex = np.zeros(len(tex))
for i in range (len(tex)):
    yex[i] = exac(tex[i])

plt.figure()
plt.plot(teu,y1eu,'--', label = 'Y1')
plt.plot(tex,yex,'k', label = 'Solucion exacta')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Soluciones númericas del PVI planteado')
plt.grid(True)

plt.figure()
plt.plot(teum,yeum,'--', label = 'Metodo Euler Mejorado Heun')
plt.plot(tex,yex,'k', label = 'Solucion exacta')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Soluciones númericas del PVI planteado')
plt.grid(True)

plt.figure()
plt.plot(teum1,yeum1,'--', label = 'Metodo Euler Mejorado Punto medio')
plt.plot(tex,yex,'k', label = 'Solucion exacta')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Soluciones númericas del PVI planteado')
plt.grid(True)

plt.tight_layout()
plt.show()
