from funciones import *
from os import *

lista_empleados = []

id_auto_incremental = 0

def incrementar_id():
    global id_auto_incremental
    id_auto_incremental +=1
    
def decrementar_id():
    global id_auto_incremental
    id_auto_incremental +=-1
    
def imprimir_menu():
    system('cls') 
    print("MENU PRINCIPAL\n\n1)Dar de alta un empleado \n2)Modificar empleado \n3)Dar de Baja a un empleado \n4)Mostrar todos los empleados\n5)Calcular salario promedio\n6)Buscar empleado por DNI\n7)Ordenar empleado\n8)Salir")


def menu():
    while(True):
        imprimir_menu()
        opcion = int(input("Elija una opción: "))
        system('cls') 
        match opcion:
            case 1:
                incrementar_id()
                if(agregar_empleado(id_auto_incremental, lista_empleados)):
                    print("Empleado dado de alta correctamente!")
                else:
                    print("Operacion cancelada!!")
                    decrementar_id()
            case 2:
                if(contar_empleados(lista_empleados) > 0):
                    retorno_modi = modificar_alumno(lista_empleados)
                    if(retorno_modi == MODIFICACION_CORRECTA):
                        print("Se realizo la modificacion correctamente!")
                    elif(retorno_modi == MODIFICACION_CANCELADA):
                        print("Se cancelo la modificacion del empleado")
                    else:
                        print("Error en la modificacion de empleado")
                else:
                    print("No hay empleados para modificar. Ingrese al punto 1..")
            case 3:
                if(contar_empleados(lista_empleados) > 0):
                    retorno_baja = bajar_empleado(lista_empleados)
                    if(retorno_baja == BAJA_CORRECTA):
                        print("Se dio de baja el empleado")
                    elif(retorno_baja == BAJA_CANCELADA):
                        print("Se cancelo la baja del empleado")
                    else:
                        print("Error en la baja del empleado")
                else:
                    print("No hay empleados para dar la baja. Ingrese al punto 1..")
            case 4:
                if(contar_empleados(lista_empleados) > 0):
                    mostrar_empleados(lista_empleados)
                else:
                    print("No hay empleados dados de alta. Ingrese al punto 1..")
            case 5:
                if(contar_empleados(lista_empleados) > 0):
                    promedio_empleados = calcular_promedio_salario(lista_empleados)
                    print("El promedio salarial es: {}".format(promedio_empleados))
                else:
                    print("No hay empleados dados de alta. Ingrese al punto 1..")
            case 6:
                if(contar_empleados(lista_empleados) > 0):
                    mostra_por_dni(lista_empleados)
                else:
                    print("No hay empleados dados de alta. Ingrese al punto 1..")
            case 7: 
                if(contar_empleados(lista_empleados) > 0):
                    mostrar_ordenamiento(lista_empleados)
                else:
                    print("No hay empleados dados de alta. Ingrese al punto 1..")
            case 8:
                print("Saliendo del sistema...")
                break
            case other:
                print("Error, Elija entre 1 y 8..")
        input("Presione enter para continuar...")
menu()