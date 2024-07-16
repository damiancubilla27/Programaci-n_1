'''Cubilla Damian - 1H
2. Escribir un programa que le pida al usuario que ingrese su edad, y luego 
imprima "Eres mayor de edad" si la edad es mayor o igual a 18, o "Eres menor 
de edad" si la edad es menor a 18.
'''
edad_ingresado = int(input("Ingrese un edad: "))
if edad_ingresado >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")