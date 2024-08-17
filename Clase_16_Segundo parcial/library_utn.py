import os
from validaciones import *
from paciente import Paciente
from turno import Turno
from archivos import*

def clear_console():
    """
    The function `clear_console` prompts the user to press Enter to continue and then clears the console
    screen based on the operating system.
    """
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: os.system('cls')    

def UTN_messenger(message: str, message_type: str = None, new_line: bool = False) -> None:
    """
    This is a Python function that prints a message with a specific color and message type.
    
    :param message: The message that needs to be displayed in the console
    :param message_type: The type of message being passed, which can be 'Error', 'Success', 'Info',
    or None. If None, the message will be printed without any formatting
    """
    _b_red: str = '\033[41m'
    _b_green: str = '\033[42m'
    _b_blue: str = '\033[44m'
    _f_white: str = '\033[37m'
    _no_color: str = '\033[0m'
    message_type = message_type.strip().capitalize()
    new_line_char = '\n'
    final_message = f'{new_line_char if new_line else ""}'
    match message_type:
        case 'Error':
            final_message += f'{_b_red}{_f_white}> Error: {message}{_no_color}'
        case 'Success':
            final_message += f'{_b_green}{_f_white}> Success: {message}{_no_color}'
        case 'Info':
            final_message += f'{_b_blue}{_f_white}> Information: {message}{_no_color}'
        case _:
            final_message += message
    print(final_message)

def imprimir_menu():
    '''
    Función:
        Esta función imprime el menú principal en la consola, con las opciones disponibles.
    Parámetros:
        No tiene parámetros de entrada.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    os.system('cls') 
    print("MENU PRINCIPAL\n\n1)Alta paciente\n2)Alta turno\n3)Ordenar turnos\n4)Mostrar pacientes en espera\n5)Atender pacientes\n6)Cobrar atenciones\n7)Cerrar caja\n8)Mostrar informe\n9)Salir")

def crear_objeto_pacientes(lista_json:list):
    lista_pacientes_objetos = []
    for paciente_data in lista_json:
        paciente = Paciente(paciente_data["id"], paciente_data["nombre"], paciente_data["apellido"],                           paciente_data["dni"], paciente_data["edad"], paciente_data["fecha_registro"],
                            paciente_data["obra_social"])
        lista_pacientes_objetos.append(paciente)
    return lista_pacientes_objetos

#--------------------------------------------------------------------- Punto 1
def mostrar_pacientes(lista_pacientes:list[Paciente])->None:
    '''
    Función:
        Recorre una lista de pacientes y construye una cadena con la información 
        formateada de cada paciente, luego imprime esta cadena.
    Parámetros:
        lista_pacientes (list): Una lista de instancias de la clase Paciente.
    Retorno:
        None: Esta función no devuelve ningún valor.
    '''
    print("PACIENTES\nID | NOMBRE | APELLIDO | DNI | EDAD | FECHA DE REGISTRO | OBRA SOCIAL")
    for paciente in lista_pacientes:            
            print(paciente.mostrar())

def mostrar_el_paciente(paciente:Paciente)->None:
    '''
    Función:
        Construye una cadena con la información detallada de un paciente específico 
        y la imprime.
    Parámetros:
        paciente (Paciente): Una instancia de la clase Paciente.
    Retorno:
        None: Esta función no devuelve ningún valor.
    '''
    print("PACIENTE\nID | NOMBRE | APELLIDO | DNI | EDAD | FECHA DE REGISTRO | OBRA SOCIAL")
    print(paciente.mostrar())

def agregar_paciente(id_autoincremental:int, lista_pacientes:list[Paciente])->bool:
    '''
    Función:
        Agrega un nuevo paciente a la lista de pacientes.
    Parámetros:
        id_autoincremental (int): ID único y autoincremental para el nuevo paciente.
        lista_pacientes (list[Paciente]): Lista actual de pacientes.
    Retorno:
        bool: Retorna True si el paciente fue agregado exitosamente, de lo contrario retorna False.
    '''
    retorno = False
    nombre_paciente = ingresar_nombre_apellido("Ingrese su nombre: ", "ERROR\nReingrese su nombre: ")
    apellido_paciente = ingresar_nombre_apellido("Ingrese su apellido: ", "ERROR\nReingrese su apellido: ")
    dni_paciente = ingresar_dni("Ingrese dni: ", "ERROR", 10000000, 90000000)
    if validar_por_dni(dni_paciente, lista_pacientes):
        print("El paciente ya existe en el sistema.")
        return False
    edad_paciente = ingresar_edad("Ingrese edad: ", "ERROR\nReingrese edad: ", 18, 90)
    fecha_registro = ingresar_fecha_regitro("Ingrese el día de inicio del registro(01 al 31): ", 
    "Ingrese el mes de inicio del registro(01 al 12): ",
    "Ingrese el año de inicio del registro(desde 1930): ",
    "ERROR\nReingrese una fecha válida en el formato DD/MM/AAAA. Inténtelo de nuevo: ")
    obra_social_paciente = ingresar_obra_social(edad_paciente)
    
    nuevo_paciente = Paciente(id_autoincremental, nombre_paciente, apellido_paciente, dni_paciente, edad_paciente, fecha_registro, obra_social_paciente)
    mostrar_el_paciente(nuevo_paciente)
    if(confirmacion_proyecto("Desea confirma el alta (S/N): ", "ERROR\nReingrese si desea el alta (S/N): ")):
        lista_pacientes.append(nuevo_paciente)
        retorno = True
    return retorno

#--------------------------------------------------------------------- Punto 2
def mostrar_turnos(lista_turno:list[Turno])->None:
    '''
    Función:
        Muestra la lista de turnos con sus detalles.
    Parámetros:
        lista_turno (list[Turno]): Lista de turnos a mostrar.
    Retorno:
        None
    '''
    print("TURNOS\nID | ID PACIENTE | ESPECIALIDAD | OBRA SOCIAL | MONTO A PAGAR | ESTADO")
    for turno in lista_turno:            
            print(turno.mostrar())

def mostrar_el_turno(turno:Paciente)->None:
    '''
    Función:
        Construye una cadena con la información detallada de un paciente específico 
        y la imprime.
    Parámetros:
        turno (Paciente): Una instancia de la clase Paciente.
    Retorno:
        None: Esta función no devuelve ningún valor.
    '''
    print("TURNOS\nID | ID PACIENTE | ESPECIALIDAD | OBRA SOCIAL | MONTO A PAGAR | ESTADO")
    print(turno.mostrar())

def encontrar_paciente(lista_pacientes: list[Paciente], id_paciente: int) -> Paciente:
    '''
    Función:
        Encuentra un paciente en la lista por su ID.
    Parámetros:
        lista_pacientes (list[Paciente]): Lista de pacientes.
        id_paciente (int): ID del paciente a encontrar.
    Retorno:
        Paciente: El paciente encontrado, o None si no se encuentra.
    '''
    for paciente in lista_pacientes:
        if paciente.get_id == id_paciente:
            return paciente
    return None

def construir_especialidades_dict(lista_especialidades: list) -> dict:
    '''
    Función:
        Construye un diccionario con las especialidades y sus precios a partir de una lista de diccionarios.
    Parámetros:
        lista_especialidades (list): Lista de diccionarios donde cada diccionario contiene una especialidad y su precio.
    Retorno:
        dict: Diccionario con las especialidades como claves y sus precios como valores.
    '''
    especialidades_dict = {}
    for especialidad_dict in lista_especialidades:
        for especialidad, precio in especialidad_dict.items():
            especialidades_dict[especialidad] = precio
    return especialidades_dict

def seleccionar_especialidad(especialidades_dict: dict) -> str:
    '''
    Función:
        Permite al usuario seleccionar una especialidad de un diccionario de especialidades.
    Parámetros:
        especialidades_dict (dict): Diccionario que contiene las especialidades como claves y sus precios como valores.
    Retorno:
        str: Nombre de la especialidad seleccionada.
    '''
    contador = 0
    for especialidad, valor in especialidades_dict.items():
        contador += 1
        print(f"{contador}. {especialidad.capitalize()} - Precio: ${valor}")
    opcion = int(input("Ingrese la opcion de la especialidad del turno: "))
    while opcion < 1 or opcion > contador:
        opcion = int(input("ERROR\nIngrese la opcion de la especialidad del turno: "))
    especialidades = list(especialidades_dict.keys())
    return especialidades[opcion - 1]

def calcular_monto_a_pagar(paciente, especialidad, especialidades_dict, lista_obras_sociales) -> float:
    '''
    Función:
        Calcula el monto a pagar por un paciente según su obra social, edad y la especialidad elegida.
    Parámetros:
        paciente (Paciente): Objeto Paciente con la información del paciente.
        especialidad (str): Nombre de la especialidad seleccionada.
        especialidades_dict (dict): Diccionario que contiene las especialidades como claves y sus precios como valores.
        lista_obras_sociales (dict): Diccionario que contiene información de las obras sociales, como descuentos y recargos.
    Retorno:
        float: Monto total a pagar por el paciente por el turno, considerando descuentos y recargos según la obra social y edad.
    '''
    obra_social = paciente.get_obra_social
    edad_paciente = paciente.get_edad
    obra_social_info = lista_obras_sociales.get(obra_social, {})
    descuento = obra_social_info.get("descuento", 0.0) #por defecto 0.0
    extra = obra_social_info.get("extra", 0.0) #por defecto 0.0
    if obra_social == "Swiss medical":
        if 18 <= edad_paciente <= 60:
            descuento += 0.1  # Descuento del 10%
    elif obra_social == "Apres":
        if 26 <= edad_paciente <= 59:
            descuento += 0.03  # Descuento del 3%
    elif obra_social == "PAMI":
        if edad_paciente >= 80:
            descuento += 0.03  # Descuento del 3%
    elif obra_social == "Particular":
        if 40 <= edad_paciente <= 60:
            extra += 0.15  # Recargo del 15%
    
    precios_especialidad = especialidades_dict.get(especialidad, 0)
    monto_base = precios_especialidad
    monto_a_pagar = monto_base * (1 - descuento) + monto_base * extra
    
    return monto_a_pagar

def alta_turno(lista_turnos: list[Turno], lista_pacientes: list[Paciente], lista_especialidades: list, lista_obras_sociales: list, lista_pacientes_con_turno:list) -> bool:
    '''
    Función:
        Gestiona el alta de un turno para un paciente, seleccionando especialidad y calculando el monto a pagar.
    Parámetros:
        lista_turnos (list[Turno]): Lista de objetos Turno donde se agregarán los nuevos turnos.
        lista_pacientes (list[Paciente]): Lista de objetos Paciente donde se buscará y eliminará el paciente para asignarle turno.
        lista_especialidades (list): Lista de diccionarios con las especialidades y sus precios.
        lista_obras_sociales (list): Lista de diccionarios con información de las obras sociales y sus descuentos/recargos.
        lista_pacientes_con_turno (list): Lista donde se agregarán los pacientes que tienen turnos activos.
    Retorno:
        bool: True si se pudo dar de alta el turno correctamente, False en caso contrario.
    '''
    mostrar_pacientes(lista_pacientes)
    id_paciente = int(input("Ingrese el ID del paciente para el turno: "))
    paciente_encontrado = encontrar_paciente(lista_pacientes, id_paciente)
    
    if not paciente_encontrado:
        print("No se encontró ningún paciente con el ID ingresado!")
        return False
    else:
        especialidades_dict = construir_especialidades_dict(lista_especialidades)
        especialidad = seleccionar_especialidad(especialidades_dict)
        obra_social_paciente = paciente_encontrado.get_obra_social
        monto_a_pagar = calcular_monto_a_pagar(paciente_encontrado, especialidad, especialidades_dict, lista_obras_sociales)
        
        nuevo_turno = Turno(id_paciente, especialidad, obra_social_paciente, monto_a_pagar, "Activo")
        lista_turnos.append(nuevo_turno)
        lista_pacientes.remove(paciente_encontrado)
        lista_pacientes_con_turno.append(paciente_encontrado)
        return True

#--------------------------------------------------------------------- Punto 3
def ordenar_por_obra(lista_turnos: list)->None:
    '''
    Función:
        Ordena una lista de turnos según la obra social del paciente.
    Parámetros:
        lista_turnos (list): Lista de objetos Turno que se va a ordenar.
    Retorno:
        None
    '''
    lista_turnos.sort(key=lambda turno: turno.get_obra_social)

def ordenar_por_monto(lista_turnos: list)->None:
    '''
    Función:
        Ordena una lista de turnos según el monto a pagar de forma descendente.
    Parámetros:
        lista_turnos (list): Lista de objetos Turno que se va a ordenar.
    Retorno:
        None
    '''
    lista_turnos.sort(key=lambda turno: turno.get_monto_a_pagar, reverse=True)

def verificar_orden() -> str:
    '''
    Función:
        Verifica y devuelve la opción seleccionada para ordenar la lista de turnos.
    Parámetros:
        Ninguno
    Retorno:
        str: Opción seleccionada para ordenar ("a" para obra social ascendente, "b" para monto descendente).
    '''
    opcion = input("A. Obra Social - ASC\nB. MONTO - DES\nIngrese opcion para ordenar: ").lower()
    while opcion not in ["a", "b"]:
        opcion = input("ERROR\nA. Obra Social - ASC\nB. MONTO - DES\nReingrese opcion para ordenar: ").lower()
    return opcion

def ordenar_turnos(lista_turnos: list)->None:
    '''
    Función:
        Ordena la lista de turnos según la opción seleccionada por el usuario (obra social ascendente o monto descendente).
    Parámetros:
        lista_turnos (list): Lista de objetos Turno a ordenar.
    Retorno:
        None
    '''
    opcion = verificar_orden()
    if opcion == "a":
        ordenar_por_obra(lista_turnos)
        mostrar_turnos(lista_turnos)
    elif opcion == "b":
        ordenar_por_monto(lista_turnos)
        mostrar_turnos(lista_turnos)
    print("Turnos ordenados correctamente.")

#--------------------------------------------------------------------- Punto 4
def mostrar_turnos_activos(lista_turnos:list[Turno])->None:
    '''
    Función:
        Muestra los turnos activos de la lista de turnos.
    Parámetros:
        lista_turnos (list[Turno]): Lista de objetos Turno.
    Retorno:
        None
    '''
    turnos_activos = list(filter(lambda turno: turno.get_estado_turno == "Activo", lista_turnos))
    if not turnos_activos:
        print("No se encontraron Turnos Activos!!")
    else:
        print("TURNOS\nID | ID PACIENTE | ESPECIALIDAD | OBRA SOCIAL | MONTO A PAGAR | ESTADO")
        for turno in turnos_activos:
            print(turno.mostrar())

#--------------------------------------------------------------------- Punto 5
def atender_pacientes_con_turno(lista_turnos:list[Turno])->bool:
    '''
    Función:
        Simula la atención de los pacientes con turno marcando sus turnos como finalizados.
    Parámetros:
        lista_turnos (list[Turno]): Lista de objetos Turno.
    Retorno:
        bool: True si se atendieron pacientes correctamente, False si no hay turnos activos.
    '''
    turnos_activos = list(filter(lambda turno: turno.get_estado_turno == "Activo", lista_turnos))
    if not turnos_activos:
        return False
    else:
        turnos_final = turnos_activos[:2]  # Selecciona los primeros dos turnos activos
        for turno in turnos_final:
            turno.set_estado_turno = "Finalizado"
        print(f"Se han atendido {len(turnos_final)} pacientes.")
        return True

def mostrar_turnos_finalizados(lista_turno:list[Turno])->None:
    '''
    Función:
        Muestra los turnos que están marcados como finalizados.
    Parámetros:
        lista_turno (list[Turno]): Lista de objetos Turno.
    Retorno:
        None
    '''
    turnos_finalizados = list(filter(lambda turno: turno.get_estado_turno == "Finalizado", lista_turno))
    print("TURNOS\nID | ID PACIENTE | ESPECIALIDAD | OBRA SOCIAL | MONTO A PAGAR | ESTADO")
    for turno in turnos_finalizados:
        print(turno.mostrar())

#--------------------------------------------------------------------- Punto 6
def cobrar_atenciones(lista_turnos: list[Turno])->None:
    '''
    Función:
        Realiza el cobro de las atenciones para los turnos finalizados.
    Parámetros:
        lista_turnos (list[Turno]): Lista de objetos Turno.
    Retorno:
        None
    '''
    turnos_finalizados = list(filter(lambda turno: turno.get_estado_turno == "Finalizado", lista_turnos))
    if not turnos_finalizados:
        print("No se encontraron turnos finalizados para cobrar")
    else:
        for turno in turnos_finalizados:
            turno.set_estado_turno = "Pagado"
        print("Cobro realizado y estado del turno cambiado a Pagado")

#--------------------------------------------------------------------- Punto 7
def verificar_pacientes_por_atender(lista_turnos: list[Turno]) -> bool:
    '''
    Función:
        Verifica si hay pacientes por atender en la lista de turnos.
    Parámetros:
        lista_turnos (list[Turno]): Lista de objetos Turno.
    Retorno:
        bool: True si hay pacientes por atender (turnos activos o finalizados), False si no hay.
    '''
    for turno in lista_turnos:
        if turno.get_estado_turno == "Activo" or turno.get_estado_turno == "Finalizado":
            return True
    return False

def cerrar_caja(lista_turnos: list[Turno], lista_pacientes: list[Paciente], lista_pacientes_con_turno:list)->None:
    '''
    Función:
        Cierra la caja del consultorio verificando si hay pacientes por atender y mostrando el total recaudado.
    Parámetros:
        lista_turnos (list[Turno]): Lista de objetos Turno.
        lista_pacientes (list[Paciente]): Lista de objetos Paciente.
        lista_pacientes_con_turno (list): Lista de pacientes con turno.
    Retorno:
        None
    '''
    if verificar_pacientes_por_atender(lista_turnos):
        print("Hay pacientes por atender!!")
    else:
        suma = 0
        turnos_pagados = list(filter(lambda turno: turno.get_estado_turno == "Pagado", lista_turnos))
        for turno_pago in turnos_pagados:
            suma += turno_pago.get_monto_a_pagar
        print(f"Total recaudado: ${suma}")
        print("Caja cerrada!!")
        guardar_turnos_json(lista_turnos)
        guardar_pacientes_json(lista_pacientes_con_turno)

#--------------------------------------------------------------------- Punto 8
'''3. Informar con qué obra social se obtuvo más ingresos'''
def informar_obras_sociales_ingresos(lista_turnos: list[Turno]):
    '''
    Función:
        Informa sobre los ingresos generados por obra social, mostrando cuál tiene mayores ingresos.
    Parámetros:
        lista_turnos (list[Turno]): Lista de objetos Turno.
    Retorno:
        None
    '''
    turnos_pagados = list(filter(lambda turno: turno.get_estado_turno == "Pagado", lista_turnos))
    ingresos_por_obras_sociales = {}
    obra_social_mas_ingresos = None
    max_ingresos = 0
    for turno in turnos_pagados:
        obra_social = turno.get_obra_social
        monto_a_pagar = turno.get_monto_a_pagar
        if obra_social in ingresos_por_obras_sociales:
            ingresos_por_obras_sociales[obra_social] += monto_a_pagar
        else:
            ingresos_por_obras_sociales[obra_social] = monto_a_pagar
    
    for obra_social, ingresos in ingresos_por_obras_sociales.items():
        if ingresos > max_ingresos:
            max_ingresos = ingresos
            obra_social_mas_ingresos = obra_social

    if obra_social_mas_ingresos:
        print(f"La obra social con mayores ingresos es '{obra_social_mas_ingresos}' con un total de ${ingresos_por_obras_sociales[obra_social_mas_ingresos]:.2f}")
    else:
        print("No se encontraron ingresos registrados para ninguna obra social.")