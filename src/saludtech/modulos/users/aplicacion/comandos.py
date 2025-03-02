class CrearUsuarioComando:
    """
    Comando para crear un usuario nuevo en el sistema.
    """
    def __init__(self, username: str, password: str, role: int):
        self.username = username
        self.password = password
        self.role = role
class ActualizarUsuarioComando:
    """
    Comando para actualizar datos del usuario, por ejemplo la contraseña o el rol.
    """
    def __init__(self, user_id: int, password: str = None, role: int = None):
        self.user_id = user_id
        self.password = password
        self.role = role
