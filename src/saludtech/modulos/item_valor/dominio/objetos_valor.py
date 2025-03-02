class PatientName:
    """
    Ejemplo de objeto de valor que valida el nombre del paciente.
    """
    def __init__(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El nombre del paciente no puede estar vacío.")
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, PatientName):
            return False
        return self.value == other.value

    def __str__(self):
        return self.value


class ResultText:
    """
    Ejemplo de objeto de valor que valida el texto del resultado.
    """
    def __init__(self, value: str):
        if not isinstance(value, str) or len(value.strip()) < 3:
            raise ValueError("El resultado clínico debe tener al menos 3 caracteres.")
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, ResultText):
            return False
        return self.value == other.value

    def __str__(self):
        return self.value
