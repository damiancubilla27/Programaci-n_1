''' Cubilla Damian - 1H
14. Crea dos listas de 10 números enteros cada una y realiza una 
multiplicación de los elementos con el mismo índice en ambas listas.
'''
lista_numero_uno = [1,2,3,4,5,6,7,8,9,10]
lista_numero_dos = [10,9,8,7,6,5,4,3,2,1]
lista_numeros_multiplicados = []
for elemento in range(10):
    lista_numeros_multiplicados.append(lista_numero_uno[elemento] * lista_numero_dos[elemento])
print(lista_numeros_multiplicados)