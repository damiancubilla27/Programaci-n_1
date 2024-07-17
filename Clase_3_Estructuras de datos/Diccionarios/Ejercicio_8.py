''' Cubilla Damian - 1H
8. Crea un diccionario que represente las edades de varias personas, 
donde las claves son los nombres de las personas y los valores 
son sus edades. Imprime la edad de la persona más joven.
'''
dict_personas = {"damian":28, "aldna":20, "camila":25}
mas_joven = dict_personas["damian"]
for elemento in dict_personas.keys():
    if(dict_personas[elemento] < mas_joven):
        mas_joven = dict_personas[elemento]
print(f"{mas_joven}")