'''Cubilla Damian - 1H
3. Escribir un programa que le pida al usuario que ingrese un número entero, 
y luego imprima "El número ingresado es par" si el número es divisible por 2, 
o "El número ingresado es impar" si el número no es divisible por 2
'''
numero_ingresado = int(input("Ingrese un numero: "))
if numero_ingresado % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")