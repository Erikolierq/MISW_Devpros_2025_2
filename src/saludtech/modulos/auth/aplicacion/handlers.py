from modulos.auth.aplicacion.comandos import LoginComando, LogoutComando
from modulos.auth.aplicacion.queries import ObtenerUsuarioPorCredencialesQuery
from modulos.auth.infraestructura.repositorios import AuthRepository
from modulos.auth.infraestructura.uow import UnitOfWork
from modulos.auth.infraestructura.event_publisher import EventPublisher
from modulos.auth.dominio.events import UserLoggedInEvent, UserLoggedOutEvent

class CommandHandler:
    def __init__(self, uow: UnitOfWork, publisher: EventPublisher):
        self.uow = uow
        self.publisher = publisher

    def handle(self, comando):
        if isinstance(comando, LoginComando):
            return self._handle_login_comando(comando)
        elif isinstance(comando, LogoutComando):
            return self._handle_logout_comando(comando)
        raise ValueError("Comando desconocido")

    def _handle_login_comando(self, comando: LoginComando):
        with self.uow:
            
            repo = AuthRepository(self.uow.session)
            user = repo.get_by_credentials(comando.username, comando.password)
            if user:
                event = UserLoggedInEvent(user_id=user.id, username=user.username)
                self.publisher.publish(event)
                return {"access_token": f"fake-jwt-{user.id}", "role": user.role}
            return None

    def _handle_logout_comando(self, comando: LogoutComando):
        with self.uow:
           
            event = UserLoggedOutEvent(user_id=comando.user_id)
            self.publisher.publish(event)
            return {"msg": "Usuario deslogueado correctamente"}

class QueryHandler:
    def __init__(self, repo: AuthRepository, publisher: EventPublisher):
        self.repo = repo
        self.publisher = publisher

    def handle(self, query):
        if isinstance(query, ObtenerUsuarioPorCredencialesQuery):
            return self._handle_obtener_usuario_por_cred(query)
        raise ValueError("Query desconocida")

    def _handle_obtener_usuario_por_cred(self, query: ObtenerUsuarioPorCredencialesQuery):
        user = self.repo.get_by_credentials(query.username, query.password)
        if user:
           
            return user.to_dict()
        return None
