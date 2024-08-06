''' Cubilla Damian - 1H
Escribir una función que tome un string y un carácter y devuelva una lista con
todas las palabras en el string que contienen ese carácter.
'''
def devolver_lista_de_palabras(texto:str)->list:
    lista = texto.split(" ")
    return lista

texto_ingresado = input("Ingrese texto: ")
print(devolver_lista_de_palabras(texto_ingresado))