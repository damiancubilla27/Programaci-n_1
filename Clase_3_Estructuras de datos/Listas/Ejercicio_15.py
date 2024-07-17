''' Cubilla Damian - 1H
15. Crea una lista de números enteros y luego encuentra 
la suma de los números en índices impares.
'''
lista_numero = [1,2,3,4,5,6,7,8,9,10]
suma = 0
for elemento in range(len(lista_numero)):
    if(elemento % 2 == 1):
        suma += lista_numero[elemento]
print(f"La suma de indices impares es: {suma}")