''' Cubilla Damian -1H
12. Dada una lista de números, imprimir la cantidad de números 
pares en la lista.
'''
lista_numeros = [2,-6,5,1,-4]
cantidad = 0
for elemento in lista_numeros:
    if(elemento % 2 == 0):
        cantidad += 1
print(f"La cantidad de numeros pares de la lista es {cantidad}")