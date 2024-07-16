''' Cubilla Damian - 1H
19. Dada una lista de palabras, imprimir las 
palabras que tienen una letra mayúscula.
'''
def palabras_con_mayuscula(lista_palabras):
    palabras_con_mayuscula = []
    for palabra in lista_palabras:
        for letra in palabra:
            if letra.isupper():
                palabras_con_mayuscula.append(palabra)
                break  
    return palabras_con_mayuscula
lista_palabras = ["hola", "Mundo", "python", "PROGRAMACIÓN", "OpenAI"]
palabras_con_mayuscula = palabras_con_mayuscula(lista_palabras)
print("Palabras con al menos una letra mayúscula:")
print(palabras_con_mayuscula)