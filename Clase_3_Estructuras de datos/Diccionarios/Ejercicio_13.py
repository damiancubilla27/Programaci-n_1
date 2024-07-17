''' Cubilla Damian - 1H
13. Crea un diccionario que contenga el nombre y el nivel 
de dificultad de varios juegos de mesa. Luego, pedirle al 
usuario un nivel de dificultad, buscar los que coinciden 
e imprimir sus nombres
'''
dict_juegos = {"ludo": 3, "truco":6, "ruleta":8}
juego_ingresado = input("Ingrese nombre de juego: ")
for elemento in dict_juegos.keys():
    if(elemento == juego_ingresado):
        print(f"El juego {juego_ingresado} tiene la dificultad de: {dict_juegos[elemento]} puntos")