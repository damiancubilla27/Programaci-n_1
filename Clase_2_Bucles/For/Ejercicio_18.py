''' Cubilla Damian
18. Dada una lista de números, imprimir la suma de los números en la 
lista que son mayores que el promedio de la lista.
'''
def suma_mayores_que_promedio(lista):
    if not lista:
        return 0
    
    promedio = sum(lista) / len(lista)
    suma = 0
    for num in lista:
        if num > promedio:
            suma += num
    return suma
lista_numeros = [10, 20, 30, 40, 50]
resultado = suma_mayores_que_promedio(lista_numeros)
print("La suma de los números mayores que el promedio en la lista es:", resultado)