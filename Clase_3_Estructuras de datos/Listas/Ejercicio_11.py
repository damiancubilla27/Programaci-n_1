''' Cubilla Damian - 1H
11. Crea una lista de palabras y pide al usuario que ingrese una palabra. 
Luego, muestra todas las palabras de la lista que tienen la misma longitud 
que la palabra ingresada.
'''
lista_deportes = ["Futbol", "Natacion", "Tenis"]
deporte_ingresado = input("Ingrese deporte: ")
for elemento in lista_deportes:
    if(len(elemento) == len(deporte_ingresado)):
        print(elemento)