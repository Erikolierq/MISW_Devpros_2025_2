class RoleValue:
    """
    Objeto de valor para representar el rol de usuario.
    """
    def __init__(self, role_id: int):
        if role_id not in [1, 2]:  # Ajusta según lógica de negocio
            raise ValueError("Rol no válido para este sistema")
        self.role_id = role_id

    def __eq__(self, other):
        return isinstance(other, RoleValue) and self.role_id == other.role_id

    def __str__(self):
        return str(self.role_id)
