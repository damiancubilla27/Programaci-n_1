''' Cubilla Damian - 1H
Escribir una función que reciba un string y devuelva el mismo string todo en
mayúsculas.
'''
def devolver_en_mayuscula(texto:str)->str:
    mayuscula = texto.upper()
    return mayuscula

texto_ingresado = input("Ingrese texto: ")
print(devolver_en_mayuscula(texto_ingresado))