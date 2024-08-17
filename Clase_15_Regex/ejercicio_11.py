'''Cubilla Damian
11. Crear una función que reciba un texto y devuelva una la lista de palabras
encuentra que comienzan con una voca
'''
import re
def buscar_vocal(texto:str)->list:
    palabras = re.split(r'\s+|[,.;!?]', texto)
    lista = []
    for palabra in palabras:
        if(re.match("^[aeiouAEIOU]", palabra)):
            lista.append(palabra)
    return lista

texto_ingresado = input("Ingrese un texto: ")
lista_devuelta = buscar_vocal(texto_ingresado)
if(len(lista_devuelta) != 0):
    print(lista_devuelta)
else:
    print("No se encontro ninguna palabra con el comienzo de una vocal!")