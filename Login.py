from Conexion import obtener_conexion
from rich.console import Console
#LOGIIN
#INICIO DE USUARIOS
def iniciar_sesion():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    print("===== INICIO DE SESIÓN =====")
#BUCLE WHILE
    while True:
#SE PIDEN DATOS
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
#SE COMPARA LOS DATOS
        if resultado:
            rol = resultado[0]
            print(f"\n✅ Bienvenido {usuario}")
            print(f"🔐 Rol: {rol}\n")
            cursor.close()
            conexion.close()
            return rol
#SI EXISTE ALGUN ERROR
        else:
            print("\n❌ Usuario o contraseña incorrectos.\n")