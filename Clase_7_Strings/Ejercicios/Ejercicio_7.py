''' Cubilla Damian - 1H
Escribir una función que tome un string y devuelva el mismo string con los
espacios eliminados
'''
def devolver_sin_espacios(texto:str)->str:
    retorno = texto.replace(" ", "")
    return retorno

texto_ingresado = input("Ingrese texto: ")
print(devolver_sin_espacios(texto_ingresado))