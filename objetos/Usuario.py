# Representa al usuario que realiza las ventas

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.nombre = nombre
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Usuario {self.nombre} (ID: {self.id_usuario})"