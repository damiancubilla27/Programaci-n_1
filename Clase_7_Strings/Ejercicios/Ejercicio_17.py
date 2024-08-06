''' Cubilla Damian - 1H
Escribir una función que tome un número binario y lo convierta en una cadena
de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo:
"101" -> "00000101".
'''
def convertir_a_8bits(binario: str) -> str:
    binario_8bits = binario.zfill(8)
    return binario_8bits

binario = "101"
print(convertir_a_8bits(binario))