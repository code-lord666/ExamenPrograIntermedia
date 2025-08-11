# Representa los productos disponibles
class Producto:
    def __init__(self, idproducto, nombreProducto, precio, cantidad):
        self.idproducto = idproducto
        self.nombreProducto = nombreProducto
        self.precio = precio
        self.cantidad = cantidad
    def __str__(self):
        return f"Producto :{self.nombre} Id :{self.id}"