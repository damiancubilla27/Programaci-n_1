''' Cubilla Damian - 1H
Escribir una función que tome una cadena de caracteres y reemplace todas
las letras mayúsculas por letras minúsculas y todas las letras minúsculas por
letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
'''
def intercambiar_mayusculas_minusculas(cadena: str) -> str:
    cadena_intercambiada = cadena.swapcase()
    return cadena_intercambiada

cadena = "HoLa"
print(intercambiar_mayusculas_minusculas(cadena)) 