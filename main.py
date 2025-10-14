class Main:
    def __init__(self):
        self.menu()

    def menu(self):
        print("##########################################")
        print("# Tu Ojo - Sistema de gestion de opticas #")
        print("##########################################")
        print("")
        print("1.- Agenda")
        print("2.- Inventario")
        print("3.- Personal")
        print("4.- Ventas")
        print("")

        try:
            opcion = int(input("Elige una opcion > "))

            if opcion > 0 and opcion < 5:
                
                if opcion == 1:
                    self.agenda()

                elif opcion == 2:
                    pass

                elif opcion == 3:
                    pass

                elif opcion == 4:
                    pass

                else:
                    input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
                    self.menu()

            else:
                input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
                self.menu()

        except Exception as e:
            input("Ingresaste una opcion incorrecta. Presiona Enter para continuar")
            self.menu()


    def agenda(self):
        print("##########################################")
        print("# Tu Ojo - Sistema de gestion de opticas #")
        print("##########################################")
        print("")
        print("1.- Agenda")
        print("2.- Inventario")
        print("3.- Personal")
        print("4.- Ventas")
        print("")

        try:
            opcion = int(input("Elige una opcion > "))

            if opcion > 0 and opcion < 5:
                
                if opcion == 1:
                    self.agenda()

                elif opcion == 2:
                    pass

                elif opcion == 3:
                    pass

                elif opcion == 4:
                    pass

                else:
                    input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
                    self.agenda()

            else:
                input("Has ingresado una opcion incorrecta. Presiona Enter para continuar")
                self.agenda()
        except Exception as e:
            input("Ingresaste una opcion incorrecta. Presiona Enter para continuar")
            self.agenda()

if __name__ == '__main__':
    Main()