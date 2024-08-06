''' Cubilla Damian - 1H
20.Escribir una función que tome una lista de direcciones de correo electrónico y
las una en una sola cadena separada por punto y coma, por ejemplo:
["juan@gmail.com",
"maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".
'''
def unir_correos(correos: list) -> str:
    cadena_unida = ";".join(correos)
    return cadena_unida

correos = ["juan@gmail.com", "maria@hotmail.com"]
print(unir_correos(correos))