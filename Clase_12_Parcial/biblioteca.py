ACTIVO = "Activo"
CANCELADO = "Cancelado"
FINALIZADO = "Finalizado"
BAJA_CORRECTA = 1
BAJA_CANCELADA = 2
BAJA_ERRONEA = 3
MODIFICACION_CORRECTA = 1
MODIFICACION_CANCELADA = 2
MODIFICACION_ERRONEA = 3
ALTA_CORRECTA = 1
ALTA_CANCELADA = 2
ALTA_ERRONEA = 3

#--------------------------------------------------------------------- Impresion
def mostrar_proyectos(lista_proyectos:list)->None:
    '''
    Función:
        Recorre una lista de proyectos y construye una cadena con la información 
        formateada de cada proyecto, luego imprime esta cadena.
    Parámetros:
        lista_proyectos (list): Una lista de diccionarios donde cada diccionario 
        contiene la información de un proyecto.
    Retorno:
        None: Esta función no devuelve ningún valor.
    '''
    informacion = "PROYECTOS\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO\n"
    for proyecto in lista_proyectos:            
            informacion += f"{proyecto['id']} | {proyecto['Nombre del Proyecto']} | {proyecto['Descripción']} | {proyecto['Fecha de inicio']} | {proyecto['Fecha de Fin']} | {proyecto['Presupuesto']} | {proyecto['Estado']}\n"
    print(informacion)

def mostrar_el_proyecto(empleado:dict)->None:
    '''
    Función:
        Construye una cadena con la información detallada de un proyecto específico 
        y la imprime.
    Parámetros:
        empleado (dict): Un diccionario que contiene la información de un proyecto.
    Retorno:
        None: Esta función no devuelve ningún valor.
    '''
    informacion = "PROYECTO\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO\n"
    informacion += f"{empleado['id']} | {empleado['Nombre del Proyecto']} | {empleado['Descripción']} | {empleado['Fecha de inicio']} | {empleado['Fecha de Fin']} | {empleado['Presupuesto']} | {empleado['Estado']}\n"
    print(informacion)

#--------------------------------------------------------------------- Punto 1
def ingresar_nombre(mensaje:str, mensaje_error:str)->str:
    '''
    Función:
        Muestra un mensaje solicitando al usuario que ingrese un nombre.
        Valida que el nombre ingresado cumpla con las siguientes condiciones:
        - La longitud del nombre debe ser mayor a 0 y menor o igual a 30.
        - El nombre debe contener solo caracteres alfabéticos.
        Si el nombre ingresado no cumple con las condiciones, se muestra un 
        mensaje de error y se solicita nuevamente el ingreso del nombre.
    Parámetros:
        mensaje (str): El mensaje que se muestra al usuario para 
        solicitar el ingreso del nombre.
        mensaje_error (str): El mensaje que se muestra al usuario en caso 
        de que el nombre ingresado no sea válido.
    Retorno:
        str: El nombre ingresado por el usuario que cumple con 
        las condiciones de validación.
    '''
    dato = input(mensaje)
    confirmar_dato = True
    while confirmar_dato:
        if(len(dato) > 0 and len(dato) <= 30 and dato.isalpha()):
            confirmar_dato = False
        else:
            dato = input(mensaje_error)
    return dato

def ingresar_descripcion(mensaje:str, mensaje_error:str)->str:
    '''
    Función:
        Muestra un mensaje solicitando al usuario que ingrese una descripción.
        Valida que la descripción ingresada cumpla con las siguientes condiciones:
        - La longitud de la descripción debe ser mayor a 0 y menor o igual a 200.
        - La descripción debe contener solo caracteres alfanuméricos y espacios.
        Si la descripción ingresada no cumple con las condiciones, se muestra un 
        mensaje de error y se solicita nuevamente el ingreso de la descripción.
    Parámetros:
        mensaje (str): El mensaje que se muestra al usuario para solicitar el 
        ingreso de la descripción.
        mensaje_error (str): El mensaje que se muestra al usuario en caso de que 
        la descripción ingresada no sea válida.
    Retorno:
        str: La descripción ingresada por el usuario que cumple con las 
        condiciones de validación.
    '''
    dato = input(mensaje)
    dato_sin_espacios = None
    confirmar_dato = True
    while confirmar_dato:
        dato_sin_espacios = dato.replace(" ", "")
        if(len(dato) > 0 and len(dato) <= 200 and dato_sin_espacios.isalnum()):
            confirmar_dato = False
        else:
            dato = input(mensaje_error)
    return dato

def ingresar_presupuesto(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->int:
    '''
    Función:
        Muestra un mensaje solicitando al usuario que ingrese un presupuesto.
        Valida que el presupuesto ingresado cumpla con las siguientes condiciones:
        - Debe ser un número entero.
        - Debe estar dentro del rango especificado.
        Si el presupuesto ingresado no cumple con las condiciones, se muestra un mensaje 
        de error y se solicita nuevamente el ingreso del presupuesto.
    Parámetros:
        mensaje (str): El mensaje que se muestra al usuario para solicitar el 
        ingreso del presupuesto.
        mensaje_error (str): El mensaje que se muestra al usuario en caso de 
        que el presupuesto ingresado no sea válido.
        minimo (int): El valor mínimo aceptable para el presupuesto.
        maximo (int): El valor máximo aceptable para el presupuesto.
    Retorno:
        int: El presupuesto ingresado por el usuario que cumple 
        con las condiciones de validación.
    '''
    confirmar_dato = True
    while confirmar_dato:
        dato = input(mensaje)
        if dato.isdigit():
            dato = int(dato)
            if dato > minimo and dato < maximo:
                confirmar_dato = False
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)
    return dato

def ingresar_fecha_inicio(mensaje_dia:str, mensaje_mes:str, mensaje_año:str, mensaje_error:str)->str:
    '''
    Función:
        Muestra mensajes solicitando al usuario que ingrese el día, mes y año de una fecha de inicio.
        Valida que los valores ingresados cumplan con las siguientes condiciones:
        - El día debe ser un número entero entre 1 y 31.
        - El mes debe ser un número entero entre 1 y 12.
        - El año debe ser un número entero mayor a 2000.
        Si los valores ingresados no cumplen con las condiciones, se muestra un mensaje de error 
        y se solicita nuevamente el ingreso de los valores.
    Parámetros:
        mensaje_dia (str): El mensaje que se muestra al usuario para solicitar el ingreso del día.
        mensaje_mes (str): El mensaje que se muestra al usuario para solicitar el ingreso del mes.
        mensaje_año (str): El mensaje que se muestra al usuario para solicitar el ingreso del año.
        mensaje_error (str): El mensaje que se muestra al usuario en caso de que los valores 
        ingresados no sean válidos.
    Retorno:
        str: La fecha de inicio ingresada por el usuario en el formato "día-mes-año".
    '''
    confirmar_dato = True
    while confirmar_dato:
        dia = input(mensaje_dia)
        mes = input(mensaje_mes)
        año = input(mensaje_año)
        if dia.isdigit() and mes.isdigit() and año.isdigit():
            dia = int(dia)
            mes = int(mes)
            año = int(año)
            if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and año > 2000:
                confirmar_dato = False
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)
    fecha_finalizada = f"{dia}-{mes}-{año}"
    return fecha_finalizada

def ingresar_fecha_fin(mensaje_dia:str, mensaje_mes:str, mensaje_año:str, mensaje_error:str, fecha_inicio:str, mensaje_fecha_mala:str)->str:
    '''
    Función:
        Utiliza la función `ingresar_fecha_inicio` para solicitar al usuario que ingrese una 
        fecha de finalización.
        Verifica que la fecha de finalización sea posterior o igual a la fecha de inicio proporcionada.
        Si la fecha de finalización no es válida (anterior a la fecha de inicio), 
        muestra un mensaje de error y solicita nuevamente la fecha de finalización.
    Parámetros:
        mensaje_dia (str): El mensaje que se muestra al usuario para solicitar el ingreso del día.
        mensaje_mes (str): El mensaje que se muestra al usuario para solicitar el ingreso del mes.
        mensaje_año (str): El mensaje que se muestra al usuario para solicitar el ingreso del año.
        mensaje_error (str): El mensaje que se muestra al usuario en caso de que los valores 
        ingresados no sean válidos.
        fecha_inicio (str): La fecha de inicio en el formato "día-mes-año" que se utiliza como referencia.
        mensaje_fecha_mala (str): El mensaje que se muestra al usuario en caso de que la fecha 
        de finalización sea anterior a la fecha de inicio.
    Retorno:
        str: La fecha de finalización ingresada por el usuario en el formato "día-mes-año", 
        validada para ser posterior o igual a la fecha de inicio.
    '''
    fecha_final = ingresar_fecha_inicio(mensaje_dia,mensaje_mes,mensaje_año,mensaje_error)
    lista_final_fecha = fecha_final.split("-")
    lista_inicio_fecha = fecha_inicio.split("-")
    if (int(lista_inicio_fecha[2]) < int(lista_final_fecha[2])):
        return fecha_final
    elif(int(lista_inicio_fecha[2]) == int(lista_final_fecha[2]) and int(lista_inicio_fecha[1]) < int(lista_final_fecha[1])):
        return fecha_final
    elif(int(lista_inicio_fecha[2]) == int(lista_final_fecha[2]) and int(lista_inicio_fecha[1]) == int(lista_final_fecha[1]) and int(lista_inicio_fecha[0]) <= int(lista_final_fecha[0])):
        return fecha_final
    else:
        print(mensaje_fecha_mala)
        return ingresar_fecha_fin(mensaje_dia,mensaje_mes,mensaje_año,mensaje_error,fecha_inicio,mensaje_fecha_mala)


def confirmacion_proyecto(mensaje:str, mensaje_error:str)->bool:
    '''
    Función:
        Pide al usuario una confirmación ingresando 'S' para sí o 'N' para no.
        Si el usuario ingresa un valor diferente a 'S' o 'N', se muestra un 
        mensaje de error y se solicita la confirmación nuevamente.
        La función convierte la entrada del usuario a mayúsculas para asegurar 
        que la comparación sea insensible a mayúsculas/minúsculas.
    Parámetros:
        mensaje (str): El mensaje que se muestra al usuario para solicitar la confirmación.
        mensaje_error (str): El mensaje que se muestra al usuario en caso de que 
        la entrada no sea válida (ni 'S' ni 'N').
    Retorno:
        bool: `True` si el usuario confirma con 'S', `False` si el usuario responde con 'N'.
    '''
    confirmacion = input(mensaje)
    confirmacion = confirmacion.upper()
    while confirmacion != 'S' and confirmacion != 'N':
        confirmacion = input(mensaje_error)
        confirmacion = confirmacion.upper()
    if(confirmacion == 'S'):
        retorno = True
    else:
        retorno = False
    return retorno

def agregar_proyecto(id_autoincremental:int, lista_proyectos:list)->bool:
    '''
    Función:
        Solicita al usuario ingresar el nombre, descripción, fecha de inicio, fecha de 
        finalización, y presupuesto del nuevo proyecto.
        Valida cada dato ingresado por el usuario según ciertos criterios (longitud, formato, rango).
        Muestra la información del proyecto ingresado para su confirmación por parte del usuario.
        Si el usuario confirma el alta del proyecto, lo añade a la lista de proyectos.
    Parámetros:
        id_autoincremental (int): El identificador autoincremental para el nuevo proyecto.
        lista_proyectos (list): La lista de proyectos a la que se agregará el nuevo proyecto.
    Retorno:
        bool: `True` si se agrega el proyecto correctamente a la lista, `False` si 
        el usuario no confirma el alta del proyecto.
    '''
    retorno = False
    nombre_proyecto = ingresar_nombre("Ingrese su nombre: ", "ERROR\nReingrese su nombre: ")
    descripcion_proyecto = ingresar_descripcion("Ingrese descripcion: ", "ERROR\nReingrese descripcion: ")
    fecha_inicio = ingresar_fecha_inicio("Ingrese el día de inicio del proyecto(01 al 31): ", 
    "Ingrese el mes de inicio del proyecto(01 al 12): ",
    "Ingrese el año de inicio del proyecto(desde 2000): ",
    "ERROR\nReingrese una fecha válida en el formato DD/MM/AAAA. Inténtelo de nuevo: ")
    fecha_final = ingresar_fecha_fin("Ingrese el día de finalizacion del proyecto(01 al 31): ", 
    "Ingrese el mes de finalizacion del proyecto(01 al 12): ",
    "Ingrese el año de finalizacion del proyecto(desde 2000): ",
    "ERROR\nReingrese una fecha válida en el formato DD/MM/AAAA. Inténtelo de nuevo: ", fecha_inicio, "La fecha de fin no puede ser anterior o igual a la fecha de inicio.")
    presupuesto_proyecto = ingresar_presupuesto("Ingrese presupuesto: ", "Error", 500000, 99999999)
    
    proyecto = {"id":id_autoincremental, "Nombre del Proyecto":nombre_proyecto, "Descripción":descripcion_proyecto, "Fecha de inicio":fecha_inicio, "Fecha de Fin":fecha_final, "Presupuesto": presupuesto_proyecto, "Estado":ACTIVO}
    mostrar_el_proyecto(proyecto)
    if(confirmacion_proyecto("Desea confirma el alta (S/N): ", "ERROR\nReingrese si desea el alta (S/N): ")):
        lista_proyectos.append(proyecto)
        retorno = True
    return retorno

#--------------------------------------------------------------------- Punto 2
def pedir_clave()->int:
    '''
    Función:
        Muestra un menú de opciones numeradas correspondientes a diferentes atributos de un proyecto.
        Solicita al usuario que ingrese el número de la opción deseada.
        Valida que el número ingresado esté dentro del rango válido (1 a 6).
        Si el número ingresado no está dentro del rango, solicita al usuario 
        que ingrese nuevamente hasta que sea válido.
    Parámetros:
        No tiene parámetros de entrada.
    Retorno:
        int: El número de la opción seleccionada por el usuario, entre 1 y 6.
    '''
    retorno = int(input("Que desea modificar:\n1.Nombre de proyecto\n2.Descripcion\n3.Fecha de Inicio\n4.Fecha de Fin\n5.Presupuesto\n6.Estado\nIngrese Opcion: "))
    while retorno < 1 or retorno > 6:
        retorno = int(input("Que desea modificar:\n1.Nombre de proyecto\n2.Descripcion\n3.Fecha de Inicio\n4.Fecha de Fin\n5.Presupuesto\n6.Estado\nIngrese Opcion: "))
    return retorno

def ingreso_estado()->str:
    '''
    Función:
        Muestra un menú con tres opciones de estado: Activo, Cancelado y Finalizado.
        Solicita al usuario que ingrese el número correspondiente al estado deseado.
        Valida que el número ingresado esté dentro del rango válido (1 a 3).
        Si el número ingresado no está dentro del rango, solicita al usuario 
        que ingrese nuevamente hasta que sea válido.
        Devuelve la cadena de texto correspondiente al estado seleccionado.

    Parámetros:
        No tiene parámetros de entrada.

    Retorno:
        str: La cadena de texto correspondiente al estado seleccionado por el 
        usuario (ACTIVO, CANCELADO o FINALIZADO).
    '''
    numero = int(input("ESTADOS:\n1.Activo\n2.Cancelado\n3.Finalizado\nIngrese numero: "))
    retorno = None
    while numero < 1 or numero > 3:
        numero = int(input("ESTADOS:\n1.Activo\n2.Cancelado\n3.Finalizado\nIngrese numero: "))
    if(numero == 1):
        retorno = ACTIVO
    elif(numero == 2):
        retorno = CANCELADO
    else:
        retorno = FINALIZADO
    return retorno

def modificar_proyecto(lista_proyectos:list):
    '''
    Función:
        Muestra todos los proyectos disponibles.
        Solicita al usuario el ID del proyecto que desea modificar.
        Busca el proyecto en la lista utilizando el ID proporcionado.
        Si el proyecto es encontrado, muestra los detalles del proyecto.
        Pide al usuario que confirme si desea modificar el proyecto.
        Actualiza el campo seleccionado con el nuevo valor ingresado por el usuario.
        Retorna un código indicando si la modificación fue correcta, errónea o cancelada.
    Parámetros:
        lista_proyectos (list): Lista de proyectos a modificar.
    Retorno:
        int: Código que indica el resultado de la modificación:
            - MODIFICACION_ERRONEA (-1): Si la modificación no se pudo realizar.
            - MODIFICACION_CORRECTA (1): Si la modificación se realizó correctamente.
            - MODIFICACION_CANCELADA (0): Si la modificación fue cancelada por el usuario.
    '''
    retorno = MODIFICACION_ERRONEA
    mostrar_proyectos(lista_proyectos)
    id_a_moficar = int(input("Ingrese el id del proyecto a modificar: "))
    indice = buscar_proyecto(lista_proyectos, id_a_moficar)
    if(indice != None):
        mostrar_el_proyecto(lista_proyectos[indice])
        confirmacion = confirmacion_proyecto("Desea confirma la modificacion (S/N): ", "ERROR\nReingrese si desea la modificacion (S/N): ")
        if(confirmacion):
            ingreso_clave = pedir_clave()
            if(ingreso_clave == 1):
                nombre_nuevo = ingresar_nombre("Ingrese nuevo nombre: ", "ERROR\nReingrese nuevo nombre: ")
                lista_proyectos[indice].update({"Nombre del Proyecto":nombre_nuevo})
            elif(ingreso_clave == 2):
                nueva_descripcion = ingresar_descripcion("Ingrese nueva descripcion: ", "ERROR\nReingrese nueva decripcion: ")
                lista_proyectos[indice].update({"Descripción":nueva_descripcion})
            elif(ingreso_clave == 3):
                nueva_fecha_inicio = ingresar_fecha_inicio("Ingrese el día de inicio del proyecto(01 al 31): ", 
                "Ingrese el mes de inicio del proyecto(01 al 12): ",
                "Ingrese el año de inicio del proyecto(desde 2000): ",
                "ERROR\nReingrese una fecha válida en el formato DD/MM/AAAA. Inténtelo de nuevo: ")
                lista_proyectos[indice].update({"Fecha de inicio":nueva_fecha_inicio})
            elif(ingreso_clave == 4):
                nueva_fecha_final = ingresar_fecha_fin("Ingrese el día de inicio del proyecto(01 al 31): ", 
                "Ingrese el mes de inicio del proyecto(01 al 12): ",
                "Ingrese el año de inicio del proyecto(desde 2000): ",
                "ERROR\nReingrese una fecha válida en el formato DD/MM/AAAA. Inténtelo de nuevo: ", lista_proyectos[indice]["fecha_inicio"], "La fecha de fin no puede ser anterior o igual a la fecha de inicio.")
                lista_proyectos[indice].update({"Fecha de Fin": nueva_fecha_final})
            elif(ingreso_clave == 5):
                nuevo_presupuestp = ingresar_presupuesto("Ingrese presupuesto: ", "Error", 500000, 99999999)
                lista_proyectos[indice].update({"Presupuesto":nuevo_presupuestp})
            else:
                nuevo_estado = ingreso_estado()
                lista_proyectos[indice].update({"Estado":nuevo_estado})
            retorno = MODIFICACION_CORRECTA
        else:
            retorno = MODIFICACION_CANCELADA
    return retorno

#--------------------------------------------------------------------- Punto 3
def buscar_proyecto(lista_proyectos:list, id_a_buscar:int)->int:
    '''
    Función:
        Itera sobre la lista de proyectos y compara el ID de cada proyecto con el ID proporcionado.
        Si encuentra un proyecto con el ID correspondiente, retorna el índice del proyecto en la lista.
        Si no encuentra el proyecto, retorna `None`.
    Parámetros:
        lista_proyectos (list): Lista de proyectos donde se va a buscar el proyecto. 
        Cada proyecto es un diccionario que contiene la clave "id".
        id_a_buscar (int): ID del proyecto que se desea buscar en la lista.
    Retorno:
        int: Indice del proyecto en la lista si es encontrado. 
        Retorna `None` si no se encuentra el proyecto.
    '''
    indice_producto = None
    for i in range(len(lista_proyectos)):
        if(lista_proyectos[i]["id"] == id_a_buscar):
            indice_producto = i
            break
    return indice_producto

def bajar_proyecto(lista_proyectos:list)->int:
    '''
    Función:
        Muestra la lista de proyectos disponibles.
        Solicita al usuario que ingrese el ID del proyecto que desea dar de baja.
        Busca el proyecto en la lista por su ID.
        Si el proyecto es encontrado, muestra la información del proyecto y 
        solicita confirmación del usuario para cancelar el proyecto.
        Si el usuario confirma, cambia el estado del proyecto a "Cancelado".
        Retorna el estado de la operación.
    Parámetros:
        lista_proyectos (list): Lista de proyectos. Cada proyecto es un diccionario 
        que contiene la clave "id" y "Estado".
    Retorno:
        int: Retorna un código de estado indicando el resultado de la operación:
            - `BAJA_CORRECTA` si la baja del proyecto fue exitosa.
            - `BAJA_CANCELADA` si el usuario cancela la baja.
            - `BAJA_ERRONEA` si ocurre un error, como no encontrar el proyecto.
    '''
    retorno = BAJA_ERRONEA
    mostrar_proyectos(lista_proyectos)
    id_a_borrar = int(input("Ingrese el id a dar de baja: "))
    indice = buscar_proyecto(lista_proyectos, id_a_borrar)
    if(indice != None):
        mostrar_el_proyecto(lista_proyectos[indice])
        confirmacion = confirmacion_proyecto("Desea confirma la baja (S/N): ", "ERROR\nReingrese si desea la baja (S/N): ")
        if(confirmacion):
            lista_proyectos[indice]["Estado"] = CANCELADO
            retorno = BAJA_CORRECTA
        else:
            retorno = BAJA_CANCELADA
    return retorno

#--------------------------------------------------------------------- Punto 4
def comprobar_finalizacion(dict_proyecto:dict)->bool:
    '''
    Función:
        Toma un diccionario de proyecto y compara la fecha de finalización del proyecto 
        con una fecha actual predefinida.
        Retorna `True` si la fecha de finalización es anterior o igual a la fecha actual, 
        indicando que el proyecto ha finalizado.
        Retorna `False` si la fecha de finalización es posterior a la fecha actual, 
        indicando que el proyecto no ha finalizado.
    Parámetros:
        dict_proyecto (dict): Diccionario que contiene la información del proyecto. 
        Debe incluir la clave "Fecha de Fin" con el formato "DD-MM-AAAA".
    Retorno:
        bool: `True` si el proyecto ha finalizado, `False` en caso contrario.
    '''
    retorno = True
    fecha_final = dict_proyecto["Fecha de Fin"]
    lista_final_fecha = fecha_final.split("-")
    dia_final = int(lista_final_fecha[0])
    mes_final = int(lista_final_fecha[1])
    anio_final = int(lista_final_fecha[2])
    
    fecha_actual = "12-06-2024"
    lista_actual_fecha = fecha_actual.split("-")
    
    dia_actual = int(lista_actual_fecha[0])
    mes_actual = int(lista_actual_fecha[1])
    anio_actual = int(lista_actual_fecha[2])
    
    if anio_final < anio_actual:
        return retorno
    elif anio_final == anio_actual:
        if mes_final < mes_actual:
            return retorno
        elif mes_final == mes_actual:
            if dia_final <= dia_actual:
                return retorno
    else:
        retorno = False
    return retorno

def cambiar_estado_por_finalizado(lista_proyectos:list)->int:
    '''
    Función:
        Itera sobre una lista de proyectos y cambia el estado de aquellos 
        proyectos que no están ya finalizados y cuya fecha de finalización 
        es anterior o igual a la fecha actual. 
        Imprime un mensaje indicando el ID de cada proyecto cuyo estado ha 
        sido cambiado a "Finalizado".
    Parámetros:
        lista_proyectos (list): Lista de diccionarios, donde cada diccionario 
        representa un proyecto y debe incluir las claves "Estado" y "Fecha de Fin" 
        con el formato "DD-MM-AAAA".
    Retorno:
        int: Retorna -1 si la lista de proyectos está vacía.
    '''
    if(lista_proyectos != []):
        for elemento in lista_proyectos:
            if(elemento["Estado"] != "Finalizado"):
                if(comprobar_finalizacion(elemento) == True):
                    elemento.update({"Estado":FINALIZADO})
                    print(f"Se cambio el estado de el id: {elemento['id']}")
    else:
        return -1

#--------------------------------------------------------------------- Punto 6
def calcular_promedio_presupuesto(lista_proyectos:list)->float:
    '''
    Función:
        Itera sobre una lista de proyectos y suma los valores de presupuesto de cada proyecto. 
        Luego, calcula el promedio dividiendo la suma total por el número de proyectos en la lista.
    Parámetros:
        lista_proyectos (list): Lista de diccionarios, donde cada diccionario representa 
        un proyecto y debe incluir la clave "Presupuesto".
    Retorno:
        float: El promedio del presupuesto de los proyectos. 
        Retorna -1 si la lista de proyectos está vacía.
    '''
    if(lista_proyectos != []):
        contador = len(lista_proyectos)
        suma = 0
        promedio = 0
        for proyecto in lista_proyectos:
            suma += int(proyecto["Presupuesto"])
        promedio = suma / contador
        return promedio
    else:
        return -1

#--------------------------------------------------------------------- Punto 7
def buscar_proyecto_por_nombre(lista_proyectos:list)->int:
    '''
    Función:
        Itera sobre una lista de proyectos buscando un proyecto cuyo nombre 
        coincida con el nombre ingresado por el usuario. 
        Si encuentra el proyecto, muestra su información y confirma que el 
        proyecto ha sido encontrado. 
        Si no encuentra el proyecto, informa al usuario. Si la lista está vacía, retorna -1.
    Parámetros:
        lista_proyectos (list): Lista de diccionarios, donde cada diccionario representa 
        un proyecto y debe incluir la clave "Nombre del Proyecto".
    Retorno:
        int: Retorna -1 si la lista de proyectos está vacía. 
        En caso contrario, no retorna ningún valor.
    '''
    if(lista_proyectos != []):
        encontrado = False
        mostrar_proyectos(lista_proyectos)
        nombre_buscar = input("Ingrese el nombre del proyecto: ")
        for proyecto in lista_proyectos:
            if(proyecto["Nombre del Proyecto"] == nombre_buscar):
                mostrar_el_proyecto(proyecto)
                encontrado = True
                break
        if(encontrado):
            print("Proyecto encontrado")
        else:
            print("No se encontro ningun proyecto con ese nombre!")
    else:
        return -1

#--------------------------------------------------------------------- Punto 8
def pedir_descripcion()->int:
    '''
    Función:
        Muestra un menú al usuario para elegir un criterio de ordenación 
        (Nombre, Presupuesto o Fecha de inicio) para los proyectos. 
        Valida que la entrada del usuario sea una de las opciones válidas 
        y retorna la opción seleccionada como un entero.
    Parámetros:
        No recibe parámetros.
    Retorno:
        int: Retorna el número correspondiente a la opción seleccionada 
        por el usuario (1, 2 o 3).
    '''
    ordenar_por = int(input("Ordenar por:\n1.Nombre\n2.Presupuesto\n3.Fecha de inicio\nElegir: "))
    while ordenar_por < 1 or ordenar_por > 3:
        ordenar_por = int(input("Ordenar por:\n1.Nombre\n2.Presupuesto\n3.Fecha de inicio\nElegir: "))
    return ordenar_por

def pedir_forma()->int:
    '''
    Función:
        Muestra un menú al usuario para elegir una forma de 
        ordenación (ascendente o descendente) y valida que la entrada del usuario 
        sea una de las opciones válidas. Retorna la opción seleccionada como un entero.
    Parámetros:
        No recibe parámetros.
    Retorno:
        int: Retorna el número correspondiente a la opción 
        seleccionada por el usuario (1 para ascendente, 2 para descendente).
    '''
    forma_ordenar = int(input("Forma de ordenar:\n1.Ascendente\n2.Descendente\nElegir:"))
    while forma_ordenar < 1 or forma_ordenar > 2:
        forma_ordenar = int(input("Forma de ordenar:\n1.Ascendente\n2.Descendente\nElegir:"))
    return forma_ordenar

def ordenar_por_valor_nombre(lista_proyectos:list, key:str, orden:bool)->list:
    '''
    Función:
        Ordena una lista de proyectos en función de un valor específico.
    Parámetros:
        lista_proyectos (list): Lista de diccionarios que representan proyectos.
        key (str): Clave del diccionario por la cual se desea ordenar.
        orden (bool): Indica el orden de la ordenación. 
        True para ascendente, False para descendente.
    Retorno:
        list: Lista de proyectos ordenada.
        
    '''
    flag_swap = True
    rango_lista = len(lista_proyectos)
    while(flag_swap):
        flag_swap = False
        rango_lista = rango_lista-1
        for proyecto in range(rango_lista):
            if((orden == True and lista_proyectos[proyecto][key] > lista_proyectos[proyecto+1][key]) or 
                (orden == False and lista_proyectos[proyecto][key] < lista_proyectos[proyecto+1][key])):

                aux = lista_proyectos[proyecto]
                lista_proyectos[proyecto] = lista_proyectos[proyecto+1]
                lista_proyectos[proyecto+1] = aux
                flag_swap = True
    return lista_proyectos

def ordenar_por_presupuesto(lista_proyectos:list, key:str, orden:bool) -> list:
    '''
    Función:
        Ordena una lista de proyectos en función de un valor específico.
    Parámetros:
        lista_proyectos (list): Lista de diccionarios que representan proyectos.
        key (str): Clave del diccionario por la cual se desea ordenar.
        orden (bool): Indica el orden de la ordenación. 
        True para ascendente, False para descendente.
    Retorno:
        list: Lista de proyectos ordenada.
        
    '''
    flag_swap = True
    rango_lista = len(lista_proyectos)
    while flag_swap:
        flag_swap = False
        rango_lista -= 1
        for proyecto in range(rango_lista):
            valor_actual = int(lista_proyectos[proyecto][key])
            valor_siguiente = int(lista_proyectos[proyecto + 1][key])
            
            if ((orden == True and valor_actual > valor_siguiente) or 
                (orden == False and valor_actual < valor_siguiente)):
                aux = lista_proyectos[proyecto]
                lista_proyectos[proyecto] = lista_proyectos[proyecto + 1]
                lista_proyectos[proyecto + 1] = aux
                flag_swap = True
    return lista_proyectos

def ordenar_por_fecha_inicio(lista_proyectos:list, key:str, orden:bool) -> list:
    '''
    Función:
        Ordena una lista de proyectos en función de un valor específico.
    Parámetros:
        lista_proyectos (list): Lista de diccionarios que representan proyectos.
        key (str): Clave del diccionario por la cual se desea ordenar.
        orden (bool): Indica el orden de la ordenación. 
        True para ascendente, False para descendente.
    Retorno:
        list: Lista de proyectos ordenada.
        
    '''
    flag_swap = True
    rango_lista = len(lista_proyectos)
    while flag_swap:
        flag_swap = False
        rango_lista -= 1
        for proyecto in range(rango_lista):
            fecha_actual = lista_proyectos[proyecto][key].split("-")
            fecha_siguiente = lista_proyectos[proyecto + 1][key].split("-")
            
            dia_actual = int(fecha_actual[0])
            mes_actual = int(fecha_actual[1])
            año_actual = int(fecha_actual[2])
            dia_siguiente = int(fecha_siguiente[0])
            mes_siguiente = int(fecha_siguiente[1])
            año_siguiente = int(fecha_siguiente[2])
            
            if ((orden == True and (año_actual, mes_actual, dia_actual) > (año_siguiente, mes_siguiente, dia_siguiente)) or 
                (orden == False and (año_actual, mes_actual, dia_actual) < (año_siguiente, mes_siguiente, dia_siguiente))):
                aux = lista_proyectos[proyecto]
                lista_proyectos[proyecto] = lista_proyectos[proyecto + 1]
                lista_proyectos[proyecto + 1] = aux
                flag_swap = True
    return lista_proyectos

def buscar_formas_de_ordenar(lista_proyectos:list)->None:
    '''
    Función:
        Esta función permite al usuario seleccionar cómo desea ordenar la lista de proyectos, 
        ya sea por nombre, presupuesto o fecha de inicio, y en orden ascendente o descendente. 
        Luego, muestra la lista de proyectos ordenada según la selección.
    Parámetros:
        lista_proyectos (list): La lista de proyectos a ordenar y mostrar.
    Retorno:
        La función muestra la lista de proyectos ordenada o devuelve -1 si la lista de 
        proyectos está vacía.
    '''
    if(lista_proyectos != []):
        descripcion = pedir_descripcion()
        forma = pedir_forma()
        if(descripcion == 1):
            if(forma == 1):
                lista_ordenada = ordenar_por_valor_nombre(lista_proyectos, "Nombre del Proyecto", True)
                mostrar_proyectos(lista_ordenada)
            else:
                lista_ordenada = ordenar_por_valor_nombre(lista_proyectos, "Nombre del Proyecto", False)
                mostrar_proyectos(lista_ordenada)
        elif(descripcion == 2):
            if(forma == 1):
                lista_ordenada = ordenar_por_presupuesto(lista_proyectos, "Presupuesto", True)
                mostrar_proyectos(lista_ordenada)
            else:
                lista_ordenada = ordenar_por_presupuesto(lista_proyectos, "Presupuesto", False)
                mostrar_proyectos(lista_ordenada)
        elif(descripcion == 3):
            if(forma == 1):
                lista_ordenada = ordenar_por_fecha_inicio(lista_proyectos, "Fecha de inicio", True)
                mostrar_proyectos(lista_ordenada)
            else:
                lista_ordenada = ordenar_por_fecha_inicio(lista_proyectos, "Fecha de inicio", False)
                mostrar_proyectos(lista_ordenada)
    else:
        return -1

#--------------------------------------------------------------------- Punto 9
def mostrar_proyectos_cancelados(lista_proyectos:list)->None:
    '''
    Función:
        Esta función recorre la lista de proyectos proporcionada y construye una cadena de texto 
        con la información de los proyectos que tienen el estado "Cancelado". 
        Luego, imprime esta información.
    Parámetros:
        lista_proyectos (list): La lista de proyectos a revisar. 
    Retorno:
        La función imprime la información de los proyectos cancelados.
    '''
    informacion = "PROYECTOS\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO\n"
    for proyecto in lista_proyectos:
            if(proyecto["Estado"] == "Cancelado"):            
                informacion += f"{proyecto['id']} | {proyecto['Nombre del Proyecto']} | {proyecto['Descripción']} | {proyecto['Fecha de inicio']} | {proyecto['Fecha de Fin']} | {proyecto['Presupuesto']} | {proyecto['Estado']}\n"
    print(informacion)

def dar_de_alta_cancelado(lista_proyectos:list)->int:
    '''
    Función:
        Esta función muestra los proyectos cancelados, pide al usuario que ingrese el 
        ID del proyecto que desea reactivar,y cambia su estado a "Activo" si se 
        confirma la operación.
    Parámetros:
        lista_proyectos (list): La lista de proyectos. 
    Retorno:
        int: Retorna una constante que indica el resultado de la operación:
            - ALTA_ERRONEA (3): Si no se encuentra el proyecto o si la lista está vacía.
            - ALTA_CANCELADA (2): Si se cancela la operación.
            - ALTA_CORRECTA (1): Si el proyecto se reactiva correctamente.  
    '''
    retorno = ALTA_ERRONEA
    mostrar_proyectos_cancelados(lista_proyectos)
    id_a_buscar = int(input("Ingrese el id de el proyecto cancelado: "))
    indice_cancelado = buscar_proyecto(lista_proyectos, id_a_buscar)
    if(indice_cancelado != None):
        mostrar_el_proyecto(lista_proyectos[indice_cancelado])
        confirmacion = confirmacion_proyecto("Desea confirma la alta (S/N): ", "ERROR\nReingrese si desea la alta (S/N): ")
        if(confirmacion):
            lista_proyectos[indice_cancelado]["Estado"] = ACTIVO
            retorno = ALTA_CORRECTA
        else:
            retorno = ALTA_CANCELADA
    return retorno

#--------------------------------------------------------------------- Convertir a int
def convertir_id_a_entero(lista_proyectos)->list:
    '''
    Función:
        Esta función recorre una lista de proyectos, donde cada proyecto es un diccionario,
        y convierte el valor del campo 'id' de cada proyecto a un entero.
    Parámetros:
        lista_proyectos (list): La lista de proyectos. Cada proyecto es un diccionario 
        con un campo 'id' que debe ser convertido a entero.
    Retorno:
        list: La lista de proyectos con los IDs convertidos a enteros.
    '''
    for proyecto in lista_proyectos:
        proyecto["id"] = int(proyecto["id"])
    return lista_proyectos

#--------------------------------------------------------------------- Contador de activos
def contador_de_proyectos_activos(lista_proyectos)->int:
    '''
    Función:
        Esta función recorre una lista de proyectos, donde cada proyecto es un diccionario,
        y cuenta cuántos proyectos tienen el estado "Activo".
    Parámetros:
        lista_proyectos (list): La lista de proyectos. 
    Retorno:
        int: El número de proyectos con estado "Activo".
    '''
    contador = 0
    for elemento in lista_proyectos:
        if(elemento["Estado"] == "Activo"):
            contador += 1
    return contador

#--------------------------------------------------------------------- Lista de Finalizados
def buscar_proyectos_finalizados(lista_proyectos:list)->list:
    '''
    Función:
        Esta función recorre una lista de proyectos y filtra aquellos que 
        tienen el estado "Finalizado".
        Los proyectos que cumplen con esta condición se agregan a una nueva lista 
        que se devuelve como resultado.
    Parámetros:
        lista_proyectos (list): La lista de proyectos.
    Retorno:
        list: Una lista de proyectos finalizados.
    '''
    lista_finalizados = []
    for proyecto in lista_proyectos:
            if(proyecto["Estado"] == "Finalizado"):            
                lista_finalizados.append(proyecto)
    return lista_finalizados


'''
D. Calcular el promedio de presupuesto de todos los proyectos que terminaron en medio de la copa
del mundo qatar 2022 (20 de Noviembre a 18 de Diciembre) En caso de que no haya indicar error
'''
def calcular_promedio_qatar(lista_proyectos:list)->None:
    '''
    Función: 
        Calcula y muestra el promedio de los presupuestos de los 
        proyectos realizados durante el periodo de Qatar 2022.
    Parámetros:
        lista_proyectos (list): Lista de diccionarios que representan proyectos.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    contador = 0
    suma = 0
    promedio = 0
    for proyecto in lista_proyectos:
        lista_fechas_inicio = proyecto["Fecha de inicio"].split("-")
        lista_fechas_final = proyecto["Fecha de Fin"].split("-")
        if(int(lista_fechas_inicio[2]) == 2022 and int(lista_fechas_inicio[1]) == 11 and int(lista_fechas_inicio[0]) >= 20):
            if(int(lista_fechas_final[2]) == 2022 and int(lista_fechas_final[1]) <= 12 and int(lista_fechas_final[0]) <= 18):
                suma += proyecto["Presupuesto"]
                contador += 1
    if(suma == 0):
        print("Error, no se encontro ningun proyecto realizado durante Qatar 2022!!")
    else:
        promedio = suma / contador
        print(f"El promedio de los presupuestos de todos los proyectos realizados durante Qatar 2022 es: {promedio}")


'''
C. Mostrar todos los proyectos terminados en medio de la cuarentena del COVID 19 (Marzo de 2020
hasta el fin del 2021 por ejemplo). En caso de que no haya indicar error
'''
def mostrar_proyectos_en_cuarentena(lista_proyectos:list)->None:
    '''
    Función: 
        Muestra los proyectos realizados durante la cuarentena del COVID-19.
    Parámetros:
        lista_proyectos (list): Lista de diccionarios que representan proyectos.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    bandera = False
    for proyecto in lista_proyectos:
        lista_fechas_inicio = proyecto["Fecha de inicio"].split("-")
        lista_fechas_final = proyecto["Fecha de Fin"].split("-")
        if(int(lista_fechas_inicio[2]) >= 2020 and int(lista_fechas_inicio[1]) >= 3 and int(lista_fechas_inicio[0]) >= 1):
            if(int(lista_fechas_final[2]) <= 2021 and int(lista_fechas_final[1]) <= 12 and int(lista_fechas_final[0]) <= 31):
                mostrar_el_proyecto(proyecto)
                bandera = True
    if(bandera == False):
            print("Error, no se encontro ningun proyecto realizado durante la cuarentena del COVID 19!!")