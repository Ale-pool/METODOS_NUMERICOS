"""
Fuente(1) : https://correoiueedu-my.sharepoint.com/personal/jmgranados_correo_iue_edu_co/_layouts/15/stream.aspx?id=%2Fpersonal%2Fjmgranados%5Fcorreo%5Fiue%5Fedu%5Fco%2FDocuments%2FAula%20Expandida%2FSesion%202%5FV2%2FS2P2%5FInterpolacion%5FRBF%5Fcodigo%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview
Fuente(2) : https://correoiueedu-my.sharepoint.com/personal/jmgranados_correo_iue_edu_co/_layouts/15/stream.aspx?id=%2Fpersonal%2Fjmgranados%5Fcorreo%5Fiue%5Fedu%5Fco%2FDocuments%2FAula%20Expandida%2FSesion%202%5FV2%2FS2P3%5FInterpolacion%5FRBF%5Fprecisi%C3%B3n%5FRecortado%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview
Autor : Julian mauricio granados
"""


import numpy as np
import matplotlib.pyplot as plt

# esta funcion nos servira para evaluar las FBR
# cada FBR se debe evaluar en un punto de prueba(xev) , punto de evaluación(xdat) y el parametro de forma(c)

def rfbfunction(xev,xdat,c):
    rbfv=np.sqrt((xev-xdat)**2 + c**2)
    return rbfv

# construccion de la matriz de interpolacion
# Las entradas de las matriz de interpolacion son las FIBR evaluadas en xev y xdat

def interpmat(xdat, c):
    nd = len(xdat)
    mat1 = np.zeros((nd,nd),float)
    for i in range(nd):
        for j in range(nd):
            mat1[i,j] = rfbfunction(xdat[i], xdat[j],c)
    return mat1

# superposicion de funciones de base radial

def rbfsuperposit(x, coef, xdat, c):
    y = np.zeros((len(x)))
    for i in range (len(x)):
        for j in range (len(xdat)):
            y[i] += coef[j]*rfbfunction(x[i], xdat[j], c)  # Corrección: acumular en lugar de sobrescribir
    return y

# información de entrada
datos = np.loadtxt(r"C:\Users\ALEXANDER VILLADA\OneDrive - IUE\Desktop\METODOS_NUMERICOS\dat_cos.txt")
xdat = datos[:,0]
ydat = datos[:,1]
c = 0.4 # parametro de forma

# matriz de interpolacion 
matint =  interpmat(xdat, c)

# coeficientes de la interpolacion
coef = np.linalg.solve(matint, ydat)

# evaluacion de la superposicion sobre un intervalo
x = np.arange(-2, 2.05, 0.05)
yinterp = rbfsuperposit(x, coef, xdat, c)     

# video 2 == simetria de cada FBR respecto a l dato o al punto que es el centro de la función ===
fbr1 = rfbfunction(x, xdat[0], c)
fbr2 = rfbfunction(x, xdat[1], c)
fbr3 = rfbfunction(x, xdat[2], c)
fbr4 = rfbfunction(x, xdat[3], c)

# calculo del error RMs entre la 
# interpolacion y la funcion dada
Err = np.sqrt(np.sum((yinterp - (np.cos(x))**10)**2)/len(yinterp))
print('parametros de la forma: ', c)
print('Error RMS de la proximación: ', Err)


# sumas parciales de la interpolación 

yinterp6 = rbfsuperposit(x, coef[0:6], xdat[0:6], c)
yinterp7 = rbfsuperposit(x, coef[0:7], xdat[0:7], c)
yinterp8 = rbfsuperposit(x, coef[0:8], xdat[0:8], c)
# graficas

# === video 2 ===

plt.figure()
plt.plot(x, (np.cos(x))**10, label = 'Funcion dada')
plt.plot(x, yinterp6, label = 'interpolacion RBF, 6 terminos')
plt.plot(x, yinterp7, label = 'interpolacion RBF, 7 terminos')
plt.plot(x, yinterp8, label = 'interpolacion RBF, 8 terminos')
plt.plot(x, yinterp, label= 'interpolacion RFB')
plt.plot(xdat, ydat, 'or', label = 'Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title("sucecion de sumas parciales con RBF")



plt.figure()
plt.plot(x, (np.cos(x))**10, label = 'Funcion dada')
plt.plot(x, fbr1, label = 'RBF1 evaluado en el intervalo de interes')
plt.plot(x, fbr2, label = 'RBF2 evaluado en el intervalo de interes')
plt.plot(x, fbr3, label = 'RBF3 evaluado en el intervalo de interes')
plt.plot(x, fbr4, label = 'RBF4 evaluado en el intervalo de interes')
plt.plot(xdat, ydat, 'or', label = 'Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title("RBF utilizadas en la interpolacion")




plt.figure()
plt.plot(x, np.cos(x)**10, label = 'Funcion dada')
plt.plot(x, yinterp, label = 'interpolacion RBF')
plt.plot(xdat, ydat, 'or', label = 'Datos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title("Interpolación con funciones de base radial")


plt.show()