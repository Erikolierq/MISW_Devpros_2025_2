from modulos.certificator.aplicacion.comandos import ValidarPermisoComando
from modulos.certificator.aplicacion.queries import ObtenerPermisoQuery
from modulos.certificator.infraestructura.repositorios import CertificatorRepository
from modulos.certificator.infraestructura.event_publisher import EventPublisher
from modulos.certificator.dominio.events import PermissionValidatedEvent
from modulos.certificator.infraestructura.uow import UnitOfWork

class CommandHandler:
    def __init__(self, uow: UnitOfWork, publisher: EventPublisher):
        self.uow = uow
        self.publisher = publisher

    def handle(self, comando):
        if isinstance(comando, ValidarPermisoComando):
            return self._handle_validar_permiso_comando(comando)
        raise ValueError("Comando desconocido")

    def _handle_validar_permiso_comando(self, comando: ValidarPermisoComando):
        """
        Lógica de validación según rol.
        """
        with self.uow:
            # Regla de negocio: rol = 2 => permitido, rol = 1 => denegado, etc.
            permitido = (comando.user_role == 2)
            event = PermissionValidatedEvent(
                user_role=comando.user_role,
                allowed=permitido
            )
            self.publisher.publish(event)
            return {"allowed": permitido}

class QueryHandler:
    def __init__(self, repo: CertificatorRepository, publisher: EventPublisher):
        self.repo = repo
        self.publisher = publisher

    def handle(self, query):
        if isinstance(query, ObtenerPermisoQuery):
            return self._handle_obtener_permiso_query(query)
        raise ValueError("Query desconocida")

    def _handle_obtener_permiso_query(self, query: ObtenerPermisoQuery):
        # Ejemplo: Podrías buscar en un repositorio que mapee roles a permisos
        permiso = self.repo.get_permiso_por_rol(query.user_role)
        if permiso is not None:
            # Publicar evento o log, si aplica
            return {"role": query.user_role, "permiso": permiso}
        return None
