''' Cubilla Damian - 1H
17. Crea un diccionario que represente las películas de un cine, 
donde las claves son los nombres de las películas y los valores 
son los horarios correspondientes. Modifica el horario de la 
película "Avengers: Endgame" a las 19:30.
'''
dict_peliculas = {"Batman":"18:30", "Guason":"22:30", "Avengers: Endgame":"23:00"}
dict_peliculas["Avengers: Endgame"] = "19:30"
print(f"El nuevo horario de 'Avengers: Endgame' es {dict_peliculas['Avengers: Endgame']}")
