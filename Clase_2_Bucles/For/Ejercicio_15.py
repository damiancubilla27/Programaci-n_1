''' Cubilla Damian - 1H
15. Dada una lista de números, imprimir la cantidad 
de números impares en la lista.
'''
lista_numeros = [2,-6,5,1,-4]
cantidad = 0
for elemento in lista_numeros:
    if(elemento % 2 == 1):
        cantidad += 1
print(f"La cantidad de numeros impares es {cantidad}")