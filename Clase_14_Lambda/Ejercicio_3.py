''' Cubilla Damian - 1H
3. Ordena una lista de tuplas en función del segundo elemento de cada tupla.
'''
tuplas = [(1, 3), (4, 2), (2, 5), (3, 1)]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print(tuplas_ordenadas)  