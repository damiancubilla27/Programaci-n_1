''' Cubilla Damian - 1H
7. Dado un número entero n, imprimir la secuencia de números impares menores
o iguales a n.'''
numero_ingresado = int(input("Ingrese numero: "))
for elemento in range(1,numero_ingresado + 1):
    if(elemento <= numero_ingresado and elemento % 2 == 1):
        print(f"{elemento}")
