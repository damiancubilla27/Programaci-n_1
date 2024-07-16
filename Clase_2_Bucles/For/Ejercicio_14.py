''' Cubilla Damian - 1H
14. Dado un número entero n, imprimir la secuencia 
de números perfectos menores o iguales a n.
'''
def es_perfecto(numero):
    suma_divisores = 1
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            suma_divisores += i
            if i != numero // i:
                suma_divisores += numero // i
    return suma_divisores == numero

def imprimir_perfectos_hasta_n(n):
    for i in range(2, n + 1):
        if es_perfecto(i):
            print(i)

numero_ingresado = int(input("Ingrese un número: "))
print("Secuencia de números perfectos menores o iguales a", numero_ingresado)
imprimir_perfectos_hasta_n(numero_ingresado)