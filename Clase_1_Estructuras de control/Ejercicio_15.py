'''Cubilla Damian - 1H
15. Escribir un programa que le pida al usuario que ingrese un número entero 
positivo, y luego imprima "El número es primo" si el número es primo, o "El 
número no es primo" si el número no es primo.'''
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True
numero_ingresado = int(input("Ingrese un número: "))
if es_primo(numero_ingresado):
    print("El número es primo")
else:
    print("El número no es primo")
