class Agenda:
    def __init__(self):
        self.citas = []  
        
    def agendar_cita(self, cita):
        self.citas.append(cita)
        print("Cita agendada con éxito.")

    def ver_agenda(self):
        if not self.citas:
            print("No hay citas en la agenda.")
        else:
            for i, cita in enumerate(self.citas, start=1):
                print(f"\nCita #{i}")
                print(cita)

    def generar_reporte(self):
        estados = {"pendiente": 0, "confirmada": 0, "cancelada": 0}
        for cita in self.citas:
            if cita.estado in estados:
                estados[cita.estado] += 1

        print("\n Reporte de Citas:")
        for estado, cantidad in estados.items():
            print(f"  {estado.capitalize():<10}: {cantidad}")




# if __name__ == "__main__":
#     from datetime import datetime
    
#     agenda = Agenda()

    

  
#     agenda.ver_agenda()

#     cita2.confirmar()
#     cita1.cancelar()
#     cita3.confirmar()
    
#     print(cita2)
#     print(cita1)
#     print(cita3)

#     agenda.generar_reporte()