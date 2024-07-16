''' Cubilla Damian - 1H
14. Dada una cadena de texto, imprimir la cantidad de veces 
que aparece una letra específica en la cadena.
'''
texto_ingresado = input("Ingrese texto: ")
letra_ingresada = input("Ingrese letra a buscar: ")
elemento = 0
suma = 0
while(elemento < len(texto_ingresado) - 1):
    if(texto_ingresado[elemento] == letra_ingresada):
        suma += 1
    elemento += 1
print(f"La cantidad de letras {letra_ingresada} son: {suma}")