''' Cubilla Damian - 1H
9. Dada una lista de números, imprimir la cantidad de números negativos 
en la lista.'''
lista_numeros = [2,-6,5,1,-4]
cantidad = 0
for elemento in lista_numeros:
    if(elemento < 0):
        cantidad += 1
print(f"La cantidad de numeros negativos es {cantidad}")