# Representa una venta concreta (producto, cantidad, total, fecha) 
from datetime import datetime
import csv
from Producto import Producto
from Usuario import Usuario
class Venta:
    def __init__(self, producto: Producto, cantidad: int, usuario: Usuario):
        self.producto = producto
        self.cantidad = cantidad
        self.usuario = usuario
        self.total = producto.precio * cantidad
        self.fecha = datetime.now()
        producto.cantidad -= cantidad

    def __str__(self):
        return f"Venta de {self.cantidad} unidades de {self.producto.nombreProducto} a {self.usuario.nombre} por un total de {self.total} el {self.fecha}"
    
    def guardar_en_csv(self, archivo='ventas.csv'):
        with open(archivo, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                self.fecha.strftime('%Y-%m-%d %H:%M:%S'),
                self.usuario.nombre,
                self.producto.nombreProducto,
                self.cantidad,
                self.total
            ])
# Aquí es donde se manipulan los objetos tipo PRODUCTO, para realizar ventas