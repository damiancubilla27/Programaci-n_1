''' Cubilla Damian - 1H
2. Crea una lista con 5 numeros enteros. Luego solicita 
un nuevo numero y reemplaza el tercer elemento de la
lista por el numero ingresado. Finalmente imprime
todos los numeros.
'''
lista_numeros = [33, 5, 2, 45, 9]
numero_ingresado = int(input("Ingrese numero: "))
lista_numeros[2] = numero_ingresado
for elemento in lista_numeros:
    print(f"{elemento}", end = " ")