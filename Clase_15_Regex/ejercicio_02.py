'''Cubilla Damian
2. Crear una función llamada es_minuscula que reciba un string y devuelva True
en caso de que todas las letras sean mayúsculas o False en el caso contrario
'''
import re

def es_minuscula(texto:str)->bool:
    resultado = re.match("^[a-z ]+$", texto)
    return resultado

texto_ingresado = input("Ingrese un texto: ")
if es_minuscula(texto_ingresado):
    print("El texto contiene todas letras minusculas!")
else:
    print("El texto tiene mayusculas y minusculas.")