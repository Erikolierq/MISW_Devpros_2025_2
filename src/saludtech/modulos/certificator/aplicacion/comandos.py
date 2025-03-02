class ValidarPermisoComando:
    """
    Comando para validar si un usuario tiene permiso para realizar cierta acción,
    como consultar o modificar un resultado clínico.
    """
    def __init__(self, user_role: int):
        self.user_role = user_role
