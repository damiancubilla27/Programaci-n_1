ACTIVO = True
INACTIVO = False

BAJA_CORRECTA = 1
BAJA_CANCELADA = 2
BAJA_ERRONEA = 3

MODIFICACION_CORRECTA = 1
MODIFICACION_CANCELADA = 2
MODIFICACION_ERRONEA = 3

def mostrar_alumnos(lista_alumnos:list):
    informacion = "ALUMNOS\nID | NOMBRE | APELLIDO | GENERO | NOTA FINAL |\n"
    for alumno in lista_alumnos:
        for clave in alumno:
            if alumno["estado"] == ACTIVO:             
                if clave != "estado":
                    informacion += str(alumno[clave]) + " | "
        informacion +="\n"
    print(informacion)

def mostrar_alumno(alumno:dict):
    informacion = "ALUMNOS\nID | NOMBRE | APELLIDO | GENERO | NOTA FINAL |\n"
    for clave in alumno:            
        if clave != "estado":
            informacion += str(alumno[clave]) + " | "
            
    print(informacion)

# ---------------------------------------------------------------------- ALTA
def ingresar_string(mensaje:str, mensaje_error:str)->str:
    dato = input(mensaje)
    while len(dato) == 0:
        dato = input(mensaje_error)
    return dato

def ingresar_genero(mensaje:str, mensaje_error:str)->str:
    dato = input(mensaje)
    dato = dato.upper()
    while dato != 'M' and dato != 'F' and dato != 'NB':
        dato = input(mensaje_error)
        dato = dato.upper()
    return dato

def ingresar_entero(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->int:
    dato = int(input(mensaje))
    while dato < minimo or dato > maximo:
        dato = int(input(mensaje_error))
    return dato

def confirmacion_alumno(mensaje:str, mensaje_error:str)->bool:
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

def agregar_alumno(id_autoincremental:int, lista_alumnos:list)->bool:
    retorno = False
    nombre_alumno = ingresar_string("Ingrese su nombre: ", "ERROR\nReingrese su nombre: ")
    apellido_alumno = ingresar_string("Ingrese su apellido: ", "ERROR\nReingrese su apellido: ")
    genero_alumno = ingresar_genero("Ingrese su genero (M,F,NB): ", "ERROR\nReingrese su genero (M,F,NB): ")
    nota_final_alumno = ingresar_entero("Ingrese su nota final (1-10): ", "ERROR\nReingrese su nota final (1-10): ", 1, 10)
    alumno = {"id":id_autoincremental, "nombre":nombre_alumno, "apellido":apellido_alumno, "genero":genero_alumno, "nota final":nota_final_alumno, "estado":ACTIVO}
    mostrar_alumno(alumno)
    if(confirmacion_alumno("Desea confirma el alta (S/N): ", "ERROR\nReingrese si desea el alta (S/N): ")):
        lista_alumnos.append(alumno)
        retorno = True
    return retorno

# ---------------------------------------------------------------------- BAJA
def buscar_alumno(lista_alumnos:list, id_a_buscar:int)->int:
    indice_alumno = None
    for i in range(len(lista_alumnos)):
        if(lista_alumnos[i]["id"] == id_a_buscar):
            indice_alumno = i
            break
    return indice_alumno

def dar_de_baja_alumno(lista_alumnos:list):
    retorno = BAJA_ERRONEA
    mostrar_alumnos(lista_alumnos)
    id_a_borrar = int(input("Ingrese el id a dar de baja: "))
    indice = buscar_alumno(lista_alumnos, id_a_borrar)
    if(indice != None):
        mostrar_alumno(lista_alumnos[indice])
        confirmacion = confirmacion_alumno("Desea confirma la baja (S/N): ", "ERROR\nReingrese si desea la baja (S/N): ")
        if(confirmacion):
            lista_alumnos[indice]["estado"] = INACTIVO
            retorno = BAJA_CORRECTA
        else:
            retorno = BAJA_CANCELADA
    return retorno

def contar_alumnos(lista_alumnos:list)->int:
    contador = 0
    for elemento in lista_alumnos:
        if(elemento["estado"] == ACTIVO):
            contador += 1
    return contador

# ---------------------------------------------------------------------- MODIFICAR
def pedir_clave()->int:
    retorno = int(input("Que desea modificar:\n1.nombre\n2.apellido\n3.genero\n4.nota final\nIngrese Opcion: "))
    while retorno < 1 or retorno > 4:
        retorno = int(input("Que desea modificar:\n1.nombre\n2.apellido\n3.genero\n4.nota final\nIngrese Opcion: "))
    return retorno

def pedir_valor()->str:
    retorno = input("Ingrese el nuevo valor: ")
    return retorno

def modificar_alumno(lista_alumnos:list):
    retorno = MODIFICACION_ERRONEA
    mostrar_alumnos(lista_alumnos)
    id_a_moficar = int(input("Ingrese el id del alumno a modificar: "))
    indice = buscar_alumno(lista_alumnos, id_a_moficar)
    if(indice != None):
        mostrar_alumno(lista_alumnos[indice])
        confirmacion = confirmacion_alumno("Desea confirma la modificacion (S/N): ", "ERROR\nReingrese si desea la modificacion (S/N): ")
        if(confirmacion):
            ingreso_clave = pedir_clave()
            ingreso_valor = pedir_valor()
            if(ingreso_clave == 1):
                lista_alumnos[indice].update({"nombre":ingreso_valor})
            elif(ingreso_clave == 2):
                lista_alumnos[indice].update({"apellido":ingreso_valor})
            elif(ingreso_clave == 3):
                lista_alumnos[indice].update({"genero":ingreso_valor})
            else:
                lista_alumnos[indice].update({"nota final":int(ingreso_valor)})
            retorno = MODIFICACION_CORRECTA
        else:
            retorno = MODIFICACION_CANCELADA
    return retorno
