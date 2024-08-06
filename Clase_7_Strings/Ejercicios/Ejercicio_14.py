''' Cubilla Damian - 1H
Escribir una función que tome una URL y devuelva solo el nombre de dominio,
por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
'''
def buscar_dominio(texto:str)->str:
    indice_primer_punto = texto.index(".")
    primer_rebanado = texto[indice_primer_punto+1:]
    indice_segundo_punto = texto.index(".")
    segundo_rebanado = primer_rebanado[:indice_segundo_punto]
    return segundo_rebanado

pagina = "https://www.ejemplo.com.ar/pagina1"
print(buscar_dominio(pagina))