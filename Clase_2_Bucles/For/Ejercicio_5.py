''' Cubilla Damian - 1H
5. Dada una lista de números, imprimir el número más pequeño de la lista.
'''
lista_numeros = [2,6,5,1,4]
menor = lista_numeros[0]
for elemento in lista_numeros:
    if(elemento <= menor):
        menor = elemento
print(f"El numero menor es {menor}")