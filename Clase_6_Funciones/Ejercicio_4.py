''' Cubilla Damian - 1H
Crear una función que calcule el promedio de edad de un grupo de personas. 
Recibe una lista de edades y devuelve el promedio.
'''
def calcular_promedio_edades(lista_edades:list)->float:
    suma = 0
    promedio = 0
    for elemento in lista_edades:
        suma += elemento
    promedio = suma / len(lista_edades)
    return promedio
lista_edades = [2,33,54,10,63]
print(f"El promedio de edades es: {calcular_promedio_edades(lista_edades)}")
