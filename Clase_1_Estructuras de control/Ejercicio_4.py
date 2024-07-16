'''Cubilla Damian - 1H
4. Escribir un programa que le pida al usuario que ingrese dos números enteros
, y luego imprima "El primer número es mayor" si el primer número es mayor que
el segundo, "El segundo número es mayor" si el segundo número es mayor que el
primero, o "Los dos números son iguales" si los dos números son iguales.'''
numero_ingresado_uno = int(input("Ingrese un numero: "))
numero_ingresado_dos = int(input("Ingrese otro numero: "))
if numero_ingresado_uno > numero_ingresado_dos:
    print("El primer numero es mayor")
elif numero_ingresado_dos > numero_ingresado_uno:
    print("El segundo numero es mayor")
else:
    print("Los dos numeros son iguales")