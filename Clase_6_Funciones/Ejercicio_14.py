''' Cubilla Damian - 1H
Crear una función que recibe una lista de números y devuelve un diccionario 
con el valor mínimo, el valor máximo y el promedio de los números en la lista.
'''
def crear_diccionario_numeros(lista):
    dic = {}
    num_minimo = 0
    num_maximo = 0
    suma = 0
    for i in range(len(lista)):
        if(num_minimo == 0 or num_minimo > lista[i]):
            num_minimo = lista[i]
        if(num_maximo == 0 or num_maximo < lista[i]):
            num_maximo = lista[i]
        suma += lista[i]
    dic["valor minimo"] = num_minimo
    dic["valor maximo"] = num_maximo
    dic["promedio"] = suma / len(lista)
    return dic
lista_numeros = [3,5,1,9,8,7,6,2]
diccionario = crear_diccionario_numeros(lista_numeros)
print(diccionario)