''' Cubilla Damian - 1H
Escribir una función que tome una cadena de texto y la convierta en un
acrónimo,tomando la primera letra de cada palabra, por ejemplo:
"Universidad Tecnológica Nacional Facultad 
Regional Avellaneda" -> "UTNFRA”.
'''
def convertir_a_acronimo(texto: str) -> str:
    palabras = texto.split()
    letras = [palabra[0].upper() for palabra in palabras]
    acronimo = ''.join(letras)
    return acronimo

texto_ingresado = "Universidad Tecnológica Nacional Facultad Regional Avellaneda"
print(convertir_a_acronimo(texto_ingresado))  # Salida: "UTNFRA"