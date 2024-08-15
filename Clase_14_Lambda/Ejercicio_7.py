''' Cubilla Damian - 1H
7. Usa una función lambda con reduce para calcular el factorial de un número.
'''
from functools import reduce
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)  