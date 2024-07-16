''' Cubilla Damian - 1H
20. Escribir un programa que le pida al usuario que ingrese dos números 
enteros, y luego imprima "Los dos números son iguales" si los dos 
números son iguales, "El primer número es mayor" si el primer número 
es mayor que el segundo, o "El segundo número es mayor" si el segundo 
número es mayor que el primero.'''
numero_ingresado_uno = int(input("Ingrese un numero: "))
numero_ingresado_dos = int(input("Ingrese otro numero: "))
if numero_ingresado_uno > numero_ingresado_dos:
    print("El primer numero es mayor")
elif numero_ingresado_dos > numero_ingresado_uno:
    print("El segundo numero es mayor")
else:
    print("Los dos numeros son iguales")