'''Cubilla Damian
4. Crear una función llamada es_solo_texto que reciba un string y devuelva True
en caso de que trate solo de caracteres alfabéticos y el espacio y False en el
caso contrario
'''
import re

def es_solo_texto(texto:str)->bool:
    resultado = re.match("^[a-zA-Z ]+$", texto)
    return resultado

texto_ingresado = input("Ingrese texto: ")
if es_solo_texto(texto_ingresado):
    print("El texto contiene solamente caracteres alfabeticos!")
else:
    print("El texto tiene otras cosas.")