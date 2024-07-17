''' Cubilla Damian - 1H
10. Crea una lista de palabras y muestra las palabras
que tienen mas de 5 letras.
'''
lista_libros = ["Prin", "Malvinas", "Martin Fierro", "Bocha", "Platon"]
for elemento in lista_libros:
    if(len(elemento) > 5):
        print(f"{elemento}")
