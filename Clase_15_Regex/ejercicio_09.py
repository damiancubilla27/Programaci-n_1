'''Cubilla Damian
9. Crear una función que reciba un texto y devuelva una lista con las palabras
que contienen entre 3 y 6 caracteres de largo
'''
import re
def palabras_entre_3_y_6_caracteres(texto: str)->list:
    resultado = re.findall(r'[a-zA-Z]{3,6}', texto)
    return resultado

texto_ingresado = input("Ingrese texto: ")
palabras = palabras_entre_3_y_6_caracteres(texto_ingresado)
print(palabras)