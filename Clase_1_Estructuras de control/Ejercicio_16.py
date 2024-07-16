''' Cubilla Damian - 1H
16. Escribir un programa que le pida al usuario que ingrese su nombre y su edad, 
y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive, 
"Eres adulto" si la edad está entre 18 y 64 inclusive, o "Eres adulto mayor" 
si la edad es mayor o igual a 65.'''
nombre_ingresado = input("Ingrese nombre: ")
edad_ingresado = int(input("Ingrese un edad: "))
if edad_ingresado >= 13 and edad_ingresado <= 17:
    print(f"Eres un adolescente, {nombre_ingresado}")
elif edad_ingresado >= 18 and edad_ingresado <= 64:
    print(f"Eres un adulto, {nombre_ingresado}")
elif edad_ingresado >= 65:
    print(f"Eres adulto mayor, {nombre_ingresado}")
else:
    print(f"Eres un bebe")