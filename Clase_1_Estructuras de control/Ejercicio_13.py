''' Cubilla Damian - 1H
13. Escribir un programa que le pida al usuario que ingrese un número entero
, y luego imprima "El número es divisible por 3 y por 5" si el número es
divisible por 3 y por 5, o "El número no es divisible por 3 y por 5" si
el número no es divisible por 3 y por 5.'''
numero_ingresado = int(input("Ingrese un número: "))
if numero_ingresado % 3 == 0 and numero_ingresado % 5 == 0:
    print("El numero es divisible por 3 y por 5")
else:
    print("El numero no es divisible por 3 y por 5")