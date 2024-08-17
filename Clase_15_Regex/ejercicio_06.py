'''Cubilla Damian
6. Crear una función llamada es_alfanumerico que devuelva True en caso de
tratarse de solo letras y números y False en el caso contrario (es decir que
contenga caracteres especiales)
'''
import re

def es_alfanumerico(texto:str)->bool:
    resultado = re.match("^[a-zA-Z0-9 ]+$", texto)
    return resultado

texto_ingresado = input("Ingrese texto: ")
if es_alfanumerico(texto_ingresado):
    print("El texto contiene solo letras y números!")
else:
    print("El texto tiene otras cosas.")