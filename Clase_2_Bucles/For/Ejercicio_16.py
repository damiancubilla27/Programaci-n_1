''' Cubilla Damian - 1H
16. Dada una lista de palabras, imprimir las palabras 
que tienen una letra específica.
'''
def palabras_con_letra_especifica(lista_palabras, letra):
    palabras_con_letra = []
    for palabra in lista_palabras:
        if letra in palabra:
            palabras_con_letra.append(palabra)
    return palabras_con_letra
lista_palabras = ["gato", "perro", "loro", "elefante", "tigre"]
letra_especifica = input("Ingrese una letra: ")
print("Palabras que contienen la letra", letra_especifica + ":")
resultado = palabras_con_letra_especifica(lista_palabras, letra_especifica)
print(resultado)