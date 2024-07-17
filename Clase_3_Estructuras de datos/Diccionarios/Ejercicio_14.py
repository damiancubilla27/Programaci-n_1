''' Cubilla Damian - 1H
14. Crea un diccionario que contenga el nombre como clave 
y el puntaje como valor de varios jugadores en un juego. 
Luego, pedirle al usuario el nombre del jugador y nuevo 
puntaje y actualizar el valor correspondiente en el 
diccionario.
'''
dict_equipo = {"sanchez":8, "cordoba":6, "cubilla":7}
nombre_ingresado = input("Ingrese nombre de jugador a buscar: ")
numero_ingresado = int(input("Ingrese nuevo puntaje de jugador: "))
for elemento in dict_equipo.keys():
    if(elemento == nombre_ingresado):
        dict_equipo[elemento] = numero_ingresado
        print(f"El jugador {nombre_ingresado} tiene como puntaje nuevo {dict_equipo[elemento]}")