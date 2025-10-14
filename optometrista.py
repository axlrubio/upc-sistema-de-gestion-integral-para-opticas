from persona import Persona

class Optometrista(Persona):
    def __init__(self, dni, nombre, apellido, telefono, direccion, especialidad):
        super().__init__(dni, nombre, apellido,telefono, direccion)
        
        self.especialidad = especialidad