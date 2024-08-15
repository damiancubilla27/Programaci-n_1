#Creacion de un objeto
class Personaje:
    def __init__(self, id, nombre, identidad, alias) -> None:
        self.__id = id#atributos del objeto
        self.__nombre = nombre
        self.__identidad = identidad
        self.__alias = alias

    def get_id(self): #Lectura del atributo privado
        return self.__id
    
    def set_id(self, nuevo_id):#Escritura del atributo privado
        self.__id = nuevo_id

    def retornar_nombre_en_mayuscula(self)-> str: #Metodo para la clase
        return self.__nombre.upper()
    
    def imprimir_nombre_identidad_alias(self)-> None: #Metodo para la clase
        print(f"{self.__nombre} - {self.__identidad} - {self.__alias}")

class Heroe(Personaje): #Herencia de la clase Personaje
    def __init__(self, id, nombre, identidad, alias, edad) -> None:
        super().__init__(id, nombre, identidad, alias) #Hereda estos atributos de la clase madre
        self.edad = edad #Se agrega un nuevo atributo (No existente en la clase madre)

objeto_personaje = Personaje(1, "Damian", "Cubilla", "Chino")
#print(objeto_personaje.alias) Llamar al objeto y mostrar el atributo

objeto_personaje_dos = Personaje(2, "Emiliano", "Martinez", "Dibu")
#print(objeto_personaje.alias) Creacion y llamada a varios objetos
#print(objeto_personaje_dos.alias)

objeto_heroe = Heroe(3, "Lionel", "Messi", "Pulga", 37)#Creando el objeto Heroe (Herencia de Personaje) 

lista_de_personajes = [objeto_personaje, objeto_personaje_dos, objeto_heroe] #Lista de objetos

'''  Creando una lista de objetos e iterando sobre sus atributos y metodos'''
for personaje in lista_de_personajes:
    print(f"El nombre del personaje es: {personaje.retornar_nombre_en_mayuscula()}")
    personaje.imprimir_nombre_identidad_alias()


