'''Cubilla Damian
3. Crear una función llamada es_entero que reciba un string y devuelva True en
caso de que se trate de un número entero y False en caso contrario.
'''
import re

def es_entero(texto:str)->bool:
    resultado = re.match("^[0-9]+$", texto)
    return resultado

texto_ingresado = input("Ingrese un numero: ")
if es_entero(texto_ingresado):
    print("El texto contiene numeros!")
else:
    print("El texto tiene otras cosas.")
