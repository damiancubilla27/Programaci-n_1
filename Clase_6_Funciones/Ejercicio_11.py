''' Cubilla Damian - 1H
Crea una función que reciba como parámetros una lista de palabras 
y devuelva la palabra más larga.
'''
def devolver_palabra_mas_larga(lista_palabras:list)->str:
    palabra = lista_palabras[0]
    for elemento in lista_palabras:
        if(len(elemento) > len(palabra)):
            palabra = elemento
    return palabra
lista_palabras = ["damian", "river", "elefante", "flecha"]
print(f"La palabra mas larga es: {devolver_palabra_mas_larga(lista_palabras)}")