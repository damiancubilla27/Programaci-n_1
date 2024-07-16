''' Cubilla Damian - 1H
11. Dada una lista de palabras, imprimir todas las palabras 
que tengan una longitud mayor a 5 caracteres.
'''
lista_palabras = ["Damian", "hoja", "hola", "Cubilla", "chau"]
elemento = 0
while(elemento < len(lista_palabras) - 1):
    if(len(lista_palabras[elemento]) > 5):
        print(f"{lista_palabras[elemento]}")
    elemento += 1    