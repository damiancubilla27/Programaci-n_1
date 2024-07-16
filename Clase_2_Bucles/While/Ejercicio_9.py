''' Cubilla Damian - 1H
9. Dado un número entero n, imprimir todos los números impares 
menores o iguales a n.
'''
numero_ingresado = int(input("Ingrese numero: "))
contador = 1

while contador <= numero_ingresado:
    print(f"{contador}")
    contador += 2

