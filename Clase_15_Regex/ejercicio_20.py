'''Cubilla Damian
20. Crear una función llamada validar_ip que reciba un string como parámetro y
verifique si se trata de una dirección IP v4 válida, en caso de serlo retornar
True de lo contrario retornar False.
Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde
xxx es un número entero entre 0 y 255.
'''
import re
def validar_ip(texto:str)->bool:
    resultado = re.match("[0-9]{3} [0-9]{3} [0-9]{3} [0-9]{3}", texto)
    return resultado

texto_ingresado = input("Ingrese direccion IP: ")
if validar_ip(texto_ingresado):
    print("Direccion IP correcta!")
else:
    print("Direccion IP incorrecta.")