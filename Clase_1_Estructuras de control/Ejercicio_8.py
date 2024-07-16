''' Cubilla Damian - 1H
8. Escribir un programa que le pida al usuario que ingrese un número entero 
positivo, y luego imprima "El número es un cuadrado perfecto" si el 
número es un cuadrado perfecto, o "El número no es un cuadrado perfecto" 
si el número no es un cuadrado perfecto.'''
numero_ingresado = int(input("Ingrese un número: "))
raiz_cuadrada = numero_ingresado ** 0.5
if raiz_cuadrada.is_integer():
    print("El número es un cuadrado perfecto")
else:
    print("El número no es un cuadrado perfecto")
