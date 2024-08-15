''' Cubilla Damian - 1H
1. Filtra los números pares de una lista usando una función lambda.
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  