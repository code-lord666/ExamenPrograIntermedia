# Representa al usuario que realiza las ventas

class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Comprado por {self.nombre} con el id {self.id}"