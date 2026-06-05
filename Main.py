from Login import iniciar_sesion
from Ferreteria import menu_administrador, menu_usuario
from rich.console import Console
print("🔧 Bienvenido al Sistema de Gestión de Ferretería\n")

#SE CREA UN MAIN Y SE LOGEA EL USUARIO
rol = iniciar_sesion()

if rol == "administrador":

    menu_administrador()

elif rol == "usuario":

    menu_usuario()

else:

    print("❌ Rol no reconocido.")