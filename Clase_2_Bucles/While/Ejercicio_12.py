''' Cubilla Damian - 1H
12. Dado un número entero n, imprimir la suma de todos los 
números impares menores o iguales a n.
'''
numero_ingresado = int(input("Ingrese numero: "))
suma_impares = 0
contador = 1

while contador <= numero_ingresado:
    suma_impares += contador
    contador += 2

print(f"La suma de todos los números impares menores o iguales a {numero_ingresado} es: {suma_impares}")