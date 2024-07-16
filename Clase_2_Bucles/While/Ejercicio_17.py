''' Cubilla Damian - 1H
17. Dada una cadena de texto, imprimir la cadena al revés.
'''
texto_ingresado = input("Ingrese texto: ")
elemento = len(texto_ingresado) - 1 
while(0 <= elemento):
    print(f"{texto_ingresado[elemento]}", end=" ")
    elemento -= 1