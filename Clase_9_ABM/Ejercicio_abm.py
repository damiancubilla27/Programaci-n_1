from funciones import *
from os import *

lista_alumnos = []

id_auto_incremental = 0

def incrementar_id():
    global id_auto_incremental
    id_auto_incremental +=1
    
def decrementar_id():
    global id_auto_incremental
    id_auto_incremental +=-1
    
def imprimir_menu():
    system('cls') 
    print("MENU PRINCIPAL\n\n1)Dar de alta un alumno \n2)Modificar Alumno \n3)Dar de Baja a un alumno \n4)Mostrar todos los alumnos\n5)Salir del programa")


def menu():
    while(True):
        imprimir_menu()
        opcion = int(input("Elija una opción: "))
        system('cls') 
        match opcion:
            case 1:
                incrementar_id()
                if(agregar_alumno(id_auto_incremental, lista_alumnos)):
                    print("Alumno dado de alta correctamente!")
                else:
                    print("Operacion cancelada!!")
                    decrementar_id()
            case 2:
                if(contar_alumnos(lista_alumnos) > 0):
                    retorno_modi = modificar_alumno(lista_alumnos)
                    if(retorno_modi == MODIFICACION_CORRECTA):
                        print("Se realizo la modificacion correctamente!")
                    elif(retorno_modi == MODIFICACION_CANCELADA):
                        print("Se cancelo la modificacion del alumno")
                    else:
                        print("Error en la modificacion de alumno")
                else:
                    print("No hay alumnos para modificar. Ingrese al punto 1..")
            case 3:
                if(contar_alumnos(lista_alumnos) > 0):
                    retorno_baja = dar_de_baja_alumno(lista_alumnos)
                    if(retorno_baja == BAJA_CORRECTA):
                        print("Se dio de baja el alumno")
                    elif(retorno_baja == BAJA_CANCELADA):
                        print("Se cancelo la baja del alumno")
                    else:
                        print("Error en la baja del alumno")
                else:
                    print("No hay alumnos para dar la baja. Ingrese al punto 1..")
            case 4:
                if(contar_alumnos(lista_alumnos) > 0):
                    mostrar_alumnos(lista_alumnos)
                else:
                    print("No hay alumnos dados de alta. Ingrese al punto 1..")
            case 5:
                print("Saliendo del sistema...")
                break
            case other:
                print("Error, Elija entre 1 y 5..")
        input("Presione enter para continuar...")
menu()