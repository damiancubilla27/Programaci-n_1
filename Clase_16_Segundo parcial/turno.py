class Turno:
    id_autoincremental = 0
    def __init__(self, id_paciente, especialidad, obra_social, monto_a_pagar, estado_turno) -> None:
        Turno.id_autoincremental += 1
        self.__id = Turno.id_autoincremental
        self.__id_paciente = id_paciente
        self.__especialidad = especialidad
        self.__obra_social = obra_social
        self.__monto_a_pagar = monto_a_pagar
        self.__estado_turno = estado_turno

    def mostrar(self):
        return f"{self.get_id} | {self.get_id_paciente} | {self.get_especialidad} | {self.get_obra_social} | {self.get_monto_a_pagar} | {self.get_estado_turno}"
    
    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_id_paciente(self):
        return self.__id_paciente
    
    @property
    def get_especialidad(self):
        return self.__especialidad
    
    @property
    def get_obra_social(self):
        return self.__obra_social
    
    @property
    def get_monto_a_pagar(self):
        return self.__monto_a_pagar
    
    @property
    def get_estado_turno(self):
        return self.__estado_turno
    
    @get_id.setter
    def set_id(self, nuevo_id):
        self.__id = nuevo_id
    
    @get_id_paciente.setter
    def set_id_paciente(self, nuevo_paciente):
        self.__id_paciente = nuevo_paciente

    @get_especialidad.setter
    def set_especialidad(self, nueva_especialidad):
        self.__especialidad = nueva_especialidad

    @get_obra_social.setter
    def set_obra_social(self, nueva_obra):
        self.get_obra_social = nueva_obra

    @get_monto_a_pagar.setter
    def set_monto_a_pagar(self, nuevo_monto):
        self.__monto_a_pagar = nuevo_monto

    @get_estado_turno.setter
    def set_estado_turno(self, nuevo_estado):
        self.__estado_turno = nuevo_estado
