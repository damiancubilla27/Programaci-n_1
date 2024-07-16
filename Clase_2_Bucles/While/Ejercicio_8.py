''' Cubilla Damian - 1H
8. Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.
'''
texto_ingresado = input("Ingresar texto: ")
elemento = 0
contador = 0
while(elemento <= len(texto_ingresado) - 1):
    if(texto_ingresado[elemento] == 'a' or texto_ingresado[elemento] == 'e' or 
        texto_ingresado[elemento] == 'i' or texto_ingresado[elemento] == 'o' or 
        texto_ingresado[elemento] == 'u'):
        contador += 1
    elemento += 1
print(f"La cantidad de vovales es: {contador}")