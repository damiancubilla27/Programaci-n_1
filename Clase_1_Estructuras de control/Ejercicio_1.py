'''Cubilla Damian - 1H
1. Escribir un programa que le pida al usuario que ingrese un número entero 
positivo, y luego imprima "El número ingresado es positivo" si el número es 
mayor que cero, o "El número ingresado es cero o negativo" si el número es 
menor o igual a cero'''

numero_ingresado = int(input("Ingrese un numero: "))
if numero_ingresado > 0:
    print("El numero ingresado es positivo")
else:
    print("El numero ingresado es cero o negativo")