''' Cubilla Damian - 1H
Escribir una función que tome una lista de nombres y los una en una sola
cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"]
-> "Juan\nMaría\nPedro".
'''
def separar_lista(lista_palabras:list)->str:
    texto = " ".join(lista_palabras)
    retorno = texto.replace(" ", "\n")
    return retorno

lista = ["Juan", "María", "Pedro"]
print(separar_lista(lista))
