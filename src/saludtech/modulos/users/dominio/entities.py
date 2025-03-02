from dataclasses import dataclass

@dataclass
class User:
    """
    Entidad que representa a un usuario.
    """
    id: int
    username: str
    password: str   # En producción, almacenar la contraseña en forma segura (hash)
    role: int

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
            # Por seguridad, no se recomienda exponer password
        }

    def to_dto(self):
        """
        Convierte la entidad a un objeto DTO para persistir en la base de datos.
        """
        from modulos.users.infraestructura.dto import UserDTO
        return UserDTO(
            id=self.id,
            username=self.username,
            password=self.password,
            role=self.role
        )
