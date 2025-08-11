# Orquestador general, aqui se manejan PRODUCTOS, USUARIOS, VENTAS

from Producto import Producto
from Usuario import Usuario
from Venta import Venta

class Tienda:
    def __init__(self):
        self.productos = []
        self.usuarios = []
        self.ventas = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def verificar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if (usuario.id_usuario == id_usuario):
                return usuario
            return False
    
    def verificar_producto(self, id_producto):
        if (id_producto != ""):
            for producto in self.productos:
                if (producto.id_producto == id_producto):
                    return producto
                return False


    #def vender_producto (self, id_producto, id_usuario): 

        
    




# Aquí se guardan los productos existentes, las ventas realizadas y los usuarios registrados