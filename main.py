from objetos.Tienda import Tienda
from objetos.Producto import Producto
from objetos.Usuario import Usuario
from objetos.Venta import Venta
from objetos.Gestor import Gestor
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


def imprimir_productos(tienda):
    print("\n📦 Productos")
    print("-" * 60)
    #print(f"{'ID':<5}{'Nombre':<30}{'Precio':>10}{'Stock':>10}")

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


# =============== Carga inicial / Guardado ===============

def cargar_datos(tienda, gestor):
    # Productos
    try:
        for p in gestor.cargar_productos():
            tienda.agregar_producto(p)
    except Exception as e:
        print(f"⚠️ No se cargaron productos: {e}")

    # Usuarios
    try:
        for u in gestor.cargar_usuarios():
            tienda.registrar_usuario(u)
    except Exception as e:
        print(f"⚠️ No se cargaron usuarios: {e}")

    # Ventas
    try:
        for v in gestor.cargar_ventas():
            tienda.registrar_venta(v)
    except Exception as e:
        print(f"⚠️ No se cargaron ventas: {e}")

def guardar_datos(tienda, gestor):
    try:
        gestor.guardar_productos(tienda.listar_productos())
        gestor.guardar_usuarios(tienda.listar_usuarios())
        gestor.guardar_ventas(tienda.listar_ventas())
        print("💾 Datos guardados.")
    except Exception as e:
        print(f"⚠️ Error al guardar: {e}")


# ================== Acciones del menú ===================

def accion_listar_productos(tienda):
    imprimir_productos(tienda)

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

def accion_listar_usuarios(tienda):
    imprimir_usuarios(tienda)

def accion_realizar_venta(tienda):
    usuario = tienda.verificar_usuario(int(input("Ingrese el Id del usuario")))
    producto = tienda.verificar_producto(int(input("Ingrese el Id del producto")))
    if not usuario:
        print("❌ No hay usuarios registrados con ese ID.")
        return
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
    

    

def accion_listar_ventas(tienda):
    imprimir_ventas(tienda)


# ===================== Menú principal ===================

def menu():
    tienda = Tienda()
    gestor = Gestor()
    cargar_datos(tienda, gestor)

    # --- Datos de prueba ---
    if not tienda.listar_usuarios():
        usuario_prueba = Usuario(1, "UsuarioPrueba")
        tienda.agregar_usuario(usuario_prueba)
    if not tienda.listar_productos():
        producto_prueba = Producto("ProductoPrueba", 1000, 10)
        tienda.agregar_producto(producto_prueba)

    while True:
        print("""
=========== MADRIGUERA ERRANTE ===========
1) Listar productos
2) Agregar producto
3) Registrar usuario
4) Listar usuarios
5) Realizar venta
6) Listar ventas
7) Guardar cambios
0) Guardar y salir
==========================================
""")
        op = pedir_int("Elige una opción: ", minimo=0, maximo=7)

        if op == 1:
            accion_listar_productos(tienda)
        elif op == 2:
            accion_agregar_producto(tienda)
        elif op == 3:
            accion_registrar_usuario(tienda)
        elif op == 4:
            accion_listar_usuarios(tienda)
        elif op == 5:
            accion_realizar_venta(tienda)
        elif op == 6:
            accion_listar_ventas(tienda)
        elif op == 7:
            guardar_datos(tienda, gestor)
        elif op == 0:
            guardar_datos(tienda, gestor)
            print("¡Gracias por usar la tienda!")
            break


if __name__ == "__main__":
    menu()