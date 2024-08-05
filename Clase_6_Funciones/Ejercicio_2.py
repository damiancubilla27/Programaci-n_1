''' Cubilla Damian - 1H
Crear una función que calcule el área de un círculo. 
Recibe un parámetro (radio) y devuelve el área del círculo.
'''
def calcular_area_circulo(radio:int)->float:
    retorno = 3.14 * (radio**2)
    return retorno

radio_ingresado = int(input("Ingrese radio del circulo: "))
print(f"El area del circulo es: {calcular_area_circulo(radio_ingresado)}")