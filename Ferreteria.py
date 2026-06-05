from Conexion import obtener_conexion
from rich.console import Console
#SE CREA EL METODO PARA MOSTRAR LOS PRODUCTOS
def mostrar_productos():
    #SE VERIFICAN CONEXIONES
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM productos")
    productos = cursor.fetchall()
    if len(productos) == 0:
        print("\n🔧 No hay productos registrados.\n")
    else:
        print("\n===== CATÁLOGO DE PRODUCTOS =====")
        for producto in productos:
            print(f"{producto[0]}. {producto[1]}")
        print()
    cursor.close()
    conexion.close()

#SE CREA EL METODO PARA AGREGAR PRODUCTOS
def agregar_producto():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    producto = input("Ingrese el nombre del producto: ").strip()
    #SE AGREGA EL PRODUCTO A LA DB
    if producto:
        sql = "INSERT INTO productos (nombre) VALUES (%s)"
        valores = (producto,)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"\n✅ Producto '{producto}' agregado correctamente.\n")
    else:
        print("\n⚠ No puede ingresar un producto vacío.\n")
    cursor.close()
    conexion.close()

#METODO PARA ELIMINAR ALGUN PRODUCTOS
def eliminar_producto():
    #SE VERIFICAN CONEXIONES
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    producto = input("Ingrese el nombre del producto a eliminar: ").strip()
    #SE ELIMINA EL PRODUCTO SI EXISTE EN TAL DB
    sql = "DELETE FROM productos WHERE nombre = %s"
    valores = (producto,)
    cursor.execute(sql, valores)
    conexion.commit()
    if cursor.rowcount > 0:
        print(f"\n🗑 Producto '{producto}' eliminado correctamente.\n")
    else:
        #POR SI EL PRODUCTO NO EXISTE
        print(f"\n⚠ El producto '{producto}' no existe.\n")
    cursor.close()
    conexion.close()

#SE CREA EL MENU DE ADMINISTRADOR
def menu_administrador():
    while True:
        print("===== MENÚ ADMINISTRADOR =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar catálogo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            eliminar_producto()

        elif opcion == "3":
            mostrar_productos()

        elif opcion == "4":

            print("\n👋 Gracias por usar el sistema.")
            break
        else:
            print("\n❌ Opción inválida.\n")

#SE CREA EL MENU DE USUARIO
def menu_usuario():
    while True:
        print("===== MENÚ USUARIO =====")
        print("1. Mostrar catálogo")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            print("\n👋 Gracias por usar el sistema.")
            break
        else:
            print("\n❌ Opción inválida.\n")