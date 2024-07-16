''' Cubilla Damian - 1H
2. Dada una lista de palabras, imprimir la palabra más larga de la lista.
'''
lista_palabras = ["River", "Hola", "Damian", "Chau"]
palabra_mas_larga = " "
for elemento in lista_palabras:
    if(len(palabra_mas_larga) < len(elemento)):
        palabra_mas_larga = elemento
print(f"La palabra mas larga es {palabra_mas_larga}")