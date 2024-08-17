'''Cubilla Damian
5. Crear una función llamada es_decimal que reciba dos strings: el primero
representa la expresión a evaluar y el segundo el separador decimal (puede
ser punto . o coma ,). Debe devolver True en caso que se trate de un número
decimal y False en el caso contrario
'''
import re
def es_decimal(texto:str, separador:str)->bool:
    regex = "^[0-9]+{0}[0-9]+$".format(separador)
    resultado = re.match(regex, texto)
    return resultado

texto_ingresado = input("Ingrese numeros: ")
separador_ingresado = input("Ingrese separador: ")
if es_decimal(texto_ingresado, separador_ingresado):
    print("El texto contiene numeros decimales!")
else:
    print("El texto no es un numero decimal.")