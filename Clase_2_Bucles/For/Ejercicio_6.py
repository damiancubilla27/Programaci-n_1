''' Cubilla Damian - 1H
6. Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.
'''
lista_texto = ['w', 'e', 't','t','u','p']
cantidad = 0
for elemento in lista_texto:
    if(elemento == 'a' or elemento == 'e' or elemento == 'i' or 
        elemento == 'o' or elemento == 'u'):
        cantidad += 1
print(f"La cantidad de vocales en la lista es: {cantidad}")