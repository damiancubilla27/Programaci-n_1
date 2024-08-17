'''Cubilla Damian
1. Crear una función llamada es_mayuscula que reciba un string y devuelva True
en caso de que todas las letras sean mayúsculas o False en el caso contrario
'''
import re

def es_mayuscula(texto:str)->bool:
    resultado = re.match("^[A-Z ]+$", texto)
    return resultado

texto_ingresado = input("Ingrese un texto: ")
if es_mayuscula(texto_ingresado):
    print("El texto contiene todas letras mayusculas!")
else:
    print("El texto tiene mayusculas y minusculas.")