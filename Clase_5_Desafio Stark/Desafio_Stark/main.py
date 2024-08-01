# Cubilla Damian - 1H
# Desafio Stark

from data_stark import lista_personajes

# 1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def imprimir_todos_los_nombres():
    for i in lista_personajes:
        print("{0}".format(i["nombre"]))


# 2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe 
# junto a la altura del mismo
def imprimir_nombre_y_altura():
    for i in lista_personajes:
        print("Nombre: {0} - Altura: {1}".format(i["nombre"], i["altura"]))


# 3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def mostrar_mas_alto():
    mas_alto = None
    for i in range(len(lista_personajes)):
        if(mas_alto is None or 
        lista_personajes[i]["altura"] > lista_personajes[mas_alto]["altura"]):
            mas_alto = i

    print("Personaje mas alto: {0} - {1}"
        .format(lista_personajes[mas_alto]["nombre"],
                lista_personajes[mas_alto]["altura"]))


# 4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def mostrar_mas_bajo():
    mas_bajo = None
    for i in range(len(lista_personajes)):
        if(mas_bajo is None or 
        lista_personajes[i]["altura"] < lista_personajes[mas_bajo]["altura"]):
            mas_bajo = i

    print("Personaje mas bajo: {0} - {1}"
        .format(lista_personajes[mas_bajo]["nombre"],
                lista_personajes[mas_bajo]["altura"]))


# 5. Recorrer la lista y determinar la altura promedio de los  superhéroes
def mostrar_promedio_alturas():
    suma = 0
    for i in lista_personajes:
        suma += float(i["altura"])
    print("La altura promedio es de: {0}".format(suma/len(lista_personajes)))


# 6. Informar cual es la identidad del superhéroe asociado a cada uno 
# de los indicadores anteriores (MÁXIMO, MÍNIMO)
def imprimir_identidad_alto():
    mas_alto = None
    for i in range(len(lista_personajes)):
        if(mas_alto is None or 
        lista_personajes[i]["altura"] > lista_personajes[mas_alto]["altura"]):
            mas_alto = i

    print("Superheroe mas alto: {0} - Indentidad: {1}"
        .format(lista_personajes[mas_alto]["nombre"],
                lista_personajes[mas_alto]["identidad"]))
def imprimir_identidad_bajo():
    mas_bajo = None
    for i in range(len(lista_personajes)):
        if(mas_bajo is None or 
        lista_personajes[i]["altura"] < lista_personajes[mas_bajo]["altura"]):
            mas_bajo = i

    print("Superheroe mas bajo: {0} - Indentidad: {1}"
        .format(lista_personajes[mas_bajo]["nombre"],
                lista_personajes[mas_bajo]["identidad"]))
    

# 7. Calcular e informar cual es el superhéroe más y menos pesado.
def mostrar_mas_pesado():
    mas_pesado = None
    for i in range(len(lista_personajes)):
        if(mas_pesado is None or 
        lista_personajes[i]["peso"] > lista_personajes[mas_pesado]["peso"]):
            mas_pesado = i    
    print("Superheroe mas pesado: {0} - Peso: {1}"
          .format(lista_personajes[mas_pesado]["nombre"],
                  lista_personajes[mas_pesado]["peso"]))
def mostrar_menos_pesado():
    menos_pesado = None
    for i in range(len(lista_personajes)):
        if(menos_pesado is None or 
        lista_personajes[i]["peso"] < lista_personajes[menos_pesado]["peso"]):
            menos_pesado = i    
    print("Superheroe menos pesado: {0} - Peso: {1}"
          .format(lista_personajes[menos_pesado]["nombre"],
                  lista_personajes[menos_pesado]["peso"]))    




while True:
    print("\nMenú de opciones:")
    print("1. Imprimir los nombres de cada superheroe")
    print("2. Imprimir los nombres de los superheroes junto con su altura")
    print("3. Mostrar el superheroe mas alto")
    print("4. Mostrar el superheroe mas bajo")
    print("5. Mostrar la altura promedio de los superheroes")
    print("6. Informar que identidad tienen los superheroes mas alto y bajo")
    print("7. Mostrar los superheroes mas y menos pesados")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")
    match opcion:
        case '1':
            imprimir_todos_los_nombres()
        case '2':
            imprimir_nombre_y_altura()
        case '3':
            mostrar_mas_alto()
        case '4':
            mostrar_mas_bajo()
        case '5':
            mostrar_promedio_alturas()
        case '6':
            imprimir_identidad_alto()
            imprimir_identidad_bajo()
        case '7':
            mostrar_mas_pesado()
            mostrar_menos_pesado()
        case '0':
            break
        case other:
             print("\nOpción inválida. Intente de nuevo.")
        