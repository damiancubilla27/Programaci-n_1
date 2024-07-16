''' Cubilla Damian - 1H
3. Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.
'''
texto_ingresado = input("Ingres texto: ")
elemento = 0
while(elemento <= int(len(texto_ingresado) - 1)):
    print(texto_ingresado[elemento])
    elemento += 1