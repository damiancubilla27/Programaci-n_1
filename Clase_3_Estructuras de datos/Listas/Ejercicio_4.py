''' Cubilla Damian - 1H
4. Crea una lista vacia y pide al usuario que ingrese 
una palabra. Luego, muestra la primera letra de la 
palabra. Repite este proceso hasta que el usuario 
ingrese una palabra que comience con la letra "z"
'''
lista_palabra = []
palabra = "a"
while(palabra[0] != 'z'):
    palabra = input("Ingrese palabra: ")
    if(palabra[0] != 'z'):
        print(f"{palabra[0]}")
        lista_palabra.append(palabra)
print(lista_palabra)