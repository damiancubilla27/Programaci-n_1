''' Cubilla Damian - 1H
Crear una función que calcule el área de un triángulo. 
Recibe dos parámetros (base y altura) y devuelve el área.
'''
def calcular_area_triangulo(base:int, altura:int)->float:
    retorno = (base * altura) / 2
    return retorno

base_ingresada = int(input("Ingrese base: "))
altura_ingresada = int(input("Ingrese altura: "))
print(f"El area del triangulo es {calcular_area_triangulo(base_ingresada, altura_ingresada)}")