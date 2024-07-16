''' Cubilla Damian - 1H
1. Dada una lista de números, imprimir el número más grande de la lista
'''
lista_numeros = [1,2,6,5,4]
mayor = 0
for numero in lista_numeros:
    if(mayor < numero):
        mayor = numero
print(f"El numero mayor es {mayor}")