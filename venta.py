from datetime import datetime
from typing import List
from producto import Producto
from paciente import Paciente

class Venta:
    def __init__(self, id: str, fecha: str, productos: List[Producto], paciente: Paciente, pagos: List[float] = []):
        self.id = id
        self.fecha = fecha
        self.productos = productos
        self.paciente = paciente
        self.pagos = pagos
        self.total = self.calcular_total()  # Se calcula automáticamente

    def calcular_total(self) -> float:
        """Calcula el total de la venta sumando los precios de los productos."""
        return sum(p.precio for p in self.productos)

    def registrar_venta(self):
        """Registra la venta, disminuye el stock y muestra un resumen."""
        for producto in self.productos:
            producto.disminuir_stock()
        print(f"✅ Venta {self.id} registrada para {self.paciente.nombre_completo}.")
        print(f"Total: S/. {self.total:.2f}")

    def entregar_comprobante(self):
        """Devuelve una cadena con el comprobante de la venta."""
        comprobante = f"\n=== COMPROBANTE DE VENTA ===\n"
        comprobante += f"ID Venta: {self.id}\n"
        comprobante += f"Fecha: {self.fecha}\n"
        comprobante += f"Cliente: {self.paciente.nombre_completo}\n"
        comprobante += f"---------------------------------\n"

        for producto in self.productos:
            comprobante += f"{producto.marca} {producto.modelo} - S/. {producto.precio:.2f}\n"

        comprobante += f"---------------------------------\n"
        comprobante += f"TOTAL: S/. {self.total:.2f}\n"

        if self.pagos:
            comprobante += f"Pagos realizados: {len(self.pagos)}\n"
            comprobante += f"Total pagado: S/. {sum(self.pagos):.2f}\n"
            comprobante += f"Saldo: S/. {self.total - sum(self.pagos):.2f}\n"

        comprobante += f"==============================\n"
        return comprobante
