'''Cubilla Damian - 1H
11. Escribir un programa que le pida al usuario que ingrese su edad, 
y luego imprima "Eres un niño" si la edad es menor a 12, 
"Eres un adolescente" si la edad está entre 12 y 17 inclusive, 
"Eres un adulto" si la edad está entre 18 y 64.'''
edad_ingresado = int(input("Ingrese un edad: "))
if edad_ingresado >= 18 and edad_ingresado <= 64:
    print("Eres un adulto")
elif edad_ingresado >= 12 and edad_ingresado <= 17:
    print("Eres un adolescente")
else:
    print("Eres un niño")