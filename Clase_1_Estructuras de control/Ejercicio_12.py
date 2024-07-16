''' Cubilla Damian - 1H
12. Escribir un programa que le pida al usuario que ingrese dos números 
enteros, y luego imprima "El primer número es positivo" si el primer 
número es mayor que cero, "El segundo número es positivo" si el segundo 
número es mayor que cero, o "Ambos números son negativos" si los 
dos números son negativos'''
numero_ingresado_uno = int(input("Ingrese un número: "))
numero_ingresado_dos = int(input("Ingrese otro número: "))
if numero_ingresado_uno > 0:
    print("El primer numero es positivo")
elif numero_ingresado_dos > 0:
    print("El segundo numero es positivo")
else:
    print("Ambos numeros son negativos")