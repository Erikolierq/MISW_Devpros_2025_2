class UsernameVO:
    """
    Ejemplo de un objeto de valor para el nombre de usuario.
    """
    def __init__(self, value: str):
        if not value or len(value.strip()) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
        self.value = value

    def __eq__(self, other):
        return isinstance(other, UsernameVO) and self.value == other.value

    def __str__(self):
        return self.value
