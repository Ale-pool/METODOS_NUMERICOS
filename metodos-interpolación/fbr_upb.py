
# programa que evalua la función RBF multicuadrica

import numpy as np
import matplotlib.pyplot as plt

# definir el dominio
xm = 1.
n= 20  # numero definido de donos

x=np.linspace(-xm,xm,n)  # definición de nuestro dominio en un rango de -1 y 1

c=1. # parametro de forma  (parametro de forma)
m =1     # constante de fbr

# funcion multicuadra

def mq(r,c):
    f=np.sqrt(r**2+c**2)
    return f

r=np.abs(x)  # vector radar de r
fmq=mq(r,c)