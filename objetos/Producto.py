# Representa los productos disponibles
class Producto:
    def __init__(self, nombre_Producto, precio, cantidad):
        self.id_producto =+ 100
        self.nombre_Producto = nombre_Producto
        self.precio = precio
        self.cantidad = cantidad #
    
    def __str__(self):
        return f"Producto :{self.nombre_Producto} Id :{self.id_producto}"