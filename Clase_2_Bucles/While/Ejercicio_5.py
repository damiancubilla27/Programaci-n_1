''' Cubilla Damian - 1H
5. Dado un número entero n, imprimir si el número es primo o no.
'''
numero_ingresado = int(input("Ingrese numero: "))
if numero_ingresado > 1:
    es_primo = True
    elemento = 2
    while elemento < numero_ingresado:
        if numero_ingresado % elemento == 0:
            es_primo = False
            break
        elemento += 1
    if es_primo:
        print(numero_ingresado, "es un número primo")
    else:
        print(numero_ingresado, "no es un número primo")
else:
    print(f"{numero_ingresado} no es un número primo")