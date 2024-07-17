''' Cubilla Damian - 1H
18. Solicitar al usuario números enteros hasta que ingrese el 0. 
Almacenar los números en una lista y luego imprimir el mayor 
(sin utilizar la función max())
'''
lista_numeros = []
numero = 1
mayor = 0
while(numero != 0):
    numero = int(input("Ingrese numero: "))
    if(numero != 0):
        lista_numeros.append(numero)
for elemento in lista_numeros:
    if(elemento > mayor):
        mayor = elemento
print(f"El numero mayor de la lista es: {mayor}")