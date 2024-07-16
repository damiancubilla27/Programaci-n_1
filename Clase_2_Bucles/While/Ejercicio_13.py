''' Cubilla Damian - 1H
13. Dada una lista de números, imprimir la cantidad de 
números negativos en la lista.
'''
lista_numeros = [1,2,-3,-25,6]
elemento = 0
while(elemento < len(lista_numeros) - 1):
    if(lista_numeros[elemento] < 0):
        print(f"{lista_numeros[elemento]}")
    elemento += 1