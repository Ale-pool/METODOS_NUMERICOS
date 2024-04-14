
print ("------- Interpolacion Polinomica (Newton) -------")
n = int(input("Ingrese el grado del polinomio a evaluar: "))+1

matriz = [0.0] * n
for i in range(n):
    matriz[i] = [0.0] * n

vector = [0.0] * n

print (matriz)
print (vector)
for i in range(n):
    x = input("Ingrese el valor de x: ")
    y = input("Ingrese el valor de f("+x+"): ")
vector[i]=float(x)
matriz[i][0]=float(y)

print (vector)
print (matriz)

punto_a_evaluar = float(input("Ingrese el punto a evaluar: "))

print ("------------------------------")
print ("------- Calculando ... -------")
print ("------------------------------")

for i in range(1,n):
    for j in range(i,n):
         print ("i=",i," j=",j)
print ("(",matriz[j][i-1],"-",matriz[j-1][i-1],")/(",vector[j],"-",vector[j-i],")")
matriz[j][i] = ( (matriz[j][i-1]-matriz[j-1][i-1]) / (vector[j]-vector[j-i]))
print ("matriz[",j,"][",i,"] = ",(matriz[j][i-1]-matriz[j-1][i-1])/(vector[j]-vector[j-i]))

print ("------------------------------")
print ("------------------------------")
for i in range(n):
    print (matriz[i])
print ("------------------------------")
print ("------------------------------")

aprx = 0
mul = 1.0
for i in range(n):
    print ("matriz[",i,"][",i,"]","=",matriz[i][i])
mul = matriz[i][i]
print ("mul antes del ciclo j=",mul)
for j in range(1,i+1):
    mul = mul * (punto_a_evaluar - vector[j-1])
print ("mul en el ciclo j=",mul)
aprx = aprx + mul

print ("------------------------------")
print ("------------------------------")
print ("El valor aproximado de f(",punto_a_evaluar,") es: ", aprx)