''' Cubilla Damian - 1H
7. Dada una lista de números, imprimir todos los números que 
son mayores que el promedio de la lista.
'''
lista_numeros = [1,2,3,25,5]
elemento = 0
suma = 0
promedio = 0
while(elemento <= len(lista_numeros) - 1):
    suma += lista_numeros[elemento]
    elemento += 1
promedio = suma / len(lista_numeros)
elemento = 0
while(elemento <= len(lista_numeros) - 1):
    if(lista_numeros[elemento] > promedio):
        print(f"El numero {lista_numeros[elemento]} es mayor al promedio {promedio}")
    elemento += 1
