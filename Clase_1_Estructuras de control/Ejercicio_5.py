'''Cubilla Damian - 1H
5. Escribir un programa que le pida al usuario que ingrese su nombre, 
y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", 
"María" o "Pedro", o "Hola desconocido" si el nombre ingresado no 
es uno de esos tres.'''
nombre_ingresado = input("Ingrese nombre: ")
if nombre_ingresado == "Juan" or nombre_ingresado == "Maria" or nombre_ingresado == "Pedro":
    print(f"Hola {nombre_ingresado}")
else:
    print("Hola desconocido")