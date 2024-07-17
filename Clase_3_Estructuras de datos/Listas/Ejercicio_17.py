''' Cubilla Damian - 1H
17. Crea dos listas de números y encuentra los elementos 
que se encuentran en ambas listas.
'''
lista_numero_uno = [1, 2, 3, 4, 5]
lista_numero_dos = [7, 6, 5, 4, 1]
elementos_comunes = []
for elemento in lista_numero_uno:
    if elemento in lista_numero_dos:
        elementos_comunes.append(elemento)
print(f"Elementos comunes en ambas listas: {elementos_comunes}")