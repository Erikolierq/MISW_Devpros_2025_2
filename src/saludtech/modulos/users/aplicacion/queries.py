class ObtenerUsuarioQuery:
    """
    Query para obtener un usuario por su ID.
    """
    def __init__(self, user_id: int):
        self.user_id = user_id

class ListarUsuariosQuery:
    """
    Query para listar todos los usuarios.
    """
    def __init__(self):
        pass
