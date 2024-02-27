import matplotlib.pyplot as plt
import numpy as np
from sympy import *


class Metodos:   # clase de -  metodos generales -
    def __init__(self,x,y,a):
        self.x=x
        self.y=y
        self.a=a
    def lagrange(self):  # metodo de lagrange 
        resultado=0
        for i in range(len(self.y)):
            valor=self.y[i]

            for j in range(len(self.y)):
                if i!=j:
                    valor*=(self.a-self.x[j])/(self.x[i]-self.x[j])
            resultado+=valor
        return resultado
    def PolLagrange(self):
        x=Symbol("x")
        polinomio=0
        for i in range(len(self.x)):
            termino=1
            for j in range(len(self.x)):
                if j!=i:
                    termino*=(x-self.x[j])/(self.x[i]-self.x[j])
            polinomio+=termino*self.y[i]
        return polinomio
    
    # el metodo de newton lo vamos a resolver a traves de las diferencias divididas
    # primero vamos a crear una tabla donde vamos a almacenar los resultados
    def tabla(self):       
        matriz=[[0]*len(self.x) for i in range(len(self.x))]
        for i in range(len(self.x)):
            matriz[i][0]=self.y[i]
        for i in range(len(self.x)):
            for j in range(1,len(self.x)):
                matriz[j][i]=(matriz[j][i-1]-matriz[j-1][i-1])/(self.x[j]-self.x[j-i])
        return matriz
    def diagonal(self):
        matriz=self.tabla()
        lista=[matriz[i][i] for i in range(len(matriz))]
        return lista
    def newton(self):
        resultado=self.diagonal()[0]
        for i in range(1,len(self.diagonal())):
            valor=self.diagonal()[i]
            for j in range(i):
                valor*=(self.a-self.x[j])
            resultado+=valor
        return resultado
    def Polnewton(self):
        x=Symbol("x")
        polinomio=self.y[0]
        for i in range(1,len(self.x)):
            factor=self.diagonal()[i]
            termino=1
            for j in range(i):
                termino*=(x-self.x[j])
            polinomio+=termino*factor
        return polinomio
    def evaluar1(self,f,x):
        return eval(f)
    def grafica(self,metodo,f):
        x=Symbol("x")
        Metodos={"1":["Interpolacion de lagrange",self.PolLagrange()],"2":["Interpolación de Newton",self.Polnewton()]}
        plt.subplots(figsize=(15,10))
        plt.grid(1)
        if metodo=="1":
             plt.title(Metodos[metodo][0])
             px=lambdify(x,Metodos[metodo][1])
        elif metodo=="2":
             plt.title(Metodos[metodo][0])
             px=lambdify(x,Metodos[metodo][1])
        xi=np.linspace(min(self.x),max(self.x),100)
        fi=px(xi)
        plt.ylabel("y")
        plt.xlabel("y")
        plt.plot(xi,fi,color="b",label="polinomio interpolador")
        plt.plot(xi,self.evaluar1(f,xi),color="r",label=f"${f}$")
        for i in range(len(self.x)):
            plt.scatter(self.x[i],self.y[i],color="purple",linewidths=4)
        plt.scatter(self.a,px(self.a),color="g",label="punto evaluado")
        plt.legend(loc="best")
        plt.show()


