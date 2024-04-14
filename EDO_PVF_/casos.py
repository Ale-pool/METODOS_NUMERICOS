#Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

def casoa(a, b, c, d):
  m, n = malla()
  sol = tipoPro()
  if sol == 1:
    tipo = 'Solución numérica'
    #Se crea la mantriz para los coeficientes
    Mat = matriz(m, n, 1)
    #Se define la matriz con la longitud de los valores de la malla y el vector donde se pondrán el vector de terminos independients
    Mat2 = Mat2ab(a, b, c, d, m, n)
    Vec = Vecg(a, b, c, d, m, n, 1)
    u = np.linalg.solve(Mat, Vec)
    #Se completa la matriz Mat2, la cual corresponde a los valores de U, tanto los conocidos en la frontera como también los que nos retorna el vector U
    #Este contador es usado para acceder a las posiciones del vector U e ir pasadondo estos a valores a la matriz que contiene las condiciones de frontera
    contU = 0
    for i in range(1, len(Mat2)-1):
      for j in range(1, len(Mat2)-1):
        #Se utiliza la función round para mostrar redondear los primeros 6 término después del .
        Mat2[i][j] = round(u[contU], 6)
        contU += 1
    print('\n\t{} de la EDP de Laplace utilizando aproximación centrada, utilizando las condiciones de frontera ({},{},{},{}), utilizando una malla de nodos: ({}x{})\n' .format(tipo, a, b, c, d, m, n))
    for i in Mat2:
      for j in i:
        print("\t", j, end=" ")
      print()
    X = Xvec(m, n)
    Y = Yvec(m, n)
    graficar(X, Y, Mat2, tipo, 'Caso a')
  elif sol == 2:
    tipo = 'Solución analítica'
    X = Xvec(m, n)
    Y = Yvec(m, n)
    Vsol = SolAnalitica(X, Y, m, n)
    MatSolA = Mat2ab(a, b, c, d, m, n)
    #Este contador es usado para acceder a las posiciones del vector U e ir pasadondo estosa valores a la matriz que contiene las condiciones de frontera
    contSolA = 0
    for i in range(1, len(MatSolA)-1):
      for j in range(1, len(MatSolA)-1):
        #Se utiliza la función round para mostrar redondear los primeros 6 término después del .
        MatSolA[i][j] = round(Vsol[contSolA], 6)
        contSolA += 1
    print('\n\n\t{} de la EDP de Laplace utilizando aproximación centrada, utilizando las condiciones de frontera ({},{},{},{}), utilizando una malla de nodos: ({}x{})\n' .format(tipo, a, b, c, d, m, n))
    for i in MatSolA:
      for j in i:
        print("\t", j, end=" ")
      print()
    graficar(X, Y, MatSolA, tipo, 'Caso a')
  elif sol == 3:
    tipo = 'Error relativo porcentual puntual'
    X = Xvec(m, n)
    Y = Yvec(m, n)
    Mat = matriz(m, n, 1)
    MatN = Mat2ab(a, b, c, d, m, n)
    Vec = Vecg(a, b, c, d, m, n, 1)
    u = np.linalg.solve(Mat, Vec)
    contU = 0
    for i in range(1, len(MatN)-1):
      for j in range(1, len(MatN)-1):
        #Se utiliza la función round para mostrar redondear los primeros 6 término después del .
        MatN[i][j] = round(u[contU], 6)
        contU += 1
    Vsol = SolAnalitica(X, Y, m, n)
    MatA = Mat2ab(a, b, c, d, m, n)
    contSolA = 0
    for i in range(1, len(MatA)-1):
      for j in range(1, len(MatA)-1):
        #Se utiliza la función round para mostrar redondear los primeros 6 término después del .
        MatA[i][j] = round(Vsol[contSolA], 6)
        contSolA += 1
    MatN = np.flipud(MatN)
    MatA = np.flipud(MatA)
    errorv = np.zeros((n, m))
    for i in range(1, m-1):
      for j in range(1, m-1):
        errorv[i][j] = round(np.abs(MatA[i][j] - MatN[i][j]),6)
    print('Calculo del error con respecto a la solución numérica y analítica de la EDP de Laplace:')
    for i in errorv:
      for j in i:
        print("\t", j, end=" ")
      print()
    graficar(X, Y, errorv, tipo, 'Caso a')

def casob(a, b, c, d):
  m, n = malla()
  tipo = 'Solución numérica'
  Mat = matriz(m, n, 1)
  Mat2 = Mat2ab(a, b, c, d, m, n)
  Vec = Vecg(a, b, c, d, m, n, 1)
  u = np.linalg.solve(Mat, Vec)
  #Se completa la matriz Mat2, la cual corresponde a los valores de U, tanto los conocidos en la frontera como también los que nos retorna el vector U
  #Este contador es usado para acceder a las posiciones del vector U e ir pasadondo estosa valores a la matriz que contiene las condiciones de frontera
  contU = 0
  for i in range(1, len(Mat2) - 1):
    for j in range(1, len(Mat2) - 1):
      Mat2[i][j] = round(u[contU], 6)
      contU += 1
  print('\n\t{} de la EDP de Laplace utilizando aproximación centrada, utilizando las condiciones de frontera ({},{},{},{}), utilizando una malla de nodos: ({}x{})\n' .format(tipo, a, b, c, d, m, n))
  for i in Mat2:
    for j in i:
      print("\t", j, end=" ")
    print()
  X = Xvec(m, n)
  Y = Yvec(m, n)
  graficar(X, Y, Mat2, tipo, 'Caso b')

def casoc(a, b, c, d):
  m, n = malla()
  tipo = 'Solución numérica'
  Mat = matriz(m, n, 2)
  Mat2 = Mat2ab(a, b, c, d, m, n)
  Vec = Vecg(a, b, c, d, m, n, 2)
  u = np.linalg.solve(Mat, Vec)
  #Se completa la matriz Mat2, la cual corresponde a los valores de U, tanto los conocidos en la frontera como también los que nos retorna el véctor U
  #Este contadr es usado para acceder a las posiciones del vector U e ir pasadondo estosa valores a la matriz que contiene las condiciones de frontera
  contU = 0
  for i in range(1, len(Mat2) - 1):
    for j in range(1, len(Mat2) - 1):
      Mat2[i][j] = round(u[contU], 6)
      Mat2[j][m - 1] = Mat2[j][i]
      contU += 1
  print('\n\t{} de la EDP de Laplace utilizando aproximación centrada, utilizando las condiciones de frontera ({},{},{},{}), utilizando una malla de nodos: ({}x{})\n' .format(tipo, a, b, c, d, m, n))
  for i in Mat2:
    for j in i:
      print("\t", j, end=" ")
    print()
  X = Xvec(m, n)
  Y = Yvec(m, n)
  graficar(X, Y, Mat2, tipo, 'Caso c')

def casod(a, b, c, d):
  m, n = malla()
  tipo = 'Solución numérica'
  Mat = matriz(m, n, 3)
  Mat2 = Mat2ab(a, b, c, d, m, n)
  Vec = Vecg(a, b, c, d, m, n, 3)
  u = np.linalg.solve(Mat, Vec)
  #Se completa la matriz Mat2, la cual corresponde a los valores de U, tanto los conocidos en la frontera como también los que nos retorna el véctor U
  #Este contadr es usado para acceder a las posiciones del vector U e ir pasadondo estosa valores a la matriz que contiene las condiciones de frontera
  contU = 0
  for i in range(1, len(Mat2)-1):
    for j in range(1, len(Mat2)-1):
      Mat2[i][j] = round(u[contU], 6)
      Mat2[j][0] = Mat2[j][i-(n-3)]
      contU +=1
  for i in range(0, len(Mat2)):
    for j in range(0, len(Mat2)):
      Mat2[m-1][i] = Mat2[m-2][i]
  print('\n\t{} de la EDP de Laplace utilizando aproximación centrada, utilizando las condiciones de frontera ({},{},{},{}), utilizando una malla de nodos: ({}x{})\n' .format(tipo, a, b, c, d, m, n))
  for i in Mat2:
    for j in i:
      print("\t", j, end=" ")
    print()
  #Esta es la manera de calcular el valor de h sabiendo que siempre estamos trabajando sobre una región unitaría
  X = Xvec(m, n)
  Y = Yvec(m, n)
  graficar(X, Y, Mat2, tipo, 'Caso d')

def tipoPro():
  #Seleccionar el proceso que se quiere realizar
  print('\nEscoja el tipo de proceso que se quiere realizar.')
  print('\n\t1. Solución numérica\n\t2. Solución Analítica\n\t3. Error relativo porcentual puntual')
  c = int(input('\nSeleccione una opción: '))
  if c == 1:
    return 1
  elif c == 2:
    return 2
  elif c == 3:
    return 3
  else:
    c = int(input('\nDebe seleccionar una opción que este dentro de las opciones: '))
    if c == 1:
      return 1
    elif c == 2:
      return 2
    elif c == 3:
      return 3

def malla():
  print('\nEscoja la malla de nodos a utilizar.')
  print('\n\t1. 5x5\n\t2. 11x11\n\t3. 31x31\n\t4. Ingresar una malla personalizada')
  c = int(input('\nSeleccione una opción: '))
  # Se selecciona la malla a utilizar
  if c == 1:
    m = 5
    n = 5
  elif c == 2:
    m = 11
    n = 11
  elif c == 3:
    m = 31
    n = 31
  elif c == 4:
    m = int(input('\nIngrese el valor para m: '))
    n = int(input('Ingrese el valor para n: '))
  else:
    c = int(input('\nDebe seleccionar una opción que este dentro de las opciones: '))
    if c == 1:
      m = 5
      n = 5
    elif c == 2:
      m = 11
      n = 11
    elif c == 3:
      m = 31
      n = 31
    elif c == 4:
      m = int(input('Ingrese el valor para m:'))
      n = int(input('Ingrese el valor para n'))
  return(m, n)

def SolAnalitica(X, Y, m, n):
  #Solucion analititica
  AnaliticaY = []
  AnaliticaX = []
  for i in range(1, m-1):
    for j in range(1, n-1):
      AnaliticaX.append(X[i][j])
      AnaliticaY.append(Y[i][j])
  #Valores para U de la solucion analitica
  Vsol = []
  op = 0.0
  for i in range(0, (n-2)**2):
    for j in range(1, 100):
      aux = op
      op = (4/(((2*j-1)*np.pi)*(np.sinh((2*j-1)*np.pi))))*(np.sin((2*j-1)*(np.pi*AnaliticaX[i])))*(np.sinh((2*j-1)*(np.pi*AnaliticaY[i])))
      op += aux
    Vsol.append(round(op, 6))
    op = 0.0
    aux = 0.0
  return(Vsol)

def matriz(m, n, case):
  Mat = np.zeros(((n - 2)**2, (m - 2)**2))
  #Se llena la matriz para los casos a y b
  if case == 1:
    cont1 = 0
    cont2 = 0
    #Recorrer la matriz
    for i in range(len(Mat)):
      for j in range(len(Mat)):
        #Diagonal superior
        if (i == j):
          Mat[i][j] = -4
        #Diagonales superiores e infereiores a la diagonal superior
        elif ((j - i) == (n - 2) or (i - j) == (n - 2)):
          Mat[i][j] = 1
        #Diagonal superior a la principal
        elif (j - i == 1):
          cont1 += 1
          Mat[i][j] = 1
          if (cont1 == (n - 2)):
            Mat[i][j] = 0
            cont1 = 0
        #Diagonal inferor a la princiapal
        elif (i - j == 1):
          cont2 += 1
          Mat[i][j] = 1
          if (cont2 == (n - 2)):
            Mat[i][j] = 0
            cont2 = 0
  #Se llena la matriz para el caso c
  elif case == 2:
    cont1 = 0
    cont2 = 0
    cont3 = 0
    #Recorrer la matriz
    for i in range(len(Mat)):
      for j in range(len(Mat)):
        #Diagonal superior a la principal
        if (i == j):
          cont3 += 1
          Mat[i][j] = -4
          if (cont3 == (n-2)):
            Mat[i][j] = -3
            cont3 = 0
        #Diagonales superiores e infereiores a la diagonal superior
        elif (j-i == (n-2) or i-j == (n-2)):
          Mat[i][j] = 1
        #Diagonal superior a la principal
        elif (j-i == 1):
          cont1 += 1
          Mat[i][j] = 1
          if (cont1 == (n-2)):
            Mat[i][j] = 0
            cont1 = 0
        #Diagonal inferor a la princiapal
        elif (i-j == 1):
          cont2 += 1
          Mat[i][j] = 1
          if (cont2 == (n-2)):
            Mat[i][j] = 0
            cont2 = 0
  #Se llena la matriz para el caso d
  else:
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = n-2
    #Recorrer la matriz
    for i in range(len(Mat)):
      for j in range(len(Mat)):
        #Diagonal superior a la principal
        if(i == j):
          if(i == 0 and j == 0):
            Mat[i][j] = -3
          elif(i == ((n-2)**2)-(n-2) and j == ((n-2)**2)-(n-2)):
            Mat[i][j] = -2
            cont4 -= 1
          elif(i == ((n-2)**2)-(cont4) and j == ((n-2)**2)-(cont4)):
            cont4 -= 1
            Mat[i][j] = -3
          elif(np.abs(cont3) == 4*(n-3)):
            Mat[i][j] = -3
            cont3 = 0
          else:
            Mat[i][j] = -4
            cont3 += Mat[i][j]
        #Diagonales superiores e infereiores a la diagonal superior
        elif(j-i == (n-2) or i-j == (n-2)):
          Mat[i][j] = 1
        #Diagonal superior a la principal
        elif(j - i == 1):
          cont1+=1
          Mat[i][j] = 1
          if(cont1 == (n-2)):
            Mat[i][j] = 0
            cont1 = 0
        #Diagonal inferor a la princiapal
        elif(i - j == 1):
          cont2+=1
          Mat[i][j] = 1
          if(cont2 == (n-2)):
            Mat[i][j] = 0
            cont2 = 0
  return (Mat)

def Mat2ab(a, b, c, d, m, n):
  Mat2 = np.zeros((m, n))
  #Se recorre la matriz y se llenan los nodos externos de X con los valores de frontera
  for i in range(len(Mat2)):
    Mat2[0][i] = a
    Mat2[m-1][i] = c
  #Se recorre la matriz y se llenan los nodos externos de Y con los valores de frontera
  for j in range(1, m - 1):
    Mat2[j][m-1] = b
    Mat2[j][0] = d
  return (Mat2)

def Vecg(a, b, c, d, m, n, case):
  Vec = []
  #Esta es la formúla para calcular la longitud del vector que contiene los términos independientes
  Vec = np.zeros((n-2)**2, dtype='float')
  #Se buscan los términos independientes y se agregan al vector correspondiente para los casos a y b
  if case == 1:
    for i in range(1, n-1):
      for j in range(1, m-1):
        if i == 1:
          Vec[(j-1)+(i-1)*(n-2)] -= a
        if i == n-2:
          Vec[(j-1)+(i-1)*(n-2)] -= c
        if j == 1:
          Vec[(j-1)+(i-1)*(n-2)] -= d
        if j == n-2:
          Vec[(j-1)+(i-1)*(n-2)] -= b
  #Se buscan los términos independientes y se agregan a al vector correspondiente para el caso c
  elif case == 2:
    for i in range(1, n - 1):
      for j in range(1, m - 1):
        if i == 1:
          Vec[(j-1)+(i-1)*(n-2)] -= a
        if i == n-2:
          Vec[(j-1)+(i-1)*(n-2)] -= c
        if j == 1:
          Vec[(j-1)+(i-1)*(n-2)] -= d
  #Se buscan los términos independientes y se agregan a al vector correspondiente para el caso d
  else:
    for i in range(1, n-1):
      for j in range(1, m - 1):
        if i == 1:
          Vec[(j-1)+(i-1)*(n-2)] -= a
        if j == 1:
          Vec[(j-1) + (i-1)*(n-2)] -= b
  #Se retorna en U los valores para U, estos solo son los valores desconocidos, ahora habrá que con los valores de forntera encontrar la matiz con estos valores
  return (Vec)

def Xvec(m, n):
  #Esta es la manera de calcular el valor de h sabiendo que siempre estamos trabajando sobre una región unitaría
  h = 1 / (m - 1)
  statusToHX = 0
  #Se escribe la matriz de X la cual era conocida desde el incicio
  X = np.zeros((m, n))
  for i in range(0, m):
    for j in range(0, n):
      if (i == 0 and j == 0):
        X[i][j] = statusToHX
      else:
        X[i][j] = statusToHX + h
        statusToHX += h
    statusToHX = -1 * (h)
  return (X)

def Yvec(m, n):
  h = 1 / (m - 1)
  #Se escribe la matriz de Y la cual era conocida desde el incicio
  Y = np.zeros((m, n))
  statusToHY = 1
  for i in range(0, m):
    for j in range(0, n - 1):
      if (i == 0 and j == 0):
        Y[j][i] = 1
      else:
        Y[j][i] = statusToHY - h
        statusToHY -= h
    statusToHY = 1 + h
  return (Y)

def graficar(x, y, mat, tipo, caso):
  fig = plt.figure()
  ax = plt.axes(projection='3d')
  surface = ax.plot_surface(x, y, mat, cmap='RdBu_r', rstride=1, cstride=1, linewidth=0, antialiased=False, alpha=0.8)
  ax.set_title('{} para la EDP de Laplace\nMétodo de diferencias finitas - {}'.format(tipo, caso), fontsize=12)
  ax.set_xlabel('x', fontsize=16)
  ax.set_ylabel('y', fontsize=16)
  ax.set_zlabel('Temperatura', fontsize=16)
  fig.colorbar(surface, shrink=0.8, aspect=20)
  plt.show()