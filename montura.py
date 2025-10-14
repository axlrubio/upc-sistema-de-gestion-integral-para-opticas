from producto import Producto

class Montura(Producto):
    def __init__(self, sku, marca, modelo, precio, stock, material):
        super().__init__(sku, marca, modelo, precio, stock)

        self.material = material

    def ver_detalle(self):
        detalle = super().ver_detalle()

        detalle += f"Material: {self.material}\n"

        return detalle