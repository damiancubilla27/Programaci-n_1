'''Cubilla Damian
15.Crear la función es_hora que reciba un string y que devuelva True en caso de
tratarse de una hora válida y False en el caso contrario. El formato admitido
es ‘hh:mm:ss’
'''
import re
def es_hora(texto:str)->bool:
    if(re.search(r"([0-9]{2}:[0-9]{2}:[0-9]{2})",texto) == None or len(texto)>8):
        return False
    else:
        return True
    
print(es_hora("19:07:55"))