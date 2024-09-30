# Ejercicio 7
# Dado un vector con N números, eliminar los elementos repetidos del vector de acuerdo a:
# a. Usando vector auxiliar
# b. Sin usar vector auxiliar.

# a)
# n = int(input('Ingrese cantidad de numeros en el vector: ')) 
# vector = []
# for i in range(n):
#     nro = int(input(f'Ingrese numero {i+1}: '))
#     if nro not in vector:
#         vector += [nro]
#     else:
#         print(f'Numero {nro} repetido.')

# print(f'\nVector sin numeros repetidos: {vector}')

# Usando random
# import random 
# n = int(input('Ingrese cantidad de numeros en el vector: '))
# vector = []
# contRepetidos = 0
# vectorRepetidos = []
# for i in range(n):
#     nro = random.randint(1, 10000)
#     if nro not in vector:
#         vector += [nro]
#     else:
#         contRepetidos += 1
#         vectorRepetidos += [nro]

# print(f'Vector: {vector}')
# print(f'\nVector repetidos: {vectorRepetidos}')
# print(f'Cantidad de repetidos: {contRepetidos}')

# b (idk if can make it this way)
# n = int(input('Ingrese cantidad de numeros en el vector: '))
# vector = []
# for i in range(n):
#     nro = int(input('Ingrese numero: '))
#     vector += [nro]

# vectorAux = []
# for numero in vector:
#     if numero not in vectorAux:
#         vectorAux += [numero]

# print(f'Vector sin repetidos: {vectorAux}')

# # Ejercicio 8
# # Realizar los siguientes metodos:
# # a. Busqueda -> 1. Busqueda lineal / 2. Busqueda binaria
# # b. Ordenamiento -> 1. Por seleccion / 2. Por insercion / 3. Por burbuja

# b.1) Por seleccion
# n = int(input('Cantidad de numeros para el vector: '))
# x = [None] * n
# for i in range(n):
#     x[i] = int(input(f'Numero {i+1}: '))
# print(f'Vector sin ordenar: {x}')
# for i in range(0, n-1):
#     for j in range(i + 1, n):
#         if x[i]>x[j]:
#             aux = x[i]
#             x[i] = x[j]
#             x[j] = aux
# print(f'\nVector ordenado: {x}')

# b.3) Por burbuja
# n = int(input('Cantidad de numeros en vector: '))
# x = [None] * n
# for i in range(n):
#     x[i] = int(input(f'Numero {i + 1}: '))
# print(f'Vector sin ordenar: {x}')

# for i in range(0, n):
#     for j in range(0, n - i - 1):
#         if x[j] > x[j + 1]:
#             aux = x[j]
#             x[j] = x[j + 1]
#             x[j + 1] = aux
# print(f'Vector ordenado: {x}')

# # Parte 2
# # Ejercicio 2
# # Tiene una lista de números enteros, ordenar la misma de mayor a menor.
# # Mostrar en cada paso como va quedando el vector. Aplicar el método de 
# # Selección y el de la Burbuja.

# print(' - Ordenamiento por Seleccion - ')
# n = int(input('Cantidad de numeros para el vector: '))
# x = [None] * n
# for i in range(n):
#     x[i] = int(input(f'Numero {i+1}: '))
# print(f'Vector sin ordenar: {x}\n')

# for i in range(0, n-1):
#     for j in range(i + 1, n):
#         if x[i] < x[j]:
#             aux = x[i]
#             x[i] = x[j]
#             x[j] = aux
#             print(f'Vector en ordenamiento: {x}')
# print(f'\nVector ordenado de mayor a menor: {x}')

# print(' - Ordenamiento por Burbuja -')
# n = int(input('Cantidad de numeros en vector: '))
# x = [None] * n
# for i in range(n):
#     x[i] = int(input(f'Numero {i + 1}: '))
# print(f'Vector sin ordenar: {x}\n')

# for i in range(0, n):
#     for j in range(0, n - i - 1):
#         if x[j] < x[j + 1]:
#             aux = x[j]
#             x[j] = x[j + 1]
#             x[j + 1] = aux
#             print(f'Vector en ordenamiento: {x}')
# print(f'\nVector ordenado de mayor a menor: {x}')

# # Ejercicio 3
# # Dada una lista de N números ordenados, insertar M números en los 
# # lugares que corresponda de tal manera que la lista preserve el orden.
# # Conviene usar insercion / No esta terminado

# Ordenamiento por Insercion
# n = int(input('Cantidad de numeros en vector: '))
# x = [None] * n
# for i in range(n):
#     x[i] = int(input(f'Numero: {i + 1}: '))
#     v = x[i]
#     j = i - 1
#     while j >= 0 and x[j] > v:
#         x[j + 1] = x[j]
#         j = j - 1
#         x[j + 1] = v
# print(f'Vector ordenado: {x}')

# # Ejercicio 4
# # En una lista de palabras, contar cuantas vocales y consonantes tiene cada
# # palabra. Mostrar además de cada vocal encontrada la posición de esa vocal 
# # dentro de la palabra. Usar la función length.

# cntdPal = int(input('Ingrese la cantidad de palabras que desea ingresar: '))
# lista = []
# vocales = ['a', 'e', 'i', 'o', 'u']
# consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
# contVocalesPal, contConsonantesPal = 0, 0
# contVocalesTotal, contConsonantesTotal = 0, 0
# for i in range(cntdPal):
#     pal = input(f'Ingrese palabra {i + 1}: ')
#     lista += [pal]

# for palabra in lista:
#     for letra in palabra:
#         if letra in vocales:
#             contVocalesPal += 1
#             contVocalesTotal += 1
#         else:
#             contConsonantesPal += 1
#             contConsonantesTotal += 1
#     print(f'La palabra "{palabra}", tiene {contVocalesPal} vocales y {contConsonantesPal} consonantes. ')
#     contVocalesPal, contConsonantesPal = 0, 0
    
# print(f'\nCantidad de vocales totales: {contVocalesTotal}')
# print(f'Cantidad de consonantes totales: {contConsonantesTotal}')

# # Ejercicio 5
# # Realizar un programa que permita determinar de una lista de palabras, cuales son palíndromas.
# vectorPalabras = []
# cntd = int(input('Cantidad de palabra que va a ingresar: '))

# for i in range(cntd):
#     palabra = input(f'Ingrese palabra {i + 1}: ')
#     vectorPalabras += [palabra]

# for palabra in vectorPalabras:
#     strAux = ''
#     for letra in range(len(palabra)):
#         strAux += palabra[len(palabra) - 1 - letra]
        
#     if palabra == strAux:
#         print(f'La palabra {palabra} es palindroma.')
#     else:
#         print(f'La palabra {palabra} no es palindroma.')

# # Ejercicio 6
# # Dadas dos listas de caracteres de m y n elementos. Determinar que caracteres de la lista 1 se encuentran en la lista 2.
cntd1 = int(input('Cantidad de caracteres en lista 1: '))
cntd2 = int(input('Cantidad de caracteres en lista 2: '))
m, n = [], []

for i in range(cntd1):
    car = input(f'Ingrese caracter {i + 1} lista 1: ')
    while len(car) != 1:
        print('Se pidio caracter.')
        car = input(f'Ingrese caracter {i + 1}: ')
    m += [car]

for j in range(cntd2):
    car2 = input(f'Ingrese caracter {j + 1} lista 2: ')
    while len(car2) != 1:
        print('Se pidio caracter.')
        car2 = input(f'Ingrese caracter {j + 1}: ')
    n += [car2]

for caracter in n:
    if caracter in m:
        print(f'\nCaracter {caracter} se encuentra en la lista 2.')
