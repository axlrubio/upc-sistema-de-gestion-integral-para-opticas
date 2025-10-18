from paciente import Paciente
from optometrista import Optometrista

class Cita:
    def __init__(self, paciente, optometrista, fecha_hora, estado="pendiente"):
        self.__paciente: Paciente = paciente 
        self.__optometrista: Optometrista = optometrista
        self.__fecha_hora = fecha_hora
        self.__estado = estado
        
    @property
    def paciente(self):
        return self.__paciente 
    
    @property
    def optometrista(self):
        return self.__optometrista
    
    @property
    def fecha_hora(self):
        return self.__fecha_hora 
    
    @property
    def estado(self):
        return self.__estado
    
    @fecha_hora.setter
    def fecha_hora(self, nueva_fecha):
        self.__fecha_hora = nueva_fecha 
        
    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado in ["pendiente","confirmada","cancelada"]:
            self.__estado = nuevo_estado
        else:
            raise ValueError("Estado invalido.") 
        
    def confirmar(self):
        if self.__estado == "confirmada":
            print("La cita esta confirmada")
        elif self.__estado == "cancelada":
            print("No se puede confirmar una cita cancelada.")
        else:
            self.__estado = "confirmada"
            print(f"Cita confirmada para {self.__paciente} con {self.__optometrista} el {self.__fecha_hora}.")
            

    def cancelar(self):
        if self.__estado == "cancelada":
            print("La cita esta cancelada.")
        else:
            self.__estado = "cancelada"
            # print(f"cita cancelada para {self.__paciente} con {self.optometrista}.") 
             
    def __str__(self):
        detalle = ""

        detalle += "Paciente: \n"
        detalle += f"  DNI: {self.__paciente.dni} \n"
        detalle += f"  Nombre: {self.__paciente.nombre} {self.__paciente.apellido} \n"
        detalle += "Optometrista: \n"
        detalle += f"  DNI: {self.__optometrista.dni} \n"
        detalle += f"  Nombre: Dr. {self.__optometrista.nombre} {self.__optometrista.apellido} \n"
        detalle += f"Fecha y Hora: {self.__fecha_hora} \n"
        detalle += f"Estado: {self.__estado}"

        return detalle  
        
