''' Cubilla Damian - 1H
17. Dado un número entero n, imprimir la secuencia de números 
de Harshad menores o iguales a n.
'''
def suma_digitos(numero):
    suma = 0
    numero_str = str(numero)
    for digito in numero_str:
        suma += int(digito)
    return suma

def es_harshad(numero):
    return numero % suma_digitos(numero) == 0

def imprimir_harshad_hasta_n(n):
    for i in range(1, n + 1):
        if es_harshad(i):
            print(i)

numero_ingresado = int(input("Ingrese un número: "))
print("Secuencia de números de Harshad menores o iguales a", numero_ingresado)
imprimir_harshad_hasta_n(numero_ingresado)