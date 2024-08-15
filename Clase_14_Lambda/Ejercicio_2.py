''' Cubilla Damian - 1H
2. Usa una función lambda para elevar al cuadrado cada número en una lista.
'''
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  