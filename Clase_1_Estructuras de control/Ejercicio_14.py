''' Cubilla Damian - 1H
14. Escribir un programa que le pida al usuario que ingrese un número entero
, y luego imprima "El número es múltiplo de 4 y de 6" si el número es 
múltiplo de 4 y de 6, o "El número no es múltiplo de 4 y de 6" si el 
número no es múltiplo de 4 y de 6.'''
numero_ingresado = int(input("Ingrese un número: "))
if numero_ingresado % 4 == 0 and numero_ingresado % 6 == 0:
    print("El numero es multiplo de 4 y de 6")
else:
    print("El numero no es multiplo de 4 y 6")