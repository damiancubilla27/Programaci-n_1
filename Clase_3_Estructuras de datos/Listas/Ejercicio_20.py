''' Cubilla Damian - 1H
20. A partir de la lista: [1,80,5,0,15,-5,1,79] determinar, 
el mayor, el menor, el promedio y la suma total de todos los elementos
'''
lista_numeros = [1,80,5,0,15,-5,1,79]
mayor = lista_numeros[0]
menor = lista_numeros[0]
suma = 0

for numero in lista_numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    suma += numero

promedio = suma / len(lista_numeros)

print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Promedio: {promedio}")
print(f"Suma: {suma}")