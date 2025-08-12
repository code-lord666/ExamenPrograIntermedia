# Representa una venta concreta (producto, cantidad, total, fecha) 
from datetime import datetime
from .Producto import Producto
from .Usuario import Usuario

class Venta:
    def __init__(self, producto: Producto, cantidad: int, usuario: Usuario):
        self.producto = producto
        self.cantidad = cantidad
        self.usuario = usuario
        self.total = producto.precio * cantidad
        self.fecha = datetime.now()
        producto.cantidad -= cantidad

    def __str__(self):
        fecha_formateada = self.fecha.strftime('%Y-%m-%d | %H:%M:%S')
        return f"Venta de {self.cantidad} unidades de {self.producto.nombre_Producto} a {self.usuario.nombre} por un total de {self.total} el {fecha_formateada}"
    
    
# Aquí es donde se manipulan los objetos tipo PRODUCTO, para realizar ventas