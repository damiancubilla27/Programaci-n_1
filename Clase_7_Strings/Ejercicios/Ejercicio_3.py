''' Cubilla Damian - 1H
Escribir una función que tome dos strings y devuelva un nuevo string que
contenga ambos strings concatenados, separados por un espacio.
'''
def concatenar_texto(texto_uno:str, texto_dos:str)->str:
    texto_concatenado = f"{texto_uno} {texto_dos}"
    return texto_concatenado

texto_ingresado_uno = input("Ingrese texto: ")
texto_ingresado_dos = input("Ingrese otro texto: ")
print(concatenar_texto(texto_ingresado_uno, texto_ingresado_dos))