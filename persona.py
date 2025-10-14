class Persona:
    def __init__(self, dni, nombre, apellido, telefono, direccion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
    
    @property
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self):
        
        return (f"DNI: {self.dni}\n"
                f"Nombre: {self.nombre} {self.apellido}\n"
                f"Teléfono: {self.telefono}\n"
                f"Dirección: {self.direccion}")

    def modificar_datos(self, nuevo_telefono, nueva_direccion):
        
        self.telefono = nuevo_telefono
        self.direccion = nueva_direccion
        print("Datos actualizados correctamente.")