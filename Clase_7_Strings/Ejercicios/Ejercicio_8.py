''' Cubilla Damian - 1H
Escribir una función que reciba dos string (nombre y apellido) y devuelva un
diccionario con el nombre y apellido, eliminando los espacios del comienzo y
el final y colocando la primer letra en mayúscula
'''
def crear_diccionario_nombres(texto:str)->dict:
    lista = texto.split(" ")
    dict_nombre = {}
    dict_nombre["nombre"] = lista[0].capitalize()
    dict_nombre["apellido"] = lista[1].capitalize()
    return dict_nombre

texto_ingresado = input("Ingrese nombre y apellido: ")
print(crear_diccionario_nombres(texto_ingresado))