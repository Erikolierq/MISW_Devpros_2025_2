from modulos.auth.dominio.entities import AuthUser
from modulos.auth.infraestructura.dto import AuthUserDTO

class AuthRepository:
    def __init__(self, session):
        self.session = session

    def get_by_credentials(self, username: str, password: str):
        """
        Retorna el usuario si las credenciales coinciden, None si no.
        """
        dto = self.session.query(AuthUserDTO).filter_by(username=username, password=password).first()
        if dto:
            return AuthUser(
                id=dto.id,
                username=dto.username,
                password=dto.password,
                role=dto.role
            )
        return None

    def get_by_id(self, user_id: int):
        dto = self.session.query(AuthUserDTO).get(user_id)
        if dto:
            return AuthUser(
                id=dto.id,
                username=dto.username,
                password=dto.password,
                role=dto.role
            )
        return None
