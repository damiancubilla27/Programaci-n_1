''' Cubilla Damian - 1H
Escribir una función que tome una lista de palabras y devuelva un string que
contenga todas las palabras concatenadas con comas y "y" antes de la última
palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el
string resultante debería ser "manzanas, naranjas y bananas"..
'''
def concatenar_palabras(lista_palabras:list)->str:
    lista_con_comas = lista_palabras[:-1]
    cadena_comas = ",".join(lista_con_comas)
    retorno = f"{cadena_comas} y {lista_palabras[-1]}"
    return retorno

lista = ["manzanas", "naranjas", "bananas"]
print(concatenar_palabras(lista))