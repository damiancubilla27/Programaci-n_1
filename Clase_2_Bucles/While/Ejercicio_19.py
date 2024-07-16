''' Cubilla Damian - 1H
19. Dada una lista de números, 
imprimir todos los números que son mayores que el 
número anterior en la lista.
'''
def imprimir_mayores_que_anterior(lista):
    if len(lista) < 2:
        return
    
    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1]:
            print(lista[i])
numeros = [5, 3, 7, 2, 8, 4, 6]
print("Números mayores que el anterior en la lista:")
imprimir_mayores_que_anterior(numeros)