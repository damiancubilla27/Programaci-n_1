''' Cubilla Damian - 1H
6. Filtra las palabras de una lista que tienen más de 5 letras.
'''
palabras = ['perro', 'gato', 'elefante', 'ratón', 'jirafa']
palabras_largas = list(filter(lambda x: len(x) > 5, palabras))
print(palabras_largas)  