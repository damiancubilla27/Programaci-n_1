import json

def leer_json_pacientes()->list:
    '''
    Función:
        Lee un archivo JSON que contiene datos de pacientes y devuelve una lista con esta información.
    Parámetros:
        None
    Retorno:
        list: Lista de diccionarios con la información de los pacientes.
    '''
    path = "C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_16_Segundo parcial\\pacientes.json"
    with open(path, 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)
        pacientes_json = data["pacientes"]
    return pacientes_json

def leer_json_especialidades() -> list:
    '''
    Función:
        Lee un archivo JSON que contiene datos de especialidades médicas y devuelve una lista con esta información.
    Parámetros:
        None
    Retorno:
        list: Lista de diccionarios con la información de las especialidades médicas.
    '''
    path = "C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_16_Segundo parcial\\configs.json"
    with open(path, 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)
        especialidades_json = data.get("especialidades", [])
    
    lista_especialidades = []
    for especialidad in especialidades_json:
        lista_especialidades.append(especialidad)
    
    return lista_especialidades

def leer_json_obras_sociales() -> dict:
    '''
    Función:
        Lee un archivo JSON que contiene datos de obras sociales y devuelve un diccionario con esta información.
    Parámetros:
        None
    Retorno:
        dict: Diccionario con la información de las obras sociales.
    '''
    path = "C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_16_Segundo parcial\\configs.json"
    with open(path, 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)
        obras_sociales_json = data.get("obras sociales", [])
    
    obras_sociales_dict = {}
    for obra_social in obras_sociales_json:
        for key, value in obra_social.items():
            obras_sociales_dict[key] = value
    return obras_sociales_dict

#--------------------------------------------------------------------------> Escribir
def objeto_turno_a_dicc(turno):
    '''
    Función:
        Convierte un objeto Turno en un diccionario con sus atributos relevantes.
    Parámetros:
        turno (Turno): Objeto de la clase Turno que se desea convertir a diccionario.
    Retorno:
        dict: Diccionario con los atributos del objeto Turno.
    '''
    return {
        "id": turno.get_id,
        "id_paciente": turno.get_id_paciente,
        "especialidad": turno.get_especialidad,
        "monto_a_pagar": turno.get_monto_a_pagar,
        "estado_turno": turno.get_estado_turno
    }

def guardar_turnos_json(lista_turnos: list):
    '''
    Función:
        Guarda una lista de turnos en un archivo JSON.
    Parámetros:
        lista_turnos (list): Lista de objetos Turno a guardar en el archivo JSON.
    Retorno:
        None
    '''
    path = "C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_16_Segundo parcial\\turnos_medicos.json"
    turnos_dict = []
    for turno in lista_turnos:
        turnos_dict.append(objeto_turno_a_dicc(turno))

    with open(path, 'w', encoding='utf-8') as archivo:
        json.dump(turnos_dict, archivo, ensure_ascii=False, indent=4)

def objeto_paciente_a_dicc(paciente):
    '''
    Función:
        Convierte un objeto Paciente en un diccionario con sus atributos relevantes.
    Parámetros:
        paciente (Paciente): Objeto Paciente a convertir.
    Retorno:
        dict: Diccionario con los atributos del paciente.
    '''
    paciente_dict = {
        "id": paciente.get_id,
        "nombre": paciente.get_nombre,
        "apellido": paciente.get_apellido,
        "dni": paciente.get_dni,
        "edad": paciente.get_edad,
        "fecha_registro": paciente.get_fecha_registro,
        "obra_social": paciente.get_obra_social,
    }
    return paciente_dict

def guardar_pacientes_json(lista_pacientes: list):
    '''
    Función:
        Guarda una lista de objetos Paciente en un archivo JSON.
    Parámetros:
        lista_pacientes (list): Lista de objetos Paciente a guardar.
    Retorno:
        None
    '''
    path = "C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_16_Segundo parcial\\lista_pacientes_con_turnos.json"
    pacientes_dict = []
    for paciente in lista_pacientes:
        pacientes_dict.append(objeto_paciente_a_dicc(paciente))
    with open(path, 'w', encoding='utf-8') as archivo:
        json.dump(pacientes_dict, archivo, ensure_ascii=False, indent=4)