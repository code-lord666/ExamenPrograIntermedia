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


def imprimir_productos(productos):
    print("\n📦 Productos")
    print("-" * 60)
    print(f"{'ID':<5}{'Nombre':<30}{'Precio':>10}{'Stock':>10}")
    print("-" * 60)
    if not productos:
        print("(sin productos)")
    else:
        for i, p in enumerate(productos, start=1):
            print(f"{i:<5}{p.nombre:<30}{p.precio:>10.2f}{p.stock:>10}")
    print("-" * 60)

def imprimir_usuarios(usuarios):
    print("\n👤 Usuarios")
    print("-" * 40)
    print(f"{'ID':<5}{'Nombre':<22}{'Rol':<10}")
    print("-" * 40)
    if not usuarios:
        print("(sin usuarios)")
    else:
        for i, u in enumerate(usuarios, start=1):
            print(f"{i:<5}{u.nombre:<22}{u.rol:<10}")
    print("-" * 40)

def imprimir_ventas(ventas):
    print("\n🧾 Ventas")
    print("-" * 80)
    print(f"{'ID':<5}{'Usuario':<18}{'Producto':<28}{'Cant':>6}{'Total':>12}")
    print("-" * 80)
    if not ventas:
        print("(sin ventas)")
    else:
        for i, v in enumerate(ventas, start=1):
            print(f"{i:<5}{v.usuario.nombre:<18}{v.producto.nombre:<28}{v.cantidad:>6}{v.total:>12.2f}")
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
    imprimir_productos(tienda.listar_productos())

def accion_agregar_producto(tienda):
    nombre = pedir_str("Nombre del producto: ", obligatorio=True)
    precio = pedir_float("Precio: ", minimo=0)
    stock  = pedir_int("Stock: ", minimo=0)
    p = Producto(nombre, precio, stock)
    tienda.agregar_producto(p)
    print("✅ Producto agregado.")

def accion_registrar_usuario(tienda):
    nombre = pedir_str("Nombre del usuario: ", obligatorio=True)
    rol = pedir_str("Rol (admin/cliente): ") or "cliente"
    u = Usuario(nombre, rol)
    tienda.registrar_usuario(u)
    print("✅ Usuario registrado.")

def accion_listar_usuarios(tienda):
    imprimir_usuarios(tienda.listar_usuarios())

def accion_realizar_venta(tienda):
    usuarios = tienda.listar_usuarios()
    productos = tienda.listar_productos()

    if not usuarios:
        print("❌ No hay usuarios registrados.")
        return
    if not productos:
        print("❌ No hay productos disponibles.")
        return

    imprimir_usuarios(usuarios)
    i_u = pedir_int("Seleccione ID de usuario: ", minimo=1, maximo=len(usuarios))
    usuario = usuarios[i_u - 1]

    imprimir_productos(productos)
    i_p = pedir_int("Seleccione ID de producto: ", minimo=1, maximo=len(productos))
    producto = productos[i_p - 1]

    cantidad = pedir_int("Cantidad: ", minimo=1)

    if producto.stock < cantidad:
        print(f"❌ Stock insuficiente. Disponible: {producto.stock}")
        return

    venta = Venta(usuario, producto, cantidad)
    tienda.registrar_venta(venta)
    producto.stock -= cantidad  # descuento simple de stock

    print(f"✅ Venta realizada. Total: {venta.total:.2f}")

def accion_listar_ventas(tienda):
    imprimir_ventas(tienda.listar_ventas())


# ===================== Menú principal ===================

def menu():
    tienda = Tienda()
    gestor = Gestor()
    cargar_datos(tienda, gestor)

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