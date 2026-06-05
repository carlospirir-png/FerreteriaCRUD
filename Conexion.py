import mysql.connector
from rich.console import Console
def obtener_conexion():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="Ferreteria_db"
    )
    return conexion