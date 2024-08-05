''' Cubilla Damian - 1H
Crea una función que reciba como parámetro una cadena de texto y devuelva
la cantidad de vocales que tiene.
'''
def contabilizar_vocales(texto:str)->int:
    contador = 0
    for elemento in range(len(texto)):
        if(texto[elemento] == 'a' or texto[elemento] == 'e' or texto[elemento] == 'i' or texto[elemento] == 'o' or texto[elemento] == 'u'):
            contador += 1
    return contador
test_texto = "el mas grande de la argentina, river plate"
print(f"{test_texto} - Tiene {contabilizar_vocales(test_texto)} vocales")