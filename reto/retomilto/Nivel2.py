import numpy as np
import matplotlib.pyplot as plt

#Datos iniciales  
Xa=1
ca=0.5
n=10
Xb=2
cb=0.69

#Parametros de forma
c=0.01
c2=0.63
c3=0.9
c4=0.7
c5=0.54

# Definimos el sistema de ecuaciones
M = np.array([[np.exp(Xa), np.exp(-Xa)], [np.exp(Xb), -np.exp(-Xb)]])
N = np.array([ca, cb])

# Resolvemos el sistema de ecuaciones
sol = np.linalg.solve(M, N)

# Obtenemos los valores de M y N
M_val = sol[0]
N_val = sol[1]

#Funciones a definir, donde r es la distacia euclidiana y c el parametro de forma.
def fg(r,c):#Funcion de base radial gaussiana, np.exp=constante e.
    return 1/np.sqrt(c**2 + r**2)

def fgPd(r,c):#Primera derivada de la funcion de base radial gaussiana.
    return (-r / (r**2 + c**2)**3/2)

def fgSd(r,c):#Segunda derivada de la funcion de base radial gaussiana.
    return -(1/(r**2 + c**2)**3/2) + ((3*r**2) / (r**2 + c**2)**5/2)

# Definimos la función de la solución analítica
def solucionAnalitica(x):
    return M_val * np.exp(x) + N_val * np.exp(-x)
    
def fbr(Xa,ca,Xb,cb,n,c):#Solucion funcion de base radial
    #Matriz de coeficientes (estas son la funciones evaluadas en las diferentes deivadas,  
    #recordando que las funciones de frontera se evalúan en la función de base radial sin derivar).
    A=np.zeros((n,n))

    #Coeficientes independientes.
    B=np.zeros(n)

    #Valores de r evaluados en la función de base radial.
    Vr=np.zeros((n,n))
    
    #Valores que se remplazaran en x.
    x = np.linspace(Xa,Xb,n)

    #Ciclo para llenar el vector y la matriz de coeficientes.
    for i in range(n):
        xi=x[i]
        # Valores en la frontera.
        if i==0: B[i]=ca
        elif i==n-1:B[i]=cb

        #Si no es un valor de la frontera, se evaluara con el lado derecho de la ecuacion.   
        else: B[i]= 0.0

        for j in range(n):#estos son los valores que toma epsilon.
            ep=x[j]#Epsilon

            r=np.abs(xi-ep)#Distancia euclidiana.
            Vr[i,j]=fg(r,c)

            #valores de la frontera
            #Notese que se evaluan en la funcion de base radial radial gaussiana sin derivar.
            if i==0: A[i,j]=fg(r,c)
            elif i==n-1: A[i,j]=fg(r,c)
            
            #Valores entre la frontera
            else:
                A[i,j]= (2 * fgSd(r,c)) - (4 * fgPd(r,c))
                
    alfa=np.linalg.solve(A,B)#Valor de cada alfa.
    y=np.matmul(Vr,alfa)#Para encontrar los valores de y.

    return x,y #Retorna el posicionamiento en X y en Y de la solución.
#Llamar la función para cada uno de los parámetros de forma.
[x,yt1]=fbr(Xa,ca,Xb,cb,n,c)
[x,yt2]=fbr(Xa,ca,Xb,cb,n,c2)
[x,yt3]=fbr(Xa,ca,Xb,cb,n,c3)
[x,yt4]=fbr(Xa,ca,Xb,cb,n,c4)
[x,yt5]=fbr(Xa,ca,Xb,cb,n,c5)

#Solución exacta
Exacta=solucionAnalitica(x)

#Determina el error local con cada uno de los parámetros de forma
Errory1=np.abs(Exacta-yt1)
Errory2=np.abs(Exacta-yt2)
Errory3=np.abs(Exacta-yt3)
Errory4=np.abs(Exacta-yt4)
Errory5=np.abs(Exacta-yt5)

#dot=producto punto; sqrt=raiz cuadrada; norma de error
Er1=np.sqrt(np.dot(Errory1,Errory1))
Er2=np.sqrt(np.dot(Errory2,Errory2))
Er3=np.sqrt(np.dot(Errory3,Errory3))
Er4=np.sqrt(np.dot(Errory4,Errory4))
Er5=np.sqrt(np.dot(Errory5,Errory5))

plt.figure()
plt.plot(x,yt1,"--o",label="parámetros de forma c:"+str(c))
plt.plot(x,yt2,"--o",label="parámetros de forma c:"+str(c2))
plt.plot(x,yt3,"--o",label="parámetros de forma c:"+str(c3))
plt.plot(x,yt4,"--o",label="parámetros de forma c:"+str(c4))
plt.plot(x,yt5,"--o",label="parámetros de forma c:"+str(c5))
plt.plot(x,Exacta,"or",label="Solucion exacta")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Solución con diferentes parámetros de forma.')
plt.show()

plt.figure()
plt.plot(x,Errory1,"--o",label="parámetros de forma c:"+str(c))
plt.plot(x,Errory2,"--o",label="parámetros de forma c:"+str(c2))
plt.plot(x,Errory3,"--o",label="parámetros de forma c:"+str(c3))
plt.plot(x,Errory4,"--o",label="parámetros de forma c:"+str(c4))
plt.plot(x,Errory5,"--o",label="parámetros de forma c:"+str(c5))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Error local, con cada uno de los parámetros de forma.')
plt.show()

#imprimir valores de norma L2
print("Errores de norma L2: \n")
print("Para el parametro de forma: "+str(c)+" es de: "+str(Er1))
print("Para el parametro de forma: "+str(c2)+" es de: "+str(Er2))
print("Para el parametro de forma: "+str(c3)+" es de: "+str(Er3))
print("Para el parametro de forma: "+str(c4)+" es de: "+str(Er4))
print("Para el parametro de forma: "+str(c5)+" es de: "+str(Er5))