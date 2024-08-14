import json
#--------------------------------------------------------------------- Lectura
def leer_csv(path:str)->list:
    '''
    Función:
        Esta función lee un archivo CSV desde la ruta especificada y 
        convierte cada fila en un diccionario.
        Cada diccionario representa una fila en el archivo CSV, donde las claves 
        son los encabezados de columna y los valores son los datos correspondientes de esa fila.
    Parámetros:
        path (str): La ruta del archivo CSV que se va a leer.
    Retorno:
        list: Una lista de diccionarios, donde cada diccionario representa una fila del archivo CSV.
    '''
    lista_de_diccionarios = []
    with open(path, mode = "r", encoding = 'utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(",")
        for linea in lineas[1:]:
            valores = linea.strip().split(",")
            diccionario = {}
            for i in range(len(encabezados)):
                diccionario[encabezados[i]] = valores[i]
            lista_de_diccionarios.append(diccionario)
    return lista_de_diccionarios

#--------------------------------------------------------------------- Escritura
def escribir_csv(path:str, lista_proyectos:list)->None:
    '''
    Función:
        Esta función toma una lista de diccionarios, donde cada diccionario 
        representa una fila de datos,y escribe estos datos en un 
        archivo CSV en la ruta especificada.
    Parámetros:
        path (str): La ruta del archivo CSV que se va a escribir.
        lista_proyectos (list): Una lista de diccionarios, donde cada 
        diccionario representa una fila de datos.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    with open(path, mode = "w", encoding = 'utf-8') as archivo:
        encabezados = lista_proyectos[0].keys()
        archivo.write(','.join(encabezados) + '\n')
        for proyecto in lista_proyectos:
            datos_proyecto = []
            for encabezado in encabezados:
                datos_proyecto.append(str(proyecto[encabezado]))
            archivo.write(','.join(datos_proyecto) + '\n')

def escribir_json_finalizados(path:str, lista_proyectos:list):
    '''
    Función:
        Esta función toma una lista de proyectos finalizados 
        representados como diccionarios y los escribe en un 
        archivo JSON en la ruta especificada.
    Parámetros:
        path (str): La ruta del archivo JSON que se va a escribir.
        lista_proyectos (list): Una lista de diccionarios que representan los proyectos finalizados.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    with open(path, mode = "w", encoding='utf-8') as archivo:
        json.dump(lista_proyectos, archivo, indent = 4, ensure_ascii = False)