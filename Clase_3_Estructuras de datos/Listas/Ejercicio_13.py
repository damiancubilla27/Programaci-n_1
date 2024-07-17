''' Cubilla Damian - 1H
13. Crea una lista de números y encuentra el promedio de todos 
los números en la lista.
'''
lista_numeros = [1,2,3,10]
suma = 0
promedio = 0
for elemento in lista_numeros:
    suma += elemento
promedio = suma / len(lista_numeros)
print(f"El promedio de los numeros de la lista es: {promedio}")