''' Cubilla Damian - 1H
11. Dado un número entero n, imprimir la secuencia de números 
primos menores o iguales a n.
'''
def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def imprimir_primos_hasta_n(n):
    for i in range(2, n + 1):
        if es_primo(i):
            print(i)

numero_ingresado = int(input("Ingrese un número: "))
print("Secuencia de números primos menores o iguales a", numero_ingresado)
imprimir_primos_hasta_n(numero_ingresado)