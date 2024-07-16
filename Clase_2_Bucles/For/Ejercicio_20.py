''' Cubilla Damian - 1H
20. Dado un número entero n, 
imprimir la secuencia de números triangulares menores o iguales a n.
'''
def es_triangular(numero):
    n = 1
    suma = 0
    while suma < numero:
        suma += n
        if suma == numero:
            return True
        n += 1
    return False
def imprimir_triangular_hasta_n(n):
    for i in range(1, n + 1):
        if es_triangular(i):
            print(i)
numero_ingresado = int(input("Ingrese un número: "))
print("Secuencia de números triangulares menores o iguales a", numero_ingresado)
imprimir_triangular_hasta_n(numero_ingresado)
