from modulos.users.dominio.entities import User
from modulos.users.infraestructura.dto import UserDTO

class UsersRepository:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id: int):
        dto = self.session.query(UserDTO).get(user_id)
        if dto:
            return User(
                id=dto.id,
                username=dto.username,
                password=dto.password,
                role=dto.role
            )
        return None

    def list_all(self):
        dtos = self.session.query(UserDTO).all()
        return [
            User(
                id=dto.id,
                username=dto.username,
                password=dto.password,
                role=dto.role
            )
            for dto in dtos
        ]

    def update_user(self, user_entity: User):
        dto = self.session.query(UserDTO).get(user_entity.id)
        if dto:
            dto.username = user_entity.username
            dto.password = user_entity.password
            dto.role = user_entity.role
            self.session.commit()

    def add_user(self, user_entity: User):
        new_dto = UserDTO(
            username=user_entity.username,
            password=user_entity.password,
            role=user_entity.role
        )
        self.session.add(new_dto)
        self.session.flush()  # Genera ID
        user_entity.id = new_dto.id
        return new_dto
