''' Cubilla Damian - 1H
10. Dada una lista de números, imprimir la cantidad de números 
pares en la lista.
'''
lista_numeros = [1,2,3,25,6]
contador = 0
while contador <= len(lista_numeros) - 1:
    if(lista_numeros[contador] % 2 == 0):
        print(f"{lista_numeros[contador]}")
    contador += 1