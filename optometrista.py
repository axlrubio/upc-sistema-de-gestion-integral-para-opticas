# -*- coding: utf-8 -*-
from persona import Persona

class Optometrista(Persona):
    def __init__(self, dni, nombre, apellido, telefono, direccion, id_medico, especialidad):
        super().__init__(dni, nombre, apellido, telefono, direccion)
        self.id_medico = id_medico
        self.especialidad = especialidad

    def __str__(self):
        info_persona = super().__str__()
        info_optometrista = (
            "\n--- Datos Profesionales ---\n"
            f"ID Médico: {self.id_medico}\n"
            f"Especialidad: {self.especialidad}"
        )
        return info_persona + info_optometrista
