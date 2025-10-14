from producto import Producto

class Lente(Producto):
    def __init__(self, sku, marca, modelo, precio, stock):
        super().__init__(sku, marca, modelo, precio, stock)
        self.tipo