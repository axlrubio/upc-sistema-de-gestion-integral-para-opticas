from producto import Producto

class Lente(Producto):
    def __init__(self, sku, marca, modelo, precio, stock, tipo):
        super().__init__(sku, marca, modelo, precio, stock)
        self.tipo = tipo

    def ver_detalle(self):
        detalle = super().ver_detalle()

        detalle += f"Tipo: {self.tipo}\n"

        return detalle