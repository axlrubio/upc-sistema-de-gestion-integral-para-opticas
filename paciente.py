from persona import Persona

class Paciente(Persona):
    def __init__(self, dni, nombre, apellido, telefono, direccion):
        super().__init__(dni, nombre, apellido, telefono, direccion)

        self.historial_citas = []
        self.prescripciones = []

    def registrarPrescripcion():
        pass

    def agendarCitas():
        pass


    def verFicha():
        pass