''' Cubilla Damian - 1H
Crear una función que cuente la cantidad de veces que aparece 
un elemento en una lista. Recibe una lista y un elemento 
como parámetros y devuelve la cantidad de veces que 
aparece en la lista.
'''
def contador_numeros_repetidos(lista_numeros:list, numero:int)->int:
    contador = 0
    for elemento in lista_numeros:
        if(elemento == numero):
            contador += 1
    return contador
lista_numeros = [3,5,6,8,4,3,1,4]
numero = 5
print(f"La cantidad de veces que aparece el numero {numero} en la lista es: {contador_numeros_repetidos(lista_numeros, numero)}")
