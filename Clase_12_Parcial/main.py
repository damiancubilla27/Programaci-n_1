from biblioteca import *
from archivos import *
from os import *

lista_proyectos = []
lista_proyectos = leer_csv("C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_12_Parcial\\Proyectos.csv")
lista_proyectos = convertir_id_a_entero(lista_proyectos)
longitud = len(lista_proyectos) - 1
id_auto_incremental = lista_proyectos[longitud]["id"]

def incrementar_id():
    '''
    Función:
        Esta función incrementa en uno el valor de la variable global id_auto_incremental.
    Parámetros:
        No tiene parámetros de entrada.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    global id_auto_incremental
    id_auto_incremental += 1
    
def decrementar_id():
    '''
    Función:
        Esta función decrementa en uno el valor de la variable global id_auto_incremental.
    Parámetros:
        No tiene parámetros de entrada.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    global id_auto_incremental
    id_auto_incremental += -1
    
def imprimir_menu():
    '''
    Función:
        Esta función imprime el menú principal en la consola, con las opciones disponibles.
    Parámetros:
        No tiene parámetros de entrada.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    system('cls') 
    print("MENU PRINCIPAL\n\n1)Ingresar proyecto\n2)Modificar proyecto\n3)Cancelar proyecto\n4)Comprobar proyectos\n5)Mostrar todos\n6)Calcular presupuesto promedio\n7)Buscar proyecto por nombre\n8)Ordenar proyectos\n9)Retomar proyecto\n10)Qatar 2022\n11)Covid 19\n12)Salir")

def menu()->None:
    '''
    Función:
        Esta función muestra un menú con opciones como agregar, modificar, dar de baja, 
        finalizar proyectos, etc.
        El usuario puede seleccionar una opción ingresando un número y realizar 
        acciones en función de esa selección.
    Parámetros:
        No tiene parámetros de entrada.
    Retorno:
        None: Esta funcion no retorna nada.
    '''
    while(True):
        imprimir_menu()
        opcion = int(input("Elija una opción: "))
        system('cls') 
        match opcion:
            case 1:
                if(contador_de_proyectos_activos(lista_proyectos) <= 50):
                    incrementar_id()
                    if(agregar_proyecto(id_auto_incremental, lista_proyectos)):
                        print("Proyecto dado de alta correctamente!")
                    else:
                        print("Operacion cancelada!!")
                        decrementar_id()
                else:
                    print("No se puede agregar mas activos al sistema")
            case 2:
                    retorno_modi = modificar_proyecto(lista_proyectos)
                    if(retorno_modi == MODIFICACION_CORRECTA):
                        print("Se realizo la modificacion correctamente!")
                    elif(retorno_modi == MODIFICACION_CANCELADA):
                        print("Se cancelo la modificacion del proyecto")
                    else:
                        print("Error en la modificacion de proyecto")
            case 3:
                    retorno_baja = bajar_proyecto(lista_proyectos)
                    if(retorno_baja == BAJA_CORRECTA):
                        print("Se dio de baja el proyecto")
                    elif(retorno_baja == BAJA_CANCELADA):
                        print("Se cancelo la baja del proyecto")
                    else:
                        print("Error en la baja del proyecto")
            case 4:
                    cambiar_estado_por_finalizado(lista_proyectos)
            case 5:
                    mostrar_proyectos(lista_proyectos)     
            case 6:
                    promedio_proyectos = calcular_promedio_presupuesto(lista_proyectos)
                    if(promedio_proyectos != -1):
                        print("Presupuesto promedio: {}".format(promedio_proyectos))
                    else:
                        print("La lista de proyectos se encuentra vacia")
            case 7: 
                    buscar_proyecto_por_nombre(lista_proyectos)
            case 8:
                    buscar_formas_de_ordenar(lista_proyectos)
            case 9:
                    retorno_alta = dar_de_alta_cancelado(lista_proyectos)
                    if(retorno_alta == ALTA_CORRECTA):
                        print("Se dio de alta el proyecto cancelado")
                    elif(retorno_alta == ALTA_CANCELADA):
                        print("Se cancelo la alta del proyecto cancelado")
                    else:
                        print("Error en la alta del proyecto cancelado")
            case 10: 
                    calcular_promedio_qatar(lista_proyectos)
            case 11:
                    mostrar_proyectos_en_cuarentena(lista_proyectos)
            case 12:
                escribir_csv("C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_12_Parcial\\Proyectos.csv", lista_proyectos)
                print("Saliendo del sistema...")
                break
            case other:
                print("Error, Elija entre 1 y 12..")
        input("Presione enter para continuar...")
        proyectos_finalizados = buscar_proyectos_finalizados(lista_proyectos)
        escribir_json_finalizados("C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_12_Parcial\\ProyectosFinalizados.json", proyectos_finalizados)
menu()