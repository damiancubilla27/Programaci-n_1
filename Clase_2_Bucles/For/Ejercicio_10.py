''' Cubilla Damian - 1H
10. Dada una lista de palabras, imprimir las palabras que comienzan 
y terminan con la misma letra.'''
lista_palabras = ["hola", "chau", "river", "damian", "alemania"]
for elemento in lista_palabras:
    if(elemento[0] == elemento[len(elemento) - 1]):
        print(f"{elemento}")