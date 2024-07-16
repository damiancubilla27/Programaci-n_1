''' Cubilla Damian - 1H
15. Dado un número entero n, imprimir todos los números primos menores o iguales a n.
'''
def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos_hasta_n(n):
    if n < 2:
        return []
    
    primos = [2]
    if n == 2:
        return primos

    primo_candidato = 3
    while primo_candidato <= n:
        if es_primo(primo_candidato):
            primos.append(primo_candidato)
        primo_candidato += 2
    return primos

numero_ingresado = int(input("Ingrese número: "))
primos_hasta_n = numeros_primos_hasta_n(numero_ingresado)
print("Números primos menores o iguales a", numero_ingresado, ":", primos_hasta_n)