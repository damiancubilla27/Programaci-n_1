''' Cubilla Damian - 1H
Crear una función que recibe una lista de diccionarios con 
información de películas (título, género, director) y devuelve 
un diccionario con la cantidad de películas por género.
'''
def contar_peliculas_por_genero(lista):
    dic_generos = {}
    for pelicula in lista:
        genero = pelicula["genero"]
        if genero in dic_generos:
            dic_generos[genero] += 1
        else:
            dic_generos[genero] = 1
    return dic_generos

lista_peliculas = [{"titulo": "El Padrino", "genero": "Drama", 
                    "director": "Coppola"},
                  {"titulo": "Regreso al futuro", "genero": "Ciencia Ficción", 
                    "director": "Zemeckis"},
                  {"titulo": "Los anillos", "genero": "Fantasía", 
                    "director": "Jackson"},
                  {"titulo": "Alien", "genero": "Ciencia Ficción",
                    "director": "Scott"},
                  {"titulo": "La lista ", "genero": "Drama",
                    "director": "Spielberg"}]

diccionario = contar_peliculas_por_genero(lista_peliculas)
print(diccionario)