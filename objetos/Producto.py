# Representa los productos disponibles
class Producto:
    contador=100
    def __init__(self, nombre_Producto, precio, cantidad):
        self.id_producto = Producto.contador
        Producto.contador += 1
        self.nombre_Producto = nombre_Producto
        self.precio = precio
        self.cantidad = cantidad 
    
    def __str__(self):
        return f"\nId: {self.id_producto} \nProducto: {self.nombre_Producto} \nPrecio: {self.precio}   \nStock: {self.cantidad}"