# MIT License
#
# Copyright (c) 2023 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Nivel 1 - Elemental
# 00 - Cargar el json con pokemones en una lista
# 01 - Imprimir nombres de pokemones
# 02 - Imprimir pokemones que tengan un ID par
# 03 - Imprimir pokemones que tengan un ID multiplo de 25
# 04 - Imprimir nombre de pokemones con su ID de prefijo.
# 05 - Imprimir los pokemones con mas poder y cuanto poder tienen (misma fuerza)
# 06 - Imprimir los pokemones con menos poder y cuanto poder tienen (misma fuerza)

import os


_b_red: str = '\033[41m'
_b_green: str = '\033[42m'
_b_blue: str = '\033[44m'
_f_white: str = '\033[37m'
_no_color: str = '\033[0m'

def imprimir_mensaje(mensaje: str, tipo_mensaje: str) -> None:
    """
    This function prints a message with a specified type (error, success, or info) in a colored format.
    
    :param mensaje: a string containing the message to be printed
    :type mensaje: str
    :param tipo_mensaje: The parameter "tipo_mensaje" is a string that represents the type of message
    that will be printed. It can be "Error", "Success", or "Info"
    :type tipo_mensaje: str
    """
    tipo_mensaje = tipo_mensaje.strip().capitalize()
    match tipo_mensaje:
        case 'Error':
            print(f'{_b_red}{_f_white}> Error: {mensaje}{_no_color}')
        case 'Success':
            print(f'{_b_green}{_f_white}> Success: {mensaje}{_no_color}')
        case 'Info':
            print(f'{_b_blue}{_f_white}> Information: {mensaje}{_no_color}')
        
def limpiar_consola() -> None:
    """
    This function clears the console screen and waits for user input to continue.
    """
    _ = input('Presione una tecla para continuar...')
    if os.name in ['ce', 'nt', 'dos']: os.system("cls")
    else: os.system("clear")

# Escribir debajo las funciones de los enunciados

# ------------------------------------------------------------- Punto 1
def capitalizar_palabras(texto:str)->str:
    lista_palabras = texto.split(" ")
    for i in range(len(lista_palabras)):
        lista_palabras[i] = lista_palabras[i].capitalize()
    texto_capitalizado = " ".join(lista_palabras)
    return texto_capitalizado

def obtener_nombre_pokemon(dict_pokemon:dict)->str:
    nombre_pokemon = capitalizar_palabras(dict_pokemon.get("nombre"))
    return nombre_pokemon

def pokedex_imprimir_nombre_pokemones(lista_pokemones:list[dict])->None:
    if(lista_pokemones != []):
        for elemento in lista_pokemones:
            nombre = obtener_nombre_pokemon(elemento)
            imprimir_mensaje(nombre, "Info")
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

# ------------------------------------------------------------- Punto 2
def tiene_id_par(dict_pokemon:dict)->bool:
    if(dict_pokemon.get("id") % 2 == 0):
        return True
    else:
        return False

def obtener_id_pokemon(dict_pokemon:dict)->str:
    numero_id = dict_pokemon.get("id")
    return str(numero_id)

def pokedex_imprimir_pokemon_id_par(lista_pokemones:list[dict])->None:
    if(lista_pokemones != []):
        for elemento in lista_pokemones:
            if(tiene_id_par(elemento)):
                imprimir_mensaje(obtener_nombre_pokemon(elemento), "Info")
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

# ------------------------------------------------------------- Punto 3
def id_multiplo_25(dict_pokemon:dict)->bool:
    id_pokemon = dict_pokemon.get("id")
    if(id_pokemon % 25 == 0):
        return True
    else:
        return False

def pokedex_imprimir_pokemon_id_mul_25(lista_pokemones:list[dict])->None:
    if(lista_pokemones != []):
        for elemento in lista_pokemones:
            if(id_multiplo_25(elemento)):
                imprimir_mensaje(obtener_nombre_pokemon(elemento), "Info")
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

# ------------------------------------------------------------- Punto 4
def nombre_format_pokemon(dict_pokemon:dict)->str:
    nombre_pokemon = obtener_nombre_pokemon(dict_pokemon)
    id_pokemon = obtener_id_pokemon(dict_pokemon)
    id_pokemon = id_pokemon.zfill(3)
    retorno = f"#{id_pokemon} - {nombre_pokemon}"
    return retorno

def pokedex_imprimir_nombres_poke_fmt(lista_pokemones:list[dict])->None:
    if(lista_pokemones != []):
        for elemento in lista_pokemones:
            imprimir_mensaje(nombre_format_pokemon(elemento), "Info")
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

# ------------------------------------------------------------- Punto 5
def buscar_valor_pokemon_mas_fuerte(lista_pokemones:list[dict], criterio:str)->int:
    if(lista_pokemones != []):
        numero = lista_pokemones[0]["poder"]
        if(criterio == "Maximo"):
            for elemento in lista_pokemones[1:]:
                if(elemento.get("poder") > numero):
                    numero = elemento.get("poder")
        elif(criterio == "Minimo"):
            for elemento in lista_pokemones[1:]:
                if(elemento.get("poder") < numero):
                    numero = elemento.get("poder")
        return numero
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

def pokedex_pokemones_fuerza_max_min(lista_pokemones:list[dict], criterio:str)->None:
    if(lista_pokemones != []):
        numero = buscar_valor_pokemon_mas_fuerte(lista_pokemones, criterio)
        for elemento in lista_pokemones:
            if(elemento.get("poder") == numero):
                imprimir_mensaje(nombre_format_pokemon(elemento), "Info")
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")