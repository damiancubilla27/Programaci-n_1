''' Cubilla Damian - 1H
18. Dado un número entero n, imprimir la suma de todos los 
números que son múltiplos de 5 menores o iguales a n.
'''
numero_ingresado = int(input("Ingrese numero: "))
elemento = 0
while(elemento <= numero_ingresado):
    if(elemento % 5 == 0):
        print(f"{elemento}")
    elemento += 1