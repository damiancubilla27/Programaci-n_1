''' Cubilla Damian - 1H
16. Dada una lista de números, imprimir todos los números 
que son múltiplos de 3.
'''
lista_numeros = [1,2,-3,-25,6]
elemento = 0
while(elemento < len(lista_numeros) - 1):
    if(lista_numeros[elemento] % 3 == 0):
        print(f"{lista_numeros[elemento]}")
    elemento += 1
