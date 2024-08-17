'''Cubilla Damian
7. Crear una función llamada es_binario que devuelva True en caso de un
número binario válido (solo ceros y unos) o False en el caso contrario
'''
import re
def es_binario(texto:str)->bool:
    resultado = re.match("^[0-1]+$", texto)
    return resultado

texto_ingresado = input("Ingrese numeros binarios: ")
if es_binario(texto_ingresado):
    print("El texto contiene solo numeros binarios!")
else:
    print("El texto contiene mas cosas.")