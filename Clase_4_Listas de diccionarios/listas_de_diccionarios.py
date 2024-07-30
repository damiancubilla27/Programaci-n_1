lista_miembros = [{"id":1, "nombre":"damian", "edad":27, "membresia":"anual"},
                {"id":2, "nombre":"camila", "edad":24, "membresia":"mensual"},
                {"id":3, "nombre":"aldana", "edad":16, "membresia":"anual"},
                {"id":4, "nombre":"kiara", "edad":20, "membresia":"anual"}]

while True:
    print("\nMenu de opciones: ")
    print("1. Agregar un nuevo miembro.")
    print("2. Mostrar la informacion de todos los miembros.")
    print("3. Actualizar el tipo de membresia de un miembro.")
    print("4. Buscar informacion de un miembro.")
    print("5. Calcular el promedio de edad de los miembros.")
    print("6. Buscar el miembro mas joven y el mas viejo.")
    print("0. Salir del programa")
    opcion = int(input("Ingrese opcion: "))
    match(opcion):
        case 1:
            nuevo_miembro = {}
            nuevo_miembro["id"] = int(input("Ingrese nuevo id: "))
            nuevo_miembro["nombre"] = input("Ingrese nuevo nombre: ")
            nuevo_miembro["edad"] = int(input("Ingrese edad nueva: "))
            nuevo_miembro["membresia"] = input("Ingrese la nueva membresia: ")
            lista_miembros.append(nuevo_miembro)
        case 2:
            for elemento in lista_miembros:
                print(f'{elemento["id"]} - {elemento["nombre"]} - {elemento["edad"]} - {elemento["membresia"]}')
        case 3:
            id_ingresado = int(input("Ingrese id a actualizar: "))
            for elemento in lista_miembros:
                if(elemento["id"] == id_ingresado):
                    elemento["membresia"] = input("Ingrese nueva membresia: ")
        case 4:
            id_ingresado = int(input("Ingrese id a actualizar: "))
            for elemento in lista_miembros:
                if(elemento["id"] == id_ingresado):
                    print(f'{elemento["id"]} - {elemento["nombre"]} - {elemento["edad"]} - {elemento["membresia"]}')
        case 5:
            suma = 0
            promedio = 0
            for elemento in lista_miembros:
                suma += elemento["edad"]
            promedio = suma / len(lista_miembros)
            print(f"El promedio de edad es: {promedio}")
        case 6:
            mas_joven = lista_miembros[0]["edad"]
            mas_viejo = lista_miembros[0]["edad"]
            for elemento in lista_miembros:
                if(elemento["edad"] < mas_joven):
                    mas_joven = elemento["edad"]
                if(elemento["edad"] > mas_viejo):
                    mas_viejo = elemento["edad"]
            print(f"El mas joven tiene {mas_joven} años")
            print(f"El mas viejo tiene {mas_viejo} años")
        case 0:
            break
        case other:
            print("Error en el ingreso de numero..")