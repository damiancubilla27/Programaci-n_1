''' Cubilla Damian - 1H
3. Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.
'''
numero_ingresado = int(input("Ingrese numero: "))
for elemento in range(1,numero_ingresado + 1):
    if(elemento <= numero_ingresado and elemento % 2 == 0):
        print(f"{elemento}")