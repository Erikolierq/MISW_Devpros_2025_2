from dataclasses import dataclass

@dataclass
class AuthUser:
    """
    Entidad que representa a un usuario para autenticación.
    """
    id: int
    username: str
    password: str
    role: int

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
           
        }
