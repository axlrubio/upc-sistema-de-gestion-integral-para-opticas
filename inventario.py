class Inventario:
    def __init__(self):
        self.productos = []
    
    def registrar_producto(self, producto):
        # Verificar si el producto ya existe
        for p in self.productos:
            if p.sku == producto.sku:
                print("Error: El producto ya existe en el inventario")
                return False
        
        self.productos.append(producto)
        print(f"Producto {producto.sku} registrado exitosamente")
        return True
    
    def buscar_producto(self, sku):
        for producto in self.productos:
            if producto.sku == sku:
                return producto
        print(f"Producto con SKU {sku} no encontrado")
        return None
    
    def listar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos en el inventario")
            return
        
        print("\n========== LISTA DE PRODUCTOS ==========")
        print(f"Total de productos: {len(self.productos)}\n")
        
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. SKU: {producto.sku}")
            print(f"   Marca: {producto.marca}")
            print(f"   Modelo: {producto.modelo}")
            print(f"   Precio: S/ {producto.precio:.2f}")
            print(f"   Stock: {producto.stock} unidades")
            print(f"   Tipo: {producto.__class__.__name__}")
            print("-" * 40)
    
    def modificar_producto(self, sku):
        producto = self.buscar_producto(sku)
        if producto is None:
            return False
        
        print("\nIngrese los nuevos datos (presione Enter para mantener el actual):")
        
        nueva_marca = input(f"Marca actual ({producto.marca}): ")
        if nueva_marca.strip():
            producto.marca = nueva_marca
        
        nuevo_modelo = input(f"Modelo actual ({producto.modelo}): ")
        if nuevo_modelo.strip():
            producto.modelo = nuevo_modelo
        
        nuevo_precio = input(f"Precio actual ({producto.precio}): ")
        if nuevo_precio.strip():
            try:
                producto.precio = float(nuevo_precio)
            except ValueError:
                print("Precio inválido, se mantiene el anterior")
        
        nuevo_stock = input(f"Stock actual ({producto.stock}): ")
        if nuevo_stock.strip():
            try:
                producto.stock = int(nuevo_stock)
            except ValueError:
                print("Stock inválido, se mantiene el anterior")
        
        print("Producto modificado exitosamente")
        return True
    
    def actualizar_stock(self, sku, cantidad):
        producto = self.buscar_producto(sku)
        if producto is None:
            return False
        
        if producto.stock < cantidad:
            print(f"Error: Stock insuficiente. Disponible: {producto.stock}")
            return False
        
        producto.stock -= cantidad
        print(f"Stock actualizado. Nuevo stock de {sku}: {producto.stock}")
        return True
    
    def generar_reporte_stock(self):
        if len(self.productos) == 0:
            print("No hay productos para generar reporte")
            return
        
        print("\n========== REPORTE DE STOCK ==========")
        productos_bajo_stock = []
        
        for producto in self.productos:
            if producto.stock < 5:
                productos_bajo_stock.append(producto)
                print(f"⚠️  ALERTA - {producto.sku}: {producto.stock} unidades (Stock bajo)")
            else:
                print(f"✓ {producto.sku}: {producto.stock} unidades")
        
        print(f"\nProductos con stock bajo: {len(productos_bajo_stock)}")
        print("=" * 40)
