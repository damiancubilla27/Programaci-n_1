'''Cubilla Damian - 1H
13. Dada una lista de palabras, imprimir las palabras 
que tienen una longitud impar.
'''
lista_palabras = ["hola", "chau", "river", "damian", "alemania"]
for elemento in lista_palabras:
    if(len(elemento) % 2 == 1):
        print(f"{elemento}")