''' Cubilla Damian - 1H
9. Crea una lista de numeros enteros y pide al usuario que
ingrese otro numero entero. Luego, buscar el numero ingresado
en la lista y muestra la posicion en la que se encuentra.
'''
lista_numeros = [1,2,3]
numero_ingresado = int(input("Ingrese numero: "))
lista_numeros.append(numero_ingresado)
for elemento in range(len(lista_numeros)):
    if(lista_numeros[elemento] == numero_ingresado):
        print(f"EL elemento se encuentra en la posicion {elemento}")