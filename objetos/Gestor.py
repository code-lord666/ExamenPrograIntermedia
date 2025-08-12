# Guarda y carga datos desde/para CSV usando pandas y matplotlib

import csv
from .Venta import Venta

class Gestor:
    def guardar_en_csv(self, venta: 'Venta', archivo='ventas.csv'):
        with open(archivo, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([venta])
