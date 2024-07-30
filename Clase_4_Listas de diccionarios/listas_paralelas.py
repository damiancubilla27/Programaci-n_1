lista_ids = [1,2,3,4]
lista_nombres = ["damian","camila","aldana","kiara"]
lista_edades = [20,24,16,12]
lista_membresias = ["anual","mensual","anual","mensual"]

while True:
    # Mostrar menú de opciones
    print("\nMenú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = int(input("\nIngrese la opción deseada: "))
    if(opcion == 1):
        lista_ids.append(int(input("Ingrese id nuevo: ")))
        lista_nombres.append(input("Ingrese nombre nuevo: "))
        lista_edades.append(int(input("Ingrese edad nueva: ")))
        lista_membresias.append(input("Ingrese membresia: "))
    elif(opcion == 2):
        for elemento in range(len(lista_ids)):
            print(f"{lista_ids[elemento]} - {lista_nombres[elemento]} - {lista_edades[elemento]} - {lista_membresias[elemento]}")
    elif(opcion == 3):
        id_ingresado = int(input("Ingrese id a actualizar: "))
        for elemento in range(len(lista_ids)):
            if(lista_ids[elemento] == id_ingresado):
                lista_membresias[elemento] = input("Ingrese nueva membresia: ")
    elif(opcion == 4):
        id_ingresado = int(input("Ingrese id para mostrar informacion: "))
        for elemento in range(len(lista_ids)):
            if(lista_ids[elemento] == id_ingresado):
                print(f"{lista_ids[elemento]} - {lista_nombres[elemento]} - {lista_edades[elemento]} - {lista_membresias[elemento]}")
    elif(opcion == 5):
        suma = 0
        promedio = 0
        for elemento in range(len(lista_ids)):
            suma += lista_edades[elemento]
        promedio = suma / len(lista_edades)
        print(f"El promedio de edades es de: {promedio}")
    elif(opcion == 6):
        mas_joven = lista_edades[0]
        mas_viejo = lista_edades[0]
        for elemento in range(len(lista_ids)):
            if(lista_edades[elemento] < mas_joven):
                mas_joven = lista_edades[elemento]
            if(lista_edades[elemento] > mas_viejo):
                mas_viejo = lista_edades[elemento]
        print(f"La persona mas joven tiene: {mas_joven}")
        print(f"La persona mas vieja tiene: {mas_viejo}")
    elif(opcion == 0):
        break
    else:
        print("\nOpción inválida. Intente de nuevo.")