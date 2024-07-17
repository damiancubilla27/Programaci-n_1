''' Cubilla Damian - 1H
1. Crear una lista con los numeros del 1 al 10 e imprime 
solo los numeros impares.
'''
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
for elemento in lista_numeros:
    if(elemento % 2 == 1):
        print(f"{elemento}", end = " ")