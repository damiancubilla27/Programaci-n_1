''' Cubilla Damian - 1H
Crear una función que calcule el descuento aplicado a un producto. 
Recibe dos parámetros (precio original y precio con descuento) y 
devuelve el porcentaje de descuento aplicado.
'''
def calcular_descuento(precio_original:int, descuento:int)->float:
    descuento_aplicar = (precio_original * descuento) / 100
    retorno = precio_original - descuento_aplicar
    return retorno

precio_ingresado = int(input("Ingrese precio: "))
descuento_ingresado = int(input("Ingrese descuento: "))
print(f"Precio original: {precio_ingresado} - {descuento_ingresado} % = {calcular_descuento(precio_ingresado, descuento_ingresado)}$ Precio final")