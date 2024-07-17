''' Cubilla Damian - 1H
19. Crea una lista vacía y pide al usuario que ingrese una palabra. 
Luego, agrega la palabra a la lista si no se encuentra ya en la lista. 
Repite este proceso hasta que la lista tenga al menos 5 palabras.
'''
lista_palabras = []
while len(lista_palabras) < 5:
    palabra = input("Ingrese una palabra: ")
    if palabra not in lista_palabras:
        lista_palabras.append(palabra)
    else:
        print("La palabra ya está en la lista. Intente con otra.")
print("La lista final de palabras es:", lista_palabras)