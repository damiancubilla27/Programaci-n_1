''' Cubilla Damian - 1H
Escribir una función que reciba un string y devuelva el mismo string todo en
minúsculas.
'''
def devolver_en_minuscula(texto:str)->str:
    minuscula = texto.lower()
    return minuscula

texto_ingresado = input("Ingrese texto: ")
print(devolver_en_minuscula(texto_ingresado))