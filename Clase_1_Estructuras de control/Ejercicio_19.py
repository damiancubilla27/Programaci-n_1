''' Cubilla Damian - 1H
19. Escribir un programa que le pida al usuario que ingrese su edad, y 
luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, 
"Eres adolescente" si la edad está entre 13 y 17 inclusive, 
o "Eres menor de edad" si la edad es menor que 13.'''
edad_ingresado = int(input("Ingrese un edad: "))
if edad_ingresado >= 18:
    print(f"Eres un adulto")
elif edad_ingresado >= 13 and edad_ingresado <= 17:
    print(f"Eres un adolescente")
elif edad_ingresado < 13:
    print(f"Eres menor de edad")
