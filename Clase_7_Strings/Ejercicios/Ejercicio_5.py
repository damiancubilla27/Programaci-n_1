''' Cubilla Damian - 1H
Escribir una función que tome un string y un carácter y devuelva el número de
veces que aparece ese carácter en el string.
'''
def devolver_en_minuscula(texto:str, letra:str)->int:
    numero_veces_caracter = texto.count(letra)
    return numero_veces_caracter

texto_ingresado = input("Ingrese texto: ")
letra_ingresada = input("Ingrese letra: ")
print(f"La cantidad de veces que aparece la letra {letra_ingresada} es: {devolver_en_minuscula(texto_ingresado, letra_ingresada)}")