class LoginComando:
    """
    Comando para que un usuario inicie sesión.
    """
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
class LogoutComando:
    """
    Comando para que un usuario cierre sesión (opcional).
    """
    def __init__(self, user_id: int):
        self.user_id = user_id
