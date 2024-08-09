# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
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

import os

def limpiar_consola():
    '''
    Función:
        Limpia la consola después de que el usuario presione Enter. 
        Solicita al usuario que presione Enter para continuar y luego
        limpiar la consola.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: os.system('cls')    
#----------------------------------------------------------- Punto 1
def obtener_nombre(dict_personaje:dict)->str:
    '''
    Función:
        Extrae el nombre de un personaje de un diccionario y lo capitaliza,
        devolviendo una cadena con el formato "Nombre: <Nombre>".

    Parámetros:
        dict_personaje (dict): Un diccionario que contiene información sobre un
        personaje. Se espera que el diccionario tenga una clave 'nombre'.

    Retorno:
        Una cadena de texto que contiene el nombre del personaje capitalizado,
        en el formato "Nombre: <Nombre>".
    '''
    nombre_personaje = dict_personaje["nombre"]
    texto = "Nombre: {}".format(nombre_personaje.capitalize())
    return texto

def imprimir_dato(dato:str)->None:
    '''
    Función:
        Imprime una cadena de texto en la consola.

    Parámetros:
        dato (str): La cadena de texto que se desea imprimir.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    print(dato)

def utn_imprimir_nombres_personajes(lista_personajes:list[dict])->None:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y utiliza las funciones `obtener_nombre` e `imprimir_dato` para imprimir
        los nombres capitalizados de los personajes en la consola.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada
        diccionario contiene información de un personaje..

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    if(lista_personajes == []):
        return -1
    else:
        for personaje in lista_personajes:
            imprimir_dato(obtener_nombre(personaje))
#----------------------------------------------------------- Punto 2
def obtener_nombre_y_dato(dict_personaje:dict, key:str)->str:
    '''
    Función:
        Extrae el nombre y un dato específico de un personaje desde un diccionario,
        y los formatea en una cadena con el formato "Nombre: <Nombre> | <key>: <dato>".

    Parámetros:
        dict_personaje (dict): Un diccionario que contiene información sobre un
        personaje.
        key (str): La clave del dato específico que se desea extraer del diccionario.

    Retorno:
        Una cadena de texto que contiene el nombre del personaje capitalizado
        y el dato específico, formateado como "Nombre: <Nombre> | <key>: <dato>".
    '''
    nombre = dict_personaje["nombre"]
    dato = dict_personaje[key]
    texto = "Nombre: {} | {}: {}".format(nombre.capitalize(), key, dato)
    return texto
#----------------------------------------------------------- Punto 3
def utn_imprimir_nombres_alturas(lista_personajes:list[dict])->None:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y utiliza la función `obtener_nombre_y_dato` para imprimir los nombres
        capitalizados y las alturas de los personajes en la consola.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada
        diccionario contiene información de un personaje.

    Retorno:
        Esta función no devuelve ningún valor. Si la lista de personajes
        está vacía, retorna -1.
    '''
    if(lista_personajes == []):
        return -1
    else:
        for personaje in lista_personajes:
            print(obtener_nombre_y_dato(personaje, "altura"))
#----------------------------------------------------------- Punto 4
def calcular_max(lista_personajes:list[dict], key:str)->dict:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y encuentra el personaje con el valor máximo para una clave específica.
        Devuelve el diccionario que representa al personaje con el valor máximo.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario
        contiene información de un personaje.
        key (str): La clave cuyo valor se quiere maximizar entre los diccionarios de la lista.

    Retorno:
        El diccionario que representa al personaje con el valor máximo para la clave especificada.
        Si la lista de personajes está vacía, retorna -1.
    '''
    if(lista_personajes == []):
        return -1
    else:
        maximo = lista_personajes[0][key]
        diccionario = {}
        for personaje in lista_personajes:
            if(personaje[key] > maximo):
                maximo = personaje[key]
                diccionario = personaje
        return diccionario

def calcular_min(lista_personajes:list[dict], key:str)->dict:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y encuentra el personaje con el valor mínimo para una clave específica.
        Devuelve el diccionario que representa al personaje con el valor mínimo.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario
        contiene información de un personaje.
        key (str): La clave cuyo valor se quiere minimizar entre los diccionarios de la lista.

    Retorno:
        El diccionario que representa al personaje con el valor mínimo para la clave especificada.
        Si la lista de personajes está vacía, retorna -1.
    '''
    if(lista_personajes == []):
        return -1
    else:
        minimo = lista_personajes[0][key]
        diccionario = {}
        for personaje in lista_personajes:
            if(personaje[key] < minimo):
                minimo = personaje[key]
                diccionario = personaje
        return diccionario

def calcular_max_min_dato(lista_personajes:list[dict], tipo_valor:str, key:str)->dict:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y encuentra el personaje con el valor máximo o mínimo para una clave específica,
        dependiendo del valor de `tipo_valor`. Devuelve el diccionario que representa
        al personaje con el valor máximo o mínimo.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario
        contiene información de un personaje.
        tipo_valor (str): Una cadena que puede ser "maximo" o "minimo", indicando si se
        desea encontrar el valor máximo o mínimo.
        key (str): La clave cuyo valor se quiere maximizar o minimizar entre los diccionarios de la lista.

    Retorno:
        El diccionario que representa al personaje con el valor máximo o mínimo para la clave especificada.
        Si la lista de personajes está vacía, retorna -1.
    '''
    if(lista_personajes == []):
        return -1
    else:
        if(tipo_valor == "minimo"):
            diccionario = calcular_min(lista_personajes, key)
        if(tipo_valor == "maximo"):
            diccionario = calcular_max(lista_personajes, key)
        return diccionario

def utn_calcular_imprimir_heroe(lista_personajes:list[dict], tipo_valor:str, key:str)->None:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y encuentra el personaje con el valor máximo o mínimo para una clave específica,
        dependiendo del valor de `tipo_valor`. Utiliza la función `imprimir_dato`
        para imprimir el nombre y el dato del personaje encontrado.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario
        contiene información de un personaje.
        tipo_valor (str): Una cadena que puede ser "maximo" o "minimo", indicando si se
        desea encontrar el valor máximo o mínimo.
        key (str): La clave cuyo valor se quiere maximizar o minimizar entre los diccionarios 
        de la lista.

    Retorno:
        Esta función no devuelve ningún valor. Si la lista de personajes está vacía, retorna -1.
    '''
    if(lista_personajes == []):
        return -1
    else:
        dict_personaje = calcular_max_min_dato(lista_personajes, tipo_valor, key)
        imprimir_dato(obtener_nombre_y_dato(dict_personaje, key))
#----------------------------------------------------------- Punto 5
def sumar_dato_personaje(lista_personajes:list[dict], key:str)->int:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y suma los valores de una clave específica para todos los personajes.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario
        contiene información de un personaje.
        key (str): La clave cuyos valores se quieren sumar entre los diccionarios de la lista.

    Retorno:
        La suma de todos los valores de la clave especificada en los personajes de la lista.
        Si la lista de personajes está vacía, retorna -1.
    '''
    if(lista_personajes == []):
        return -1
    else:
        suma = 0
        for elemento in lista_personajes:
            suma += elemento[key]
        return suma

def dividir(dividendo:int, divisor:int)->float:
    '''
    Función:
        Realiza la división del dividendo entre el divisor y devuelve el 
        resultado como un número de punto flotante.
        Si el divisor es igual a cero, devuelve 0.

    Parámetros:
        dividendo (int): El número que se va a dividir.
        divisor (int): El número por el cual se va a dividir el dividendo.

    Retorno:
        El resultado de la división como un número flotante.
        Si el divisor es igual a cero, retorna 0.
    '''
    if(divisor == 0):
        return 0
    else:
        resultado = dividendo / divisor
        return resultado

def calcular_promedio(lista_personajes:list[dict], key:str)->float:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y calcula el promedio de los valores de una clave específica para todos los personajes.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario
        contiene información de un personaje.
        key (str): La clave cuyos valores se quieren promediar entre los diccionarios de la lista.

    Retorno:
        El promedio de todos los valores de la clave especificada en los personajes de la lista.
        Si la lista de personajes está vacía, retorna -1.
    '''
    if(lista_personajes == []):
        return -1
    else:
        suma = sumar_dato_personaje(lista_personajes, key)
        promedio = dividir(suma, len(lista_personajes))
        return promedio

def utn_calcular_imprimir_promedio_dato(lista_personajes:list[dict], key:str)->None:
    '''
    Función:
        Recorre una lista de diccionarios, cada uno representando un personaje,
        y calcula el promedio de los valores de una clave específica para todos los personajes.
        Luego, imprime el resultado junto con el nombre de la clave.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario
        contiene información de un personaje.
        key (str): La clave cuyos valores se quieren promediar entre los diccionarios de la lista.

    Retorno:
        Esta función no devuelve ningún valor. Si la lista de personajes está vacía, retorna -1.
    '''
    if(lista_personajes == []):
        return -1
    else:
        texto = f"El promedio de {key} es: {round(calcular_promedio(lista_personajes, key), 2)}"
        imprimir_dato(texto)
#----------------------------------------------------------- Punto menu
def imprimir_menu(dato:str)->None:
    '''
    Función:
        Imprime el texto proporcionado como un menú en la consola, utilizando la 
        función `imprimir_dato`.

    Parámetros:
        dato (str): El texto que se imprimirá como un menú en la consola.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    imprimir_dato(dato)

def validar_entero(validar_numero:str)->bool:
    '''
    Función:
        Verifica si una cadena de texto representa un número entero válido.
        Retorna True si la cadena es un número entero válido; de lo contrario, retorna False.

    Parámetros:
        validar_numero (str): La cadena de texto que se verificará.

    Retorno:
        Devuelve True si la cadena de texto representa un número entero 
        válido; de lo contrario, False.
    '''
    if(validar_numero.isnumeric()):
        return True
    else:
        return False

def utn_menu_principal()->int:
    '''
    Función:
        Muestra un menú principal en la consola con diversas opciones y solicita al usuario 
        que ingrese un número correspondiente a una de las opciones. Verifica si 
        el número ingresado es válido utilizando la función `validar_entero` y devuelve 
        la opción seleccionada como un número entero.

    Retorno:
        La opción seleccionada por el usuario como un número entero. Si el usuario 
        ingresa un valor no numérico, retorna -1.
    '''
    imprimir_menu('''Menu Principal
1. Recorrer la lista imprimiendo por consola el nombre de cada personaje
2. Recorrer la lista imprimiendo por consola nombre de cada personaje junto a
la altura del mismo.
3. Recorrer la lista y determinar cuál es el personaje más alto (MÁXIMO).
4. Recorrer la lista y determinar cuál es el personaje más bajo (MÍNIMO).
5. Recorrer la lista y determinar la altura promedio de los
personajes
(PROMEDIO).
6. Informar cual es la identidad del personaje asociado a cada uno de los
indicadores anteriores (Opcion 3 y 4).
7. Calcular e informar cual es el personaje más y menos pesado.
8. Calcular e informar cual es el personaje mas y menos poderoso.
9. Determinar el promedio de nivel de poder de todos los personajes e informar
qué personaje/s están por debajo de ese poder.
10.Calcular e informar la cantidad total de personajes.
11.Calcular e informar cuántos personajes son de “DC Comics” y cuántos de
“Marvel Comics”
12.Ordenar los personajes en orden descendente del que tiene mayor poder al
que tiene menos, luego mostrarlos por consola con su nombre y poder.
13.Ordenar los personajes en orden ascendente del que tiene menos inteligencia
al que tiene más inteligencia. Luego mostrarlos por consola su nombre e
inteligencia.
14.Calcular e informar el promedio de poder de personajes femeninos.
15.Calcular e informar el promedio de poder de personajes masculinos.
16. Salir''')
    numero_ingresado = input("Ingrese opcion: ")
    if(validar_entero(numero_ingresado)):
        return int(numero_ingresado)
    else:
        return -1

#----------------------------------------------------------- Punto 6
def utn_imprimir_identidad(lista_personajes:list[dict], tipo_valor:str, key:str):
    '''
    Función:
        Calcula el personaje con el valor máximo o mínimo para una clave específica en
        una lista de diccionarios, luego imprime su nombre, identidad y 
        el valor correspondiente.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario 
        contiene información de un personaje.
        tipo_valor (str): El tipo de valor a calcular, puede ser "maximo" o "minimo".
        key (str): La clave cuyo valor máximo o mínimo se calculará.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    dict_personaje = calcular_max_min_dato(lista_personajes, tipo_valor, key)
    texto = f'Nombre: {dict_personaje["nombre"]} - Identidad: {dict_personaje["identidad"]} - {key.capitalize()}: {dict_personaje[key]}'
    imprimir_dato(texto)
#----------------------------------------------------------- Punto 9
def utn_imprimir_personajes_debajo_promedio(lista_personajes:list[dict], key:str)->None:
    '''
    Función:
        Calcula el promedio de los valores de una clave específica para todos los personajes 
        en una lista de diccionarios.
        Luego, imprime los detalles de los personajes cuyo valor para la clave especificada 
        está por debajo del promedio.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario 
        contiene información de un personaje.
        key (str): La clave cuyos valores se utilizarán para calcular el promedio y 
        comparar con los personajes.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    if(lista_personajes == []):
        return -1
    else:
        promedio = calcular_promedio(lista_personajes, key)
        print("Personajes por debajo del promedio:")
        for elemento in lista_personajes:
            if(elemento[key] < promedio):
                dato = obtener_nombre_y_dato(elemento, key)
                imprimir_dato(dato)
#----------------------------------------------------------- Punto 10
def utn_imprimir_cantidad_personajes(lista_personajes:list[dict])->None:
    '''
    Función:
        Calcula la cantidad de personajes en la lista de diccionarios proporcionada 
        y luego imprime este valor.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario 
        contiene información de un personaje.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    if(lista_personajes == []):
        return -1
    else:
        cantidad = len(lista_personajes)
        texto = f"La cantidad de personajes es: {cantidad}"
        imprimir_dato(texto)
#----------------------------------------------------------- Punto 11
def calcular_por_empresa(lista_personajes:list[dict], key:str)->int:
    '''
    Función:
        Itera sobre la lista de diccionarios de personajes y cuenta cuántos de ellos están 
        asociados a una empresa específica.
        Retorna la cantidad total de personajes asociados a la empresa especificada 
        por la clave `key`.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario 
        contiene información de un personaje.
        key (str): La clave que representa la empresa a la que se asocian los personajes.

    Retorno:
        La cantidad de personajes asociados a la empresa específica.
    '''
    if(lista_personajes == []):
        return -1
    else:
        cantidad = 0
        for elemento in lista_personajes:
            if(elemento["empresa"] == key):
                cantidad += 1
        return cantidad

def utn_imprimir_empresa(lista_personajes:list[dict], key:str)->None:
    '''
    Función:
        Calcula la cantidad de personajes asociados a una empresa específica 
        en una lista de diccionarios de personajes y luego imprime este valor 
        junto con el nombre de la empresa.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario 
        contiene información de un personaje.
        key (str): La clave que representa la empresa a la que se asocian los personajes.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    if(lista_personajes == []):
        return -1
    else:
        cantidad = calcular_por_empresa(lista_personajes, key)
        texto = f"La cantidad de personajes de la empresa {key} es {cantidad}"
        imprimir_dato(texto)
#----------------------------------------------------------- Punto 12-13
def ordenar_por_valor(lista_personajes:list[dict], key:str, orden:bool)->list:
    '''
    Función:
        Ordena una lista de diccionarios de personajes basándose en el valor de una 
        clave específica, en orden ascendente o descendente.
        Utiliza el algoritmo de burbuja para realizar la ordenación.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario 
        contiene información de un personaje.
        key (str): La clave cuyo valor se utilizará para realizar la ordenación.
        orden (bool): Un valor booleano que indica si la ordenación se realizará 
        en orden ascendente (True) o descendente (False).

    Retorno:
        La lista de personajes ordenada según el valor de la clave especificada, 
        o -1 si la lista está vacía.
    '''
    if(lista_personajes == []):
        return -1
    else:
        flag_swap = True
        rango_lista = len(lista_personajes)
        while(flag_swap):
            flag_swap = False
            rango_lista = rango_lista-1
            for heroe in range(rango_lista):
                if((orden == True and lista_personajes[heroe][key] > lista_personajes[heroe+1][key]) or (orden == False and lista_personajes[heroe][key] < lista_personajes[heroe+1][key])):
                    aux = lista_personajes[heroe]
                    lista_personajes[heroe] = lista_personajes[heroe+1]
                    lista_personajes[heroe+1] = aux
                    flag_swap = True
    return lista_personajes

'''
Intente hacer Quick Sort y no me salio!
def ordenar_por_valor(lista_personajes:list[dict], key:str, orden:str)->list:
    if(lista_personajes == []):
        return -1
    else:
        pivot = lista_personajes[-1]
    lista_mas_grandes = []
    lista_mas_chicos = []

    for elemento in lista_personajes[:-1]:  
        if elemento[key] > pivot[key]:
            lista_mas_grandes.append(elemento)
        else:
            lista_mas_chicos.append(elemento)

    if orden == "mayor":
        return ordenar_por_valor(lista_mas_grandes, key, orden) + [pivot] + ordenar_por_valor(lista_mas_chicos, key, orden)
    else:
        return ordenar_por_valor(lista_mas_chicos, key, orden) + [pivot] + ordenar_por_valor(lista_mas_grandes, key, orden)
'''

def utn_imprimir_valor_por_orden(lista_personajes:list[dict], key:str, orden:str)->None:
    '''
    Función:
        Ordena la lista de personajes según los valores de una clave específica en 
        orden ascendente o descendente, y luego imprime los detalles de cada personaje.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario 
        contiene información de un personaje.
        key (str): La clave cuyos valores se utilizarán para realizar la ordenación y la impresión.
        orden (str): El criterio de ordenación, puede ser ascendente o descendente.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    if(lista_personajes == []):
        return -1
    else:
        lista_ordenada = ordenar_por_valor(lista_personajes, key, orden)
        for elemento in lista_ordenada:
            texto = obtener_nombre_y_dato(elemento, key)
            imprimir_dato(texto)
#----------------------------------------------------------- Punto 14-15
def utn_imprimir_dato_por_genero(lista_personajes:list[dict], key:str, genero:str)->None:
    '''
    Función:
        Calcula el promedio de genero específico de una lista de diccionarios de personajes 
        y luego imprime este valor junto con el genero.

    Parámetros:
        lista_personajes (list[dict]): Una lista de diccionarios donde cada diccionario 
        contiene información de un personaje.
        key (str): La clave que representa la empresa a la que se asocian los personajes.
        genero (str): La clave que representa el genero a la que se asocian los personajes.

    Retorno:
        Esta función no devuelve ningún valor.
    '''
    if(lista_personajes == []):
        return -1
    else:
        lista_por_genero = []
        for elemento in lista_personajes:
            if(elemento["genero"] == genero):
                lista_por_genero.append(elemento)
        promedio = round(calcular_promedio(lista_por_genero, key),2)
        texto = f"La promedio de {key} de personajes de genero {genero} es de: {promedio}"
        imprimir_dato(texto)


