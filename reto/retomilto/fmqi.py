import numpy as np

def fmqi(r, c):
    f= np.sqrt(r**2+c**2)**-1
    return f

def dfmqi(r, c):
    f = -(r / (r**2 + c**2)**3/2)
    return f
def d2fmqi(r, c):
    f = -(1/(r**2 + c**2)**3/2) + ((3*r**2) / (r**2 + c**2)**5/2)
    return f