from Conexion import obtener_conexion
from rich.console import Console
def iniciar_sesion():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    print("===== INICIO DE SESIÓN =====")

    while True:

        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        sql = """
        SELECT rol
        FROM usuarios
        WHERE usuario = %s AND contraseña = %s
        """

        valores = (usuario, contraseña)

        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        if resultado:

            rol = resultado[0]

            print(f"\n✅ Bienvenido {usuario}")
            print(f"🔐 Rol: {rol}\n")

            cursor.close()
            conexion.close()

            return rol

        else:

            print("\n❌ Usuario o contraseña incorrectos.\n")