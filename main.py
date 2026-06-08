import database.conexionDB
from database.dbModels import Producto, Compra, Mesas, User, Reservas, Actividades
import bcrypt

def run():
    pass
database = database.conexionDB.db(
    user="postgres",
    password="Huza2244",
    host="localhost",
    port="5432",
    database="Sociedades"
)
database.connect()
if database.engine is not None:
    # Crear tablas en orden de dependencias
    User.__table__.create(database.engine, checkfirst=True)
    Producto.__table__.create(database.engine, checkfirst=True)
    Compra.__table__.create(database.engine, checkfirst=True)
    Mesas.__table__.create(database.engine, checkfirst=True)
    Reservas.__table__.create(database.engine, checkfirst=True)
    Actividades.__table__.create(database.engine, checkfirst=True)
else:
    raise SystemExit("No se pudo conectar a la base de datos. Revisa el mensaje anterior.")

# Creamos un switch para elegir las acciones que queremos realizar
print("Bienvenido a la aplicación de finanzas personales")
action = 0
while action != 3:
    action = int(input("Que acción desea realizar: \n 1. Crear un nuevo usuario \n 2. Login \n 3. Salir \n"))
    match action:
        case 1:
            new_user = input(str("Introduzca el email: "))
            new_password = input(str("Introduzca la contraseña del nuevo usuario: "))
            # Hashear la contraseña antes de almacenarla
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            print(hashed_password)
            database.create_user(new_user, hashed_password)
        case 2:
            my_user = input(str("Introduzca el email: "))
            my_Password = input(str("Introduzca la contraseña: "))
            if database.validate_user(my_user, my_Password) == "Usuario valido":
                print("Login exitoso")
            else:
                print("Credenciales incorrectas")
        case 3:
            print("Saliendo de la aplicación...")
            database.disconnect()
            break
        case _:
            print("Opción no válida, por favor intente de nuevo.")