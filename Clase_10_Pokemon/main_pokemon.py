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

# importar dentro de los parentesis las funciones necesarias
import re
from poke_lib_elemental import (
    limpiar_consola, imprimir_mensaje, pokedex_imprimir_nombre_pokemones,
    pokedex_imprimir_pokemon_id_par, pokedex_imprimir_pokemon_id_mul_25,
    pokedex_imprimir_nombres_poke_fmt, pokedex_pokemones_fuerza_max_min
)

# importar dentro de los parentesis las funciones necesarias
from poke_lib_basico import (
    pokedex_promedio_poder_tipo
)
# importar dentro de los parentesis las funciones necesarias
from poke_lib_intermedio import (
    podekex_pokemones_varios_atributo, pokedex_pokemones_atributo_y_cantidad
)
# importar dentro de los parentesis las funciones necesarias
from poke_lib_int_avan import (
    pokedex_imprimir_multiples_atributos
)
# importar dentro de los parentesis las funciones necesarias
#from poke_lib_avanzado import (
    
#)


def pokemon_app(pokemones: list[dict]) -> None:
    
    while True:
        menu =\
"""
1 - Imprimir nombre de pokemones.
2 - Imprimir pokemones que tengan un ID par
3 - Imprimir pokemones que tengan un ID multiplo de 25
4 - Imprimir nombre de pokemones con su ID de prefijo.
5 - Imprimir los pokemones con mas poder y cuanto poder tienen (misma fuerza)
6 - Imprimir los pokemones con menos poder y cuanto poder tienen (misma fuerza)
7 - Imprimir el promedio de poder de pokemones que entre sus tipos tenga 'psiquico'
8 - Imprimir el promedio de poder de pokemones que entre sus tipos tenga 'fuego'
9 - Imprimir el promedio de poder de pokemones que entre sus tipos tenga 'electrico'
10 - Imprimir pokemones que posean mas de un tipo
11 - Imprimir pokemones que posean mas de un tipo y su cantidad
12 - Imprimir pokemones que posean mas de una evolucion
13 - Imprimir pokemones que posean mas de una evolucion y su cantidad
14 - Imprimir pokemones que posean mas de una fortaleza
15 - Imprimir pokemones que posean mas de una fortaleza y su cantidad
16 - Imprimir pokemones que posean mas de una debilidad
17 - Imprimir pokemones que posean mas de una debilidad y su cantidad
18 - Imprimir los tipos de cada pokemon
19 - Imprimir las evoluciones de cada pokemon
20 - Imprimir las debilidades de cada pokemon
21 - Imprimir las fortalezas de cada pokemon
22 - Imprimir pokemones agrupados por tipo. 
    (Si poseen mas de un tipo, debera aparecer en cada uno de ellos)
23 - Imprimir pokemones con su id, nombre, fuerza, tipos, 
    evoluciones, fortalezas y debilidades
24 - Filtrar pokemones por tipo y guardarlos en un JSON
25 - Ordenar pokemones por una clave de forma ASC o DESC y guardar en JSON
26 - Salir de la aplicacion.
_______________________________________________________________
"""
        
        opcion = 0
        opcion_str = input(f'{menu}Su opcion: ')
        if re.match('^[0-9]{1,2}$', opcion_str):
            opcion = int(opcion_str)

        match opcion:
            case 1:
                pokedex_imprimir_nombre_pokemones(pokemones)
            case 2:
                pokedex_imprimir_pokemon_id_par(pokemones)
            case 3:
                pokedex_imprimir_pokemon_id_mul_25(pokemones)
            case 4:
                pokedex_imprimir_nombres_poke_fmt(pokemones)
            case 5:
                pokedex_pokemones_fuerza_max_min(pokemones, "Maximo")
            case 6:
                pokedex_pokemones_fuerza_max_min(pokemones, "Minimo")
            case 7:
                pokedex_promedio_poder_tipo(pokemones, "tipo", "psiquico")
            case 8:
                pokedex_promedio_poder_tipo(pokemones, "tipo", "fuego")
            case 9:
                pokedex_promedio_poder_tipo(pokemones, "tipo", "electrico")
            case 10:
                podekex_pokemones_varios_atributo(pokemones, "tipo")
            case 11:
                pokedex_pokemones_atributo_y_cantidad(pokemones, "tipo")
            case 12:
                podekex_pokemones_varios_atributo(pokemones, "evoluciones")
            case 13:
                pokedex_pokemones_atributo_y_cantidad(pokemones, "evoluciones")
            case 14:
                podekex_pokemones_varios_atributo(pokemones, "fortaleza")
            case 15:
                pokedex_pokemones_atributo_y_cantidad(pokemones, "fortaleza")
            case 16:
                podekex_pokemones_varios_atributo(pokemones, "debilidad")
            case 17:
                pokedex_pokemones_atributo_y_cantidad(pokemones, "debilidad")
            case 18:
                pokedex_imprimir_multiples_atributos(pokemones, "tipo")
            case 19:
                pokedex_imprimir_multiples_atributos(pokemones, "evoluciones")
            case 20:
                pokedex_imprimir_multiples_atributos(pokemones, "debilidad")
            case 21:
                pokedex_imprimir_multiples_atributos(pokemones, "fortaleza")
            case 22:
                pass
            case 23:
                pass
            case 24:
                pass
            case 25:
                pass
            case 26:
                break
            case _:
                imprimir_mensaje(f'La opcion {opcion} es incorrecta!', 'error')
        limpiar_consola()


if __name__ == '__main__':
    #PATH = './data_pokemones.json' # Editar ruta de archivo JSON
    from data_pokemones import pokemones
    pokemon_app(pokemones)