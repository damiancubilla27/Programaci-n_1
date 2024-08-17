import library_utn as utn
from library_utn import *
from archivos import *

# Listas del json
lista_pacientes_json = leer_json_pacientes()
lista_especialidades = leer_json_especialidades()
lista_obras_sociales = leer_json_obras_sociales()

#Creacion de objeto paciente
lista_pacientes_objetos = crear_objeto_pacientes(lista_pacientes_json)
id_auto_incremental = len(lista_pacientes_objetos)

#Listas para escribir json
lista_pacientes_con_turno = []
lista_turnos = []

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



def main_app():
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
    
    while True:
        imprimir_menu()
        selected_option = int(input("Elija una opción: "))
        match selected_option:
            case 1: # Alta paciente
                incrementar_id()
                if(agregar_paciente(id_auto_incremental, lista_pacientes_objetos)):
                    print("Paciente dado de alta correctamente!")
                else:
                    print("Operacion cancelada!!")
                    decrementar_id()
            case 2: # Alta turno
                if(alta_turno(lista_turnos, lista_pacientes_objetos, lista_especialidades, lista_obras_sociales, lista_pacientes_con_turno)):
                    print("Turno dado de alta correctamente!")
                    mostrar_turnos(lista_turnos)
                else:
                    print("Turno cancelado!!")
            case 3: #Ordenar Turnos
                ordenar_turnos(lista_turnos)
            case 4: # Mostrar pacientes en espera (Turnos Activos)
                mostrar_turnos_activos(lista_turnos)
            case 5: # Atender pacientes
                if(atender_pacientes_con_turno(lista_turnos)):
                    mostrar_turnos_finalizados(lista_turnos)
                else:
                    print("No se encontraron Turnos Activos!!")
            case 6: # Cobrar atenciones
                cobrar_atenciones(lista_turnos)
            case 7: # Cerrar caja
                cerrar_caja(lista_turnos, lista_pacientes_objetos, lista_pacientes_con_turno)
            case 8: # Mostrar informe
                informar_obras_sociales_ingresos(lista_turnos)
            case 9: # Salir
                break
            case _:
                utn.UTN_messenger('Opción inválida. Por favor, seleccione una opción válida.', 'Error')
        utn.clear_console()
        guardar_turnos_json(lista_turnos)