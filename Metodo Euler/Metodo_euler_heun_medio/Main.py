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
def ejercio_7(t,p):
    return 0.026 * (1-(p/12000))*p
t_0 = 1950
y1_0 = 2555

T = 2000
hp = 10

 
nit = int((T-t_0)/hp)

teu,y1eu = Eu.euler_meth1(ejercio_7,t_0,y1_0,nit,hp)
teum,yeum = Eu.euler_Mejorado_meth(ejercio_7,t_0,y1_0,nit,hp)
teum1,yeum1 = Eu.euler_Mejorado_meth1(ejercio_7,t_0,y1_0,nit,hp)
print("Euler mejorado Heun")
print(teum)
print(yeum)
print("Euler mejorado punto medio")
print(teum1)
print(yeum1)

# tex = np.linspace(t_0,T,200)
# yex = np.zeros(len(tex))
# for i in range (len(tex)):
#     yex[i] = exac(tex[i])
tex = [1950,1960,1970,1980,1990,2000]
yex = [2555,3040,3708,4454,5276,6079]

plt.figure()
plt.plot(teu,y1eu,'--', label = 'Metodo Euler con el paso')
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
