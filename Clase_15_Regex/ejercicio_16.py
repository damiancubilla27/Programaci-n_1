'''Cubiilla Damian
16. Crear la función validar_codigo_postal que reciba un string como parámetro y
devuelva True en caso de tratarse de código postal válido o False en caso
contrario
'''
import re
def validar_codigo_postal(texto:str)->bool:
    resultado = re.match("^([A-Z]{1} [0-9]{4} [A-Z]{3})$", texto)
    return resultado

texto_ingresado = input("Ingrese codigo postal: ")
if validar_codigo_postal(texto_ingresado):
    print("El codigo postal es correcta!")
else:
    print("El codigo postal es INCORRECTO.")