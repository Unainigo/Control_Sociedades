import uuid

class Usuario:
    def __init__(self, id_usuario, nombre, correo, contraseña):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña