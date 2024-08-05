''' Cubilla Damian - 1H
Crear una función que convierta grados Celsius a grados Fahrenheit. 
Recibe un parámetro (grados Celsius) y devuelve el resultado 
en grados Fahrenheit.
'''
def convertir_grados(celsius:int)->float:
    retorno = (1.8 * celsius) + 32
    return retorno

grado_ingresado = int(input("Ingrese grados celsius: "))
print(f"{grado_ingresado} grados celsius son {convertir_grados(grado_ingresado)} grados fahrenheit")