''' Cubilla Damian 1H
4. Dada una lista de números, imprimir la suma de todos los elementos de la lista.
'''
lista_numeros = [1,2,3,4,5]
elemento = 0
suma = 0
while(elemento <= len(lista_numeros) - 1):
    suma += lista_numeros[elemento]
    elemento += 1
print(suma)