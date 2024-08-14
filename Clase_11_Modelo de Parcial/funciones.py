ACTIVO = True
INACTIVO = False
BAJA_CORRECTA = 1
BAJA_CANCELADA = 2
BAJA_ERRONEA = 3
MODIFICACION_CORRECTA = 1
MODIFICACION_CANCELADA = 2
MODIFICACION_ERRONEA = 3


def mostrar_empleados(lista_empleado:list):
    informacion = "EMPLEADOS\nID | NOMBRE | APELLIDO | DNI | PUESTO | SALARIO\n"
    for empleado in lista_empleado:
        for clave in empleado:
            if empleado["estado"] == ACTIVO:             
                if clave != "estado":
                    informacion += str(empleado[clave]) + " | "
        informacion +="\n"
    print(informacion)

def mostrar_el_empleado(empleado:dict):
    informacion = "EMPLEADOS\nID | NOMBRE | APELLIDO | DNI | PUESTO | SALARIO\n"
    for clave in empleado:            
        if clave != "estado":
            informacion += str(empleado[clave]) + " | "
    print(informacion)

#----------------------------------------------------------------- Punto 1
def ingresar_string(mensaje:str, mensaje_error:str)->str:
    dato = input(mensaje)
    confirmar_dato = None
    if(len(dato) < 20 and len(dato) > 0 and dato.isalpha()):
        confirmar_dato = False
    else:
        confirmar_dato = True
    while confirmar_dato:
        dato = input(mensaje_error)
        if(len(dato) < 20 and len(dato) > 0 and dato.isalpha()):
            confirmar_dato = False
        else:
            confirmar_dato = True
    return dato

def ingresar_entero(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->int:
    dato = int(input(mensaje))
    while dato < minimo or dato > maximo:
        dato = int(input(mensaje_error))
    return dato

def ingresar_puesto(mensaje:str, mensaje_error:str)->str:
    dato = input(mensaje)
    dato = dato.capitalize()
    while dato != 'Gerente' and dato != 'Supervisor' and dato != 'Analista' and dato != 'Encargado' and dato != 'Asistente':
        dato = input(mensaje_error)
        dato = dato.capitalize()
    return dato

def confirmacion_empleado(mensaje:str, mensaje_error:str)->bool:
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

def agregar_empleado(id_autoincremental:int, lista_empleados:list)->bool:
    retorno = False
    nombre_empleados = ingresar_string("Ingrese su nombre: ", "ERROR\nReingrese su nombre: ")
    apellido_empleado = ingresar_string("Ingrese su apellido: ", "ERROR\nReingrese su apellido: ")
    dni_empleado = ingresar_entero("Ingrese su dni: ", "Error\nReingrese su dni: ", 5000000, 99999999)
    puesto_empleado = ingresar_puesto("Ingrese su puesto(Gerente|Supervisor|Analista|Encargado|Asistente): ", "ERROR\nReingrese su puesto(Gerente|Supervisor|Analista|Encargado|Asistente): ")
    salario_empleado = ingresar_entero("Ingrese su salario: ", "Error\nReingrese su salario: ", 234315, 10000000)
    empleado = {"id":id_autoincremental, "nombre":nombre_empleados, "apellido":apellido_empleado, "dni": dni_empleado, "puesto":puesto_empleado, "salario": salario_empleado, "estado":ACTIVO}
    mostrar_el_empleado(empleado)
    if(confirmacion_empleado("Desea confirma el alta (S/N): ", "ERROR\nReingrese si desea el alta (S/N): ")):
        lista_empleados.append(empleado)
        retorno = True
    return retorno

#----------------------------------------------------------------- Punto 2
def pedir_clave()->int:
    retorno = int(input("Que desea modificar:\n1.nombre\n2.apellido\n3.DNI\n4.Puesto\n5.Salario\nIngrese Opcion: "))
    while retorno < 1 or retorno >= 5:
        retorno = int(input("Que desea modificar:\n1.nombre\n2.apellido\n3.DNI\n4.Puesto\n5.Salario\nIngrese Opcion: "))
    return retorno

def pedir_valor()->str:
    retorno = input("Ingrese el nuevo valor: ")
    return retorno

def modificar_alumno(lista_empleado:list):
    retorno = MODIFICACION_ERRONEA
    mostrar_empleados(lista_empleado)
    id_a_moficar = int(input("Ingrese el id del empleado a modificar: "))
    indice = buscar_empleado(lista_empleado, id_a_moficar)
    if(indice != None):
        mostrar_el_empleado(lista_empleado[indice])
        confirmacion = confirmacion_empleado("Desea confirma la modificacion (S/N): ", "ERROR\nReingrese si desea la modificacion (S/N): ")
        if(confirmacion):
            ingreso_clave = pedir_clave()
            ingreso_valor = pedir_valor()
            if(ingreso_clave == 1):
                lista_empleado[indice].update({"nombre":ingreso_valor})
            elif(ingreso_clave == 2):
                lista_empleado[indice].update({"apellido":ingreso_valor})
            elif(ingreso_clave == 3):
                lista_empleado[indice].update({"DNI":ingreso_valor})
            elif(ingreso_clave == 4):
                lista_empleado[indice].update({"puesto":int(ingreso_valor)})
            else:
                lista_empleado[indice].update({"salario":int(ingreso_valor)})
            retorno = MODIFICACION_CORRECTA
        else:
            retorno = MODIFICACION_CANCELADA
    return retorno

#----------------------------------------------------------------- Punto 3
def buscar_empleado(lista_empleados:list, id_a_buscar:int)->int:
    indice_alumno = None
    for i in range(len(lista_empleados)):
        if(lista_empleados[i]["id"] == id_a_buscar):
            indice_alumno = i
            break
    return indice_alumno

def bajar_empleado(lista_empleados:list):
    retorno = BAJA_ERRONEA
    mostrar_empleados(lista_empleados)
    id_a_borrar = int(input("Ingrese el id a dar de baja: "))
    indice = buscar_empleado(lista_empleados, id_a_borrar)
    if(indice != None):
        mostrar_el_empleado(lista_empleados[indice])
        confirmacion = confirmacion_empleado("Desea confirma la baja (S/N): ", "ERROR\nReingrese si desea la baja (S/N): ")
        if(confirmacion):
            lista_empleados[indice]["estado"] = INACTIVO
            retorno = BAJA_CORRECTA
        else:
            retorno = BAJA_CANCELADA
    return retorno

def contar_empleados(lista_empleados:list)->int:
    contador = 0
    for elemento in lista_empleados:
        if(elemento["estado"] == ACTIVO):
            contador += 1
    return contador

#----------------------------------------------------------------- Punto 5
def calcular_promedio_salario(lista_empleados:list)->float:
    contador = 0
    suma = 0
    promedio = 0
    for empleado in lista_empleados:
        contador += 1
        suma = empleado["salario"]
    promedio = suma / contador
    return promedio

#----------------------------------------------------------------- Punto 6
def buscar_dni(lista_empleados:list, dni_a_buscar:int)->int:
    indice_alumno = -1
    for i in range(len(lista_empleados)):
        if(lista_empleados[i]["dni"] == dni_a_buscar):
            indice_alumno = i
            break
    return indice_alumno

def mostra_por_dni(lista_empleados:list)->None:
    dni_ingresado = int(input("Ingrese DNI a buscar: "))
    numero = buscar_dni(lista_empleados, dni_ingresado)
    if(numero != -1):
        mostrar_el_empleado(lista_empleados[numero])
    else:
        print("Error, no se encontro el empleado")

#----------------------------------------------------------------- Punto 7
def ordenar_por_valor(lista_empleados:list, key:str, orden:bool)->list:
    flag_swap = True
    rango_lista = len(lista_empleados)
    while(flag_swap):
        flag_swap = False
        rango_lista = rango_lista-1
        for empleado in range(rango_lista):
            if((orden == True and lista_empleados[empleado][key] > lista_empleados[empleado+1][key]) or (orden == False and lista_empleados[empleado][key] < lista_empleados[empleado+1][key])):
                aux = lista_empleados[empleado]
                lista_empleados[empleado] = lista_empleados[empleado+1]
                lista_empleados[empleado+1] = aux
                flag_swap = True
    return lista_empleados

def mostrar_ordenamiento(lista_empleados:list)->None:
    tipo_orden = input("Ingrese qué desea ordenar (nombre, apellido, o salario): ").lower()
    if tipo_orden not in ['nombre', 'apellido', 'salario']:
        print("Error: tipo de ordenamiento no válido.")
    forma_orden = input("Ingrese True para forma Ascendente o False para forma Descendente: ")
    if forma_orden.lower() == 'true':
        forma_orden = True
    elif forma_orden.lower() == 'false':
        forma_orden = False
    else:
        print("Error: forma de ordenamiento no válida.")
    lista_ordenada = ordenar_por_valor(lista_empleados, tipo_orden, forma_orden)
    mostrar_empleados(lista_ordenada)