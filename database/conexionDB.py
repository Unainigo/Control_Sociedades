import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.dbModels import User, Producto, Compra, Mesas, Reservas, Actividades

class db:
    # Constructor de la clase con los datos que va a ir utilizando
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = None
        self.session = None

    # Función que realiza la conexión a la base de datos
    def connect(self):
        try:
            connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            self.engine = create_engine(connection_string)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            print("Conexión a la base de datos exitosa.")
        except Exception as e:
            self.engine = None
            self.session = None
            print(f"Error al conectar a la base de datos: {e}")
    #Función para desconectarnos de la base de datos
    def disconnect(self):
        if self.session:
            self.session.close()
        if self.engine:
            self.engine.dispose()
            print("Desconexión de la base de datos exitosa.")
        else:
            print("No hay una conexión activa para desconectar.")

    # Función para validar el usuario y contraseña ingresados por el usuario
    def validate_user(self, user, password):
        this_user = self.session.query(User).filter_by(email=user).first()
        if this_user and bcrypt.checkpw(password.encode('utf-8'), this_user.password.encode('utf-8')):
            return "Usuario valido"
        else:
            return "Usuario no valido"
    #Función para crear un nuevo usuario en la base de datos
    def create_user(self, user, password):
        this_user = self.session.query(User).filter_by(email=user).first()
        if this_user:
            print("El usuario ya existe. Por favor elige otro email.")
        else:
            new_user = User(email=user, password=password)
            self.session.add(new_user)
            self.session.commit()
            print("Usuario creado exitosamente.")