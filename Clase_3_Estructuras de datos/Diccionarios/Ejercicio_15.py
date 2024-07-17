''' Cubilla Damian - 1H
15. Crea un diccionario que contenga el nombre y el 
sueldo de varios empleados. Luego, permite al usuario 
aumentar el sueldo de un empleado y actualizar el 
valor correspondiente en el diccionario.
'''
dict_empleado = {"sanchez":800, "cordoba":600, "cubilla":700}
nombre_ingresado = input("Ingrese nombre del enpleado a buscar: ")
numero_ingresado = int(input("Ingrese nuevo salario del empleado: "))
for elemento in dict_empleado.keys():
    if(elemento == nombre_ingresado):
        dict_empleado[elemento] = numero_ingresado
        print(f"El empleado {nombre_ingresado} tiene como salario nuevo {dict_empleado[elemento]}")