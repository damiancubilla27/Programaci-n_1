''' Cubilla Damian - 1H
18. Crea un diccionario que represente los juegos de una consola, 
donde las claves son los nombres de los juegos y los valores 
son las puntuaciones correspondientes. Solicita al usuario el 
nombre de un juego y luego su puntuación, si el juego no 
existe agregarlo y si existe actualizar su puntuación.
'''
dict_juegos = {"mario": 9, "pes": 8, "fifa": 7}
nombre_ingresado = input("Ingrese nombre del juego: ")
puntuacion_ingresada = int(input("Ingrese nueva puntuacion: "))
bandera_nombre = 0
for elemento in dict_juegos.keys():
    if(elemento == nombre_ingresado):
        dict_juegos[elemento] = puntuacion_ingresada
        print(f"El juego {elemento} pasa a tener una puntuacion de: {dict_juegos[elemento]}")
        bandera_nombre = 1
if(bandera_nombre != 1):
    dict_juegos[nombre_ingresado] = puntuacion_ingresada

print(dict_juegos)