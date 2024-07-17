''' Cubilla Damian - 1H
3. Crear una lista vacia y pide al usuario que ingrese 
numeros enteros hasta que ingrese un numero negativo. Luego,
muestra la suma de todos los numeros ingresados.
'''
lista_numeros = []
numero = 0
suma = 0
while(numero >= 0):
    numero = int(input("Ingrese numero: "))
    if(numero >= 0):
        lista_numeros.append(numero)
for elemento in lista_numeros:
    suma += elemento
print(f"La suma de los numeros es: {suma}")