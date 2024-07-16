''' Cubilla Damian - 1H
20. Dado un número entero n, imprimir todos los números 
perfectos menores o iguales a n.
'''
def es_perfecto(numero):
    suma_divisores = 1
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            suma_divisores += i
            if i != numero // i:
                suma_divisores += numero // i
    return suma_divisores == numero

def numeros_perfectos_hasta_n(n):
    perfectos = []
    for i in range(2, n + 1):
        if es_perfecto(i):
            perfectos.append(i)
    return perfectos

numero_ingresado = int(input("Ingrese número: "))
perfectos_hasta_n = numeros_perfectos_hasta_n(numero_ingresado)
print("Números perfectos menores o iguales a", numero_ingresado, ":", perfectos_hasta_n)