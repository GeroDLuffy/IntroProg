# # Ejercicio 3
# # Dada una lista de N numeros, generar un vector con los numeros que sean capicuas.
# k = 0
# v = []
# n = int(input('Ingrese cantidad de numeros: '))
# for i in range(1, n+1):
#     x = int(input('Ingresar un numero: '))
#     inverso = 0
#     aux = x
#     while aux > 0:
#         r = aux % 10
#         inverso = inverso * 10 + r
#         aux = aux // 10
#     if aux == inverso:
#         k += 1
#         v[k] = x

# for i in range(1, k+1):
#     print(v[i])

# # Ejercicio 4
# # Dado dos vectores A y B que contienen cada uno un número natural positivo, se pide componer un nuevo numero, de acuerdo al siguiente ejemplo:
# # A = [5, 3], B = [7, 2] -> C = 5237

# # Ejercicio 6

gr = int(input('Ingrese el grado del polinomio: '))
vector = []
inicio = 0
final = len(vector) - 1
for i in range(1, gr+1):
    ti = int(input(f'Ingrese el termino independiente del grado {i+1}: '))
    vector += [ti]
    while inicio < final:
        vector[inicio], vector[final] = vector[final], vector[inicio]
        inicio += 1
        final -= 1

print(vector)