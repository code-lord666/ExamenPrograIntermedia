# Guarda y carga datos desde/para CSV usando pandas y matplotlib

import pandas as pd
import matplotlib.pyplot as plt


class Gestor:
    def __init__(self):
        pass

    def guardar_csv(self, tienda):    
        datos = []

        for v in tienda.ventas:
            datos.append({
                "Fecha": v.fecha.strftime('%Y-%m-%d'),
                "Hora": v.fecha.strftime('%H:%M:%S'),
                "Producto": v.producto.nombre_Producto,
                "Cantidad": v.cantidad,
                "Precio Unitario": v.producto.precio,
                "Total": v.total,
                "Usuario": v.usuario.nombre,
            })

        df = pd.DataFrame(datos)
        df.to_csv("ventas.csv", index=False, encoding="utf-8")
    
    
    def mostrar_estadisticas_csv(self):
        df = pd.read_csv("ventas.csv")

        # Ventas por día
        ventas_por_dia = df.groupby("Fecha")["Total"].sum()
        print("\n=" * 40)
        print("Ventas por día:\n")
        print(ventas_por_dia.reset_index().to_string(index=False, header=["Fecha", "Total"]))

        # Ingresos totales
        ingresos_totales = df["Total"].sum()
        print(f"\nIngresos totales: {ingresos_totales}")

        # Productos más vendidos (por cantidad)
        productos_mas_vendidos = df.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False)
        print("\nProductos más vendidos (por cantidad):")
        print(productos_mas_vendidos.reset_index().to_string(index=False, header=["Producto", "Cantidad"]))

        # Producto más vendido
        producto_mas_vendido = productos_mas_vendidos.idxmax()
        cantidad_vendida = productos_mas_vendidos.max()
        print(f"\nProducto más vendido: {producto_mas_vendido} ({cantidad_vendida} unidades)")
        print("=" * 40)        

        # Graficar estadísticas
        plt.figure(figsize=(12, 6))    
        ventas_por_dia.plot(kind="bar", title="Ingresos por día", color="skyblue")
        plt.ylabel("Ingresos")
        plt.xlabel("Fecha")
        plt.tight_layout()
        plt.show()

        productos_mas_vendidos.plot(kind="bar", title="Productos más vendidos", color="orange")
        plt.ylabel("Cantidad vendida")
        plt.xlabel("Producto")
        plt.tight_layout()
        plt.show()
    