'''Cubilla Damian
14. Crear la función es_fecha que reciba dos string, el primero representa la
expresión a evaluar y el segundo el separador de la fecha (puede ser la barra /
o el guión -) y que devuelva True en caso de tratarse de una fecha válida y
False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o
‘dd-mm-aaaa’
'''
import re
def es_fecha(expresion:str, separador:str)->bool:
    texto = "{0}{1}{2}{3}{4}".format(expresion[:2],separador,expresion[2:4],separador,expresion[4:8])
    if(re.search(r"([0-9]{2}/[0-9]{2}/[0-9]{4})|([0-9]{2}-[0-9]{2}-[0-9]{4})",texto) == None or len(expresion)>8):
        return False
    else:
        print(texto)
        return True
    

print(es_fecha("13222011","-"))