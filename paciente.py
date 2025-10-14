from persona import Persona

class Paciente(Persona):
    def __init__(self, dni, nombre, apellido, telefono, direccion):
        
        super().__init__(dni, nombre, apellido, telefono, direccion)

        self.historial_citas = []
        self.prescripciones = []

    def agregar_cita(self, cita):
        
        self.historial_citas.append(cita)
        print(f"Cita para {self.nombre_completo} agendada correctamente.")

    def agregar_prescripcion(self, prescripcion):
       
        self.prescripciones.append(prescripcion)
        print(f"Prescripción registrada para {self.nombre_completo}.")

    def __str__(self):
        
        info_persona = super().__str__()
        
       
        info_paciente = (f"\n--- Historial del Paciente ---\n"
                         f"Número de citas: {len(self.historial_citas)}\n"
                         f"Número de prescripciones: {len(self.prescripciones)}")
        
        return info_persona + info_paciente