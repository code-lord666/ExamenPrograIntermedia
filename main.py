from objetos.Tienda import Tienda
from objetos.Producto import Producto
from objetos.Usuario import Usuario
from objetos.Venta import Venta
from objetos.Gestor import Gestor
from datetime import datetime, timedelta
import random

## ================== Precargar datos ===================
def recargardatos(tienda):
    # Agregar productos de prueba
    for i in range(1, 6):
        if not tienda.listar_productos():
            producto_prueba = Producto(f"ProductoPrueba{i}", (i*1000), (10+i))
            tienda.agregar_producto(producto_prueba)

    # Agregar usuarios de prueba
    for i in range(1, 6):
        if not tienda.listar_usuarios():
            usuario_prueba = Usuario(i, f"UsuarioPrueba{i}")
            tienda.agregar_usuario(usuario_prueba)

    # Crear ventas de prueba usando los productos y usuarios agregados
    productos = tienda.productos
    usuarios = tienda.usuarios
    for i in range(min(len(productos), len(usuarios))):
        usuario = usuarios[i]
        producto = productos[i]
        cantidad = 1 + i  # Cantidad de prueba
        dias_atras = random.randint(0, 29)
        segundos = random.randint(0, 86399)
        fecha_random = datetime.now() - timedelta(days=dias_atras, seconds=segundos)
        venta = Venta(producto, cantidad, usuario, fecha_random)
        tienda.agregar_venta(venta)


#------------------- Funciones de entrada --------------------------
def pedir_int(msg, minimo=None, maximo=None):
    while True:
        try:
            v = int(input(msg))
            if minimo is not None and v < minimo:
                print(f"Debe ser ≥ {minimo}")
                continue
            if maximo is not None and v > maximo:
                print(f"Debe ser ≤ {maximo}")
                continue
            return v
        except ValueError:
            print("Ingresa un número entero válido.")

def pedir_float(msg, minimo=None):
    while True:
        try:
            v = float(input(msg))
            if minimo is not None and v < minimo:
                print(f"Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("Ingresa un número válido (usa punto decimal si hace falta).")

def pedir_str(msg, obligatorio=False):
    while True:
        s = input(msg).strip()
        if obligatorio and not s:
            print("No puede estar vacío.")
            continue
        return s

# ================== Impresiones =========================

def imprimir_productos(tienda):
    print("\n📦 Productos")
    print("-" * 60)
    tienda.listar_productos()
    print("-" * 60)

def imprimir_usuarios(tienda):
    print("\n👤 Usuarios")
    print("-" * 40)
    tienda.listar_usuarios()
    print("-" * 40)

def imprimir_ventas(tienda):
    print("\n🧾 Ventas")
    print("-" * 80)
    tienda.listar_ventas()
    print("-" * 80)

# ================== Acciones del menú ===================

def accion_agregar_producto(tienda):
    nombre = pedir_str("Nombre del producto: ", obligatorio=True)
    precio = pedir_float("Precio: ", minimo=0)
    stock  = pedir_int("Stock: ", minimo=0)
    p = Producto(nombre, precio, stock)
    tienda.agregar_producto(p)
    print("✅ Producto agregado.")

def accion_registrar_usuario(tienda):
    nombre = pedir_str("Nombre del usuario: ", obligatorio=True)
    Id = pedir_int("ID del usuario: ")
    u = Usuario(Id, nombre)
    tienda.agregar_usuario(u)
    print("✅ Usuario registrado.")

def accion_realizar_venta(tienda):
    usuario = tienda.verificar_usuario(pedir_int("Ingrese el ID del usuario: "))
    if not usuario:
        print("❌ No hay usuarios registrados con ese ID.")
        return    
    producto = tienda.verificar_producto(pedir_int("Ingrese el ID del producto: "))
    if not producto:
        print("❌ No hay productos disponibles.")
        return
    
    if producto and usuario:
        cantidad = pedir_int("Cantidad: ")
        if cantidad > 0 and cantidad <= producto.cantidad:
            venta = Venta(producto, cantidad, usuario)
            tienda.agregar_venta(venta)
            print(f"✅ Venta realizada.\n {venta}")
        else:
            print("❌ Cantidad inválida.")
            return

# ===================== Menú principal ===================

def menu():
    tienda = Tienda()
    gestor = Gestor()

    while True:
        print("""
=========== MADRIGUERA ERRANTE ===========
1) Listar productos
2) Agregar producto
3) Registrar usuario
4) Listar usuarios
5) Realizar venta
6) Listar ventas
7) Guardar ventas en CSV
8) Mostrar estadísticas
9) Recargar datos
0) Salir
==========================================
""")
        op = pedir_int("Elige una opción: ", minimo=0, maximo=9)

        if op == 1:
            imprimir_productos(tienda)
        elif op == 2:
            accion_agregar_producto(tienda)
        elif op == 3:
            accion_registrar_usuario(tienda)
        elif op == 4:
            imprimir_usuarios(tienda)   
        elif op == 5:
            accion_realizar_venta(tienda)
        elif op == 6:
            imprimir_ventas(tienda)
        elif op == 7:
            gestor.guardar_csv(tienda)
        elif op == 8:
            gestor.mostrar_estadisticas_csv()
        elif op == 9:
            recargardatos(tienda)
        elif op == 0:
            print("¡Gracias por usar la tienda!")
            break
        
menu()#Inicio del menú
