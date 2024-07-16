''' Cubilla Damian - 1H
17. Escribir un programa que le pida al usuario que ingrese un número entero
, y luego imprima "El número es negativo" si el número es menor que cero
, "El número es cero" si el número es igual a cero, o "El número es positivo" 
si el número es mayor que cero.'''
numero_ingresado = int(input("Ingrese un número: "))
if numero_ingresado > 0:
    print("El numero es positivo")
elif numero_ingresado == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")