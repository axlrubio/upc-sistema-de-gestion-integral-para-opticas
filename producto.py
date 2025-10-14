class Producto:
    def __init__(self, sku, marca, modelo, precio, stock):
        self.sku = sku
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.stock = stock

    def incrementar_stock(self):
        self.stock += 1

    def disminuir_stock(self):
        self.stock -= 1

    def ver_detalle(self):
        detalle = ""

        detalle += f"SKU: {self.sku}\n"
        detalle += f"Marca: {self.marca}\n"
        detalle += f"Modelo: {self.modelo}\n"
        detalle += f"Precio: s./ {self.precio}\n"
        detalle += f"Stock: {self.stock}\n"

        return detalle
        