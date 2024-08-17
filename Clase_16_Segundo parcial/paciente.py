class Paciente:
    def __init__(self, id, nombre, apellido, dni, edad, fecha_registro, obra_social) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__edad = edad
        self.__fecha_registro = fecha_registro
        self.__obra_social = obra_social
    
    def mostrar(self):
        return f"{self.get_id} | {self.get_nombre} | {self.get_apellido} | {self.get_dni} | {self.get_edad} | {self.get_fecha_registro} | {self.get_obra_social}"
    
    @property
    def get_id(self):
        return self.__id
    
    @get_id.setter
    def set_id(self, nuevo_id):
        self.__id = nuevo_id

    @property
    def get_nombre(self):
        return self.__nombre
    
    @get_nombre.setter
    def set_nombre(self, nombre_nuevo):
        self.__nombre = nombre_nuevo
    
    @property   
    def get_apellido(self):
        return self.__apellido
    
    @get_apellido.setter
    def set_apellido(self, apellido_nuevo):
        self.__apellido = apellido_nuevo
    
    @property
    def get_dni(self):
        return self.__dni
    
    @get_dni.setter
    def set_dni(self, nuevo_dni):
        self.__dni = nuevo_dni
    
    @property
    def get_edad(self):
        return self.__edad
    
    @get_edad.setter
    def set_edad(self, nuevo_edad):
        self.__edad = nuevo_edad
    
    @property
    def get_fecha_registro(self):
        return self.__fecha_registro
    
    @get_fecha_registro.setter
    def set_fecha_registro(self, nuevo_fecha_registro):
        self.__fecha_registro = nuevo_fecha_registro

    @property
    def get_obra_social(self):
        return self.__obra_social
    
    @get_obra_social.setter
    def set_obra_social(self, nuevo_obra_social):
        self.__obra_social = nuevo_obra_social

    
