''' Cubilla Damian - 1H
6. Dado un número entero n, imprimir la suma de todos los números
pares menores o iguales a n.'''
numero_ingresado = int(input("Ingrese numero: "))
suma_pares = 0
contador = 2

while contador <= numero_ingresado:
    suma_pares += contador
    contador += 2

print(f"La suma de todos los números pares menores o iguales a {numero_ingresado} es: {suma_pares}")