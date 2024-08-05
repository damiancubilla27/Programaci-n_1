''' Cubilla Damian - 1H
Crea una función que reciba dos listas de nombres, y devuelva una 
lista con los nombres que aparecen en ambas listas.
'''
def comparar_listas(primera_lista:list, segunda_lista:list)->list:
    lista_retorno = []
    for elemento in primera_lista:
        if(elemento in segunda_lista):
            lista_retorno.append(elemento)
    return lista_retorno
lista_uno = ["Damian", "Lucia", "Gerardo"]
lista_dos = ["Camila", "Aldana", "Damian"]
print(comparar_listas(lista_uno, lista_dos))