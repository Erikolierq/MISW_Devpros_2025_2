class ObtenerUsuarioPorCredencialesQuery:
    """
    Query para obtener un usuario por su nombre y contraseña.
    """
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
