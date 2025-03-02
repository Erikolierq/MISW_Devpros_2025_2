class ObtenerPermisoQuery:
    """
    Query para obtener información de permisos según el rol de usuario.
    """
    def __init__(self, user_role: int):
        self.user_role = user_role
