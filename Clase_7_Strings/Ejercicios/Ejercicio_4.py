''' Cubilla Damian - 1H
Escribir una función que tome un string y devuelva el número de caracteres
que tiene el string.
'''
def contar_letras(texto:str)->int:
    contador = len(texto)
    return contador

texto_ingresado = input("Ingrese texto: ")
print(f"Numero de letras: {contar_letras(texto_ingresado)}")