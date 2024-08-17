from paciente import Paciente

def ingresar_nombre_apellido(mensaje:str, mensaje_error:str)->str:
    '''
    Función:
        Muestra un mensaje solicitando al usuario que ingrese un nombre/apellido.
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

def ingresar_dni(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->int:
    '''
    Función:
        Muestra un mensaje solicitando al usuario que ingrese dni.
        Valida que el dni ingresado cumpla con las siguientes condiciones:
        - Debe ser un número entero.
        - Debe estar dentro del rango especificado.
        Si el dni ingresado no cumple con las condiciones, se muestra un mensaje 
        de error y se solicita nuevamente el ingreso del dni.
    Parámetros:
        mensaje (str): El mensaje que se muestra al usuario para solicitar el 
        ingreso del dni.
        mensaje_error (str): El mensaje que se muestra al usuario en caso de 
        que el dni ingresado no sea válido.
        minimo (int): El valor mínimo aceptable para el dni.
        maximo (int): El valor máximo aceptable para el dni.
    Retorno:
        int: El dni ingresado por el usuario que cumple 
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

def ingresar_edad(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->int:
    '''
    Función:
        Muestra un mensaje solicitando al usuario que ingrese una edad.
        Valida que edad ingresado cumpla con las siguientes condiciones:
        - Debe ser un número entero.
        - Debe estar dentro del rango especificado.
        Si el edad ingresado no cumple con las condiciones, se muestra un mensaje 
        de error y se solicita nuevamente el ingreso del edad.
    Parámetros:
        mensaje (str): El mensaje que se muestra al usuario para solicitar el 
        ingreso del edad.
        mensaje_error (str): El mensaje que se muestra al usuario en caso de 
        que el edad ingresado no sea válido.
        minimo (int): El valor mínimo aceptable para el edad.
        maximo (int): El valor máximo aceptable para el edad.
    Retorno:
        int: El edad ingresado por el usuario que cumple 
        con las condiciones de validación.
    '''
    confirmar_dato = True
    while confirmar_dato:
        dato = input(mensaje)
        if dato.isdigit():
            dato = int(dato)
            if dato >= minimo and dato <= maximo:
                confirmar_dato = False
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)
    return dato

def ingresar_fecha_regitro(mensaje_dia:str, mensaje_mes:str, mensaje_año:str, mensaje_error:str)->str:
    '''
    Función:
        Muestra mensajes solicitando al usuario que ingrese el día, mes y año de una fecha de registro.
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
        str: La fecha de registro ingresada por el usuario en el formato "DD-MM-AAAA".
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
            if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and año >= 1930:
                confirmar_dato = False
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)
    fecha_finalizada = f"{dia}-{mes}-{año}"
    return fecha_finalizada

def ingresar_obra_social(edad:str)->str:
    '''
    Función:
        Solicita al usuario seleccionar una obra social de una lista de opciones.
        Si la edad del paciente es mayor o igual a 60, solo puede elegir "PAMI".
        Valida que la selección del usuario sea una opción válida.
    Parámetros:
        edad (int): La edad del paciente.
    Retorno:
        str: La obra social seleccionada por el usuario.
    '''
    opciones = {1: "Swiss medical", 2: "Apres", 3: "PAMI", 4: "Particular"}
    if edad >= 60:
        print("Solamente puede utilizar PAMI (mayor o igual a 60)!!")
        return "PAMI"
    while True:
        obra_social = input("Obra social:\n1. Swiss medical\n2. Apres\n4. Particular\nElegir: ")
        if obra_social.isdigit():
            obra_social = int(obra_social)
            if obra_social in opciones:
                return opciones[obra_social]
        print("ERROR")

def validar_por_dni(dni_ingresado:int, lista_pacientes:list[Paciente])->bool:
    '''
    Función:
        Valida si un DNI ingresado corresponde a algún paciente en la lista de pacientes.
    Parámetros:
        dni_ingresado (int): El DNI que se desea validar.
        lista_pacientes (list[Paciente]): Lista de objetos de tipo Paciente.
    Retorno:
        bool: Retorna True si el DNI ingresado se encuentra en la lista de pacientes, de lo contrario retorna False.
    '''
    retorno = False
    for paciente in lista_pacientes:
        if(int(paciente.get_dni) == int(dni_ingresado)):
            retorno = True
            break
    return retorno

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