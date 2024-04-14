# este codigo es hecho por by: https://github.com/GabrielOque
# en este metodo se implementara la solucion de EDO Por el medio del metodo de diferencias finitas
# valores de frontera

import casos as ca

def case(c):
  msg = ''
  if c == 1:
    # Se definen las condiciones de frontera
    print(ca.casoa(1, 0, 0, 0))
  elif c == 2:
    print('\nDigite las condiciones de forntera a continuación:')
    a = float(input('\ta: '))
    b = float(input('\tb: '))
    c = float(input('\tc: '))
    d = float(input('\td: '))
    print(ca.casob(a, b, c, d))
  elif c == 3:
    print(ca.casoc(1, 0, 0, 0))
  elif c == 4:
    print('\nDigite las condiciones de forntera a continuación:')
    a = float(input('\ta: '))
    b = float(input('\tb: '))
    print(ca.casod(a, b, 0, 0))
  elif c == 5:
    msg = '\n\tHas salido del programa.'
    return msg

print('A continuación se ejecutará el método de diferencias finitas para resolver la EDP de Laplace, para ello se plantean diferentes condiciones de frontera que están especificadas en el documento propuesto. Seleccione alguno de los casos a ejecutar.')
print('\n\t1. Caso a\n\t2. Caso b\n\t3. Caso c\n\t4. Caso d\n\t5. Salir')
opcion = int(input('\nSeleccione una opción: '))
print(case(opcion))
while opcion != 5:
  print('Selecciones alguno de los casos a ejecutar. ')
  print('\n\t1. Caso a\n\t2. Caso b\n\t3. Caso c\n\t4. Caso d\n\t5. Salir')
  opcion = int(input('\nSeleccione una opción: '))
  print(case(opcion))