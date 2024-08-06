''' Cubilla Damian - 1H
Escribir una función que tome una cadena de caracteres y cuente la cantidad
de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
'''
def contar_digitos(cadena: str) -> int:
    contador = 0
    for caracter in cadena:
        if caracter.isdigit():
            contador += 1
    return contador

cadena = "1234 Hola Mundo"
print(f'La cadena "{cadena}" contiene {contar_digitos(cadena)} dígitos.')