from modulos.users.aplicacion.comandos import CrearUsuarioComando, ActualizarUsuarioComando
from modulos.users.aplicacion.queries import ObtenerUsuarioQuery, ListarUsuariosQuery
from modulos.users.infraestructura.repositorios import UsersRepository
from modulos.users.infraestructura.event_publisher import EventPublisher
from modulos.users.infraestructura.uow import UnitOfWork
from modulos.users.dominio.events import UserCreatedEvent, UserUpdatedEvent
from modulos.users.dominio.entities import User

class CommandHandler:
    def __init__(self, uow: UnitOfWork, publisher: EventPublisher):
        self.uow = uow
        self.publisher = publisher

    def handle(self, comando):
        if isinstance(comando, CrearUsuarioComando):
            return self._handle_crear_usuario(comando)
        elif isinstance(comando, ActualizarUsuarioComando):
            return self._handle_actualizar_usuario(comando)
        raise ValueError("Comando desconocido")

    def _handle_crear_usuario(self, comando: CrearUsuarioComando):
        with self.uow:
            nuevo_usuario = User(
                id=None,
                username=comando.username,
                password=comando.password,  # En producción, encriptar/hash
                role=comando.role
            )
            self.uow.session.add(nuevo_usuario.to_dto())
            self.uow.session.flush()  
            # Asignar el ID autogenerado al objeto User
            nuevo_usuario.id = nuevo_usuario.to_dto().id

            event = UserCreatedEvent(
                user_id=nuevo_usuario.id,
                username=nuevo_usuario.username,
                role=nuevo_usuario.role
            )
            self.publisher.publish(event)
            return nuevo_usuario.to_dict()

    def _handle_actualizar_usuario(self, comando: ActualizarUsuarioComando):
        with self.uow:
            repo = UsersRepository(self.uow.session)
            user_entity = repo.get_by_id(comando.user_id)
            if user_entity:
                if comando.password is not None:
                    user_entity.password = comando.password
                if comando.role is not None:
                    user_entity.role = comando.role
                repo.update_user(user_entity)
                
                event = UserUpdatedEvent(
                    user_id=user_entity.id,
                    username=user_entity.username,
                    role=user_entity.role
                )
                self.publisher.publish(event)
                return user_entity.to_dict()
            return None

class QueryHandler:
    def __init__(self, repo: UsersRepository, publisher: EventPublisher):
        self.repo = repo
        self.publisher = publisher

    def handle(self, query):
        if isinstance(query, ObtenerUsuarioQuery):
            return self._handle_obtener_usuario(query)
        elif isinstance(query, ListarUsuariosQuery):
            return self._handle_listar_usuarios(query)
        raise ValueError("Query desconocida")

    def _handle_obtener_usuario(self, query: ObtenerUsuarioQuery):
        user_entity = self.repo.get_by_id(query.user_id)
        return user_entity.to_dict() if user_entity else None

    def _handle_listar_usuarios(self, query: ListarUsuariosQuery):
        lista = self.repo.list_all()
        return [u.to_dict() for u in lista]
