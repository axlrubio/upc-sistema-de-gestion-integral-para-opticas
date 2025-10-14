from venta import Venta
from agenda import Agenda
from inventario import Inventario
from cita import Cita
from paciente import Paciente
from optometrista import Optometrista
from paciente import Paciente
from typing import List
from datetime import datetime
from lente import Lente
from montura import Montura
import os

class Main:
    def __init__(self):
        self.optometristas:List[Optometrista] = []
        self.pacientes: List[Paciente] = []

        # Generando optometrista por defecto
        optometrista1 = Optometrista('55555555', 'Optometrista 1', 'OP Prueba', '909090909', '-', '1', 'Especialidad 1')
        optometrista2 = Optometrista('66666666', 'Optometrista 2', 'OP Prueba', '909090901', '-', '2', 'Especialidad 2')
        optometrista3 = Optometrista('77777777', 'Optometrista 3', 'OP Prueba', '909090902', '-', '3', 'Especialidad 3')
        optometrista4 = Optometrista('88888888', 'Optometrista 4', 'OP Prueba', '909090903', '-', '4', 'Especialidad 4')
        
        self.optometristas.append(optometrista1)
        self.optometristas.append(optometrista2)
        self.optometristas.append(optometrista3)
        self.optometristas.append(optometrista4)

        # Generando pacientes por defecto
        paciente1 = Paciente('11111111', 'Paciente 1', 'Prueba', '999999999', ' - ')
        paciente2 = Paciente('22222222', 'Paciente 2', 'Prueba', '999999991', ' - ')
        paciente3 = Paciente('33333333', 'Paciente 3', 'Prueba', '999999992', ' - ')
        paciente4 = Paciente('44444444', 'Paciente 4', 'Prueba', '999999993', ' - ')

        self.pacientes.append(paciente1)
        self.pacientes.append(paciente2)
        self.pacientes.append(paciente3)
        self.pacientes.append(paciente4)

        # Generando citas por paciente
        cita1 = Cita(paciente1, optometrista1, "2025-11-01 10:00")
        cita2 = Cita(paciente2, optometrista2, "2025-11-02 11:00")
        cita3 = Cita(paciente3, optometrista3, "2025-11-03 12:00")
        cita4 = Cita(paciente4, optometrista4, "2025-11-03 12:00")

        # Agenda por defecto
        self.agenda = Agenda()
        
        self.agenda.agendar_cita(cita1)
        self.agenda.agendar_cita(cita2)
        self.agenda.agendar_cita(cita3)
        self.agenda.agendar_cita(cita4)

        cita1.cancelar()
        cita2.confirmar()
        cita3.cancelar()
        cita4.confirmar()

        self.inventario = Inventario()

        lente1 = Lente("LN001", "Ray-Ban", "Aviator", 550.00, 10, "Sol")
        lente2 = Lente("LN002", "Oakley", "Holbrook", 480.00, 8, "Deportivo")
        lente3 = Lente("LN003", "Vogue", "Classic", 420.00, 12, "Receta")
        lente4 = Lente("LN004", "Gucci", "Elegance", 980.00, 5, "Sol polarizado")

        montura1 = Montura("MT001", "Ray-Ban", "RB3548N", 320.00, 15, "Metal")
        montura2 = Montura("MT002", "Vogue", "VO5163", 280.00, 20, "Acetato")
        montura3 = Montura("MT003", "Oakley", "OX8156", 350.00, 10, "Titanio")

        self.inventario.registrar_producto(lente1)
        self.inventario.registrar_producto(lente2)
        self.inventario.registrar_producto(lente3)
        self.inventario.registrar_producto(lente4)
        self.inventario.registrar_producto(montura1)
        self.inventario.registrar_producto(montura2)
        self.inventario.registrar_producto(montura3)

        self.menu()

    def limpiar_pantalla(self):
        os.system('cls')

    def menu(self):
        self.limpiar_pantalla()

        print("##########################################")
        print("# Tu Ojo - Sistema de gestion de opticas #")
        print("##########################################")
        print("")
        print("1.- Agenda")
        print("2.- Inventario")
        print("3.- Personal")
        print("4.- Ventas")
        print("")

        # try:
        opcion = int(input("Elige una opcion > "))

        if opcion > 0 and opcion < 5:
            
            if opcion == 1:
                self.opcionAgenda()

            elif opcion == 2:
                self.opcionInventario()

            elif opcion == 3:
                self.opcionPersonal()

            elif opcion == 4:
                pass

            else:
                input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
                self.menu()

        else:
            input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
            self.menu()

        # except Exception as e:
        #     input("Ingresaste una opcion incorrecta. Presiona Enter para continuar")
        #     self.menu()

    def opcionAgenda(self):
        self.limpiar_pantalla()
        print("##########################################")
        print("#            Tu Ojo - Agenda             #")
        print("##########################################")
        print("")
        print("1.- Ver agenda")
        print("2.- Agendar cita")
        print("3.- Generar reporte")
        print("4.- Salir")
        print("")

        # try:
        opcion = int(input("Elige una opcion > "))

        if opcion > 0 and opcion < 5:
            
            if opcion == 1:
                print(self.agenda.citas)
                self.agenda.ver_agenda()
                input("\nPresionar enter para regresar.")
                self.opcionAgenda()

            elif opcion == 2:
                dni_paciente = input("Ingresa el dni del paciente > ")

                paciente_encontrado = None
                paciente_creado = None

                for paciente in self.pacientes:
                    if(paciente.dni == dni_paciente):
                        paciente_encontrado = paciente

                if(paciente_encontrado != None):
                    print(f"\nSe ha encontrado al paciente con DNI {dni_paciente}\n")
                
                else:
                    nombre_paciente = input("Ingresa el nombre del paciente > ")
                    apellido_paciente = input("Ingresa el apellido del paciente > ")
                    telefono_paciente = input("Ingresa el telefono del paciente > ")
                    direccion_paciente = input("Ingresa el direccion del paciente > ")

                    paciente_creado = Paciente(dni_paciente, nombre_paciente, apellido_paciente, telefono_paciente, direccion_paciente)

                    self.pacientes.append(paciente_creado)

                dni_optometrista = input("Ingresa el dni del optometrista > ")

                optometrista_encontrado = None
                optometrista_creado = None

                for optometrista in self.optometristas:
                    if(optometrista.dni == dni_optometrista):
                        optometrista_encontrado = optometrista

                if(optometrista_encontrado != None):
                    print(f"\nSe ha encontrado al optometrista con DNI { dni_optometrista }\n")
                
                else:
                    nombre_optometrista = input("Ingresa el nombre del optometrista > ")
                    apellido_optometrista = input("Ingresa el apellido del optometrista > ")
                    telefono_optometrista = input("Ingresa el telefono del optometrista > ")
                    direccion_optometrista = input("Ingresa el direccion del optometrista > ")
                    id_medico = input("Ingresa el id del medico > ")
                    especialidad_optometrista = input("Ingresa el direccion del optometrista > ")

                    optometrista_creado = Optometrista(dni_optometrista, nombre_optometrista, apellido_optometrista, telefono_optometrista, direccion_optometrista, id_medico, especialidad_optometrista)

                    self.optometristas.append(optometrista_creado)

                cita = Cita( (paciente_encontrado if paciente_encontrado != None else paciente_creado), (optometrista_creado if optometrista_encontrado == None else optometrista_encontrado), datetime.now().strftime("%Y-%m-%d %H:%M"))

                self.agenda.agendar_cita(cita)

                cita.confirmar()                    

                input("Se ha generado la cita!. Presiona Enter para continuar")
                self.opcionAgenda()

            elif opcion == 3:
                self.agenda.generar_reporte()
                input("Se ha generado el reporte!. Presiona Enter para continuar")
                self.opcionAgenda()
            
            elif opcion == 4:
                self.menu()

            else:
                input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
                self.opcionAgenda()

        else:
            input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
            self.opcionAgenda()

        # except Exception as e:
        #     print(e.)
        #     input("Ingresaste una opcion incorrecta. Presiona Enter para continuar")
        #     self.opcionAgenda()


    def opcionInventario(self):
        self.limpiar_pantalla()
        print("##########################################")
        print("#          Tu Ojo - Inventario           #")
        print("##########################################")
        print("")
        print("1.- Registrar producto")
        print("2.- Buscar producto")
        print("3.- Actualizar stock")
        print("4.- Generar reporte de stock")
        print("5.- Ver Stock")
        print("6.- Salir")
        print("")

        # try:
        opcion = int(input("Elige una opcion > "))

        if opcion > 0 and opcion < 7:
            
            if opcion == 1:
                tipo_registro = input("Que producto registraras? (lente o montura) > ")
                
                if tipo_registro == "lente":
                    sku = input("Ingresa SKU > ")
                    marca = input("Ingresa marca > ")
                    modelo = input("Ingresa modelo > ")
                    precio = float(input("Ingresa precio > "))
                    cantidad = int(input("Ingresa cantidad > "))
                    tipo = input("Ingresa tipo > ")

                    nuevo_lente = Lente(sku, marca, modelo, precio, cantidad, tipo)

                    self.inventario.registrar_producto(nuevo_lente)

                    input(f"Se ha registrado el producto {sku}. Presiona Enter para continuar")

                    self.opcionInventario()

                else:
                    sku = input("Ingresa SKU > ")
                    marca = input("Ingresa marca > ")
                    modelo = input("Ingresa modelo > ")
                    precio = float(input("Ingresa precio > "))
                    cantidad = int(input("Ingresa cantidad > "))
                    material = input("Ingresa materialo > ")

                    nueva_montura = Montura(sku, marca, modelo, precio, cantidad, material)

                    self.inventario.registrar_producto(nueva_montura)

                    input(f"Se ha registrado el producto {sku}. Presiona Enter para continuar")

                    self.opcionInventario()

            if opcion == 2:
                sku = input("Ingresa SKU > ")

                producto_encontrado = self.inventario.buscar_producto(sku)

                if producto_encontrado != None:
                    print(producto_encontrado.ver_detalle())
                else:
                    print("No se han encontrado el producto")

                input("Presiona Enter para continuar")

                self.opcionInventario()

            if opcion == 3:
                sku = input("Ingresa SKU > ")
                cantidad = input("Ingresa la nueva cantidad > ")

                estado_actualizar = self.inventario.actualizar_stock(sku, cantidad)

                if estado_actualizar:
                    print(f"Se ha actualizado correctamente el stock del producto {sku}")
                else:
                    print("No se ha podido actualizar el stock")

                input("Presiona Enter para continuar")

                self.opcionInventario()

            if opcion == 4:
                self.inventario.generar_reporte_stock()
                input("Presiona Enter para continuar")

                self.opcionInventario()

            elif opcion == 5:
                if len(self.inventario.productos) == 0:
                    print("\nNo hay productos\n")
                else:
                    for producto in self.inventario.productos:
                        print(producto.ver_detalle())

                input(f"Se listaron los productos. Presiona Enter para continuar")

                self.opcionInventario()

            elif opcion == 6:
                self.menu()

            else:
                input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
                self.opcionInventario()

        else:
            input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
            self.opcionInventario()


    def opcionPersonal(self):
        print("Personal")

        for personal in self.optometristas:
            print(personal)
            print("\n")

        input(f"Presiona Enter para continuar")

        self.menu()

    def ventas(self):
        pass

if __name__ == '__main__':
    Main()