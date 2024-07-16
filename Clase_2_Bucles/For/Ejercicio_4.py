''' Cubilla Damian - 1H
4. Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.
'''
numero_ingresado = int(input("Ingrese numero: "))
suma = 0
for elemento in range(1,numero_ingresado + 1):
    if(elemento <= numero_ingresado and elemento % 2 == 1):
        suma += elemento
print(f"La suma de los numeros impares es {suma}")