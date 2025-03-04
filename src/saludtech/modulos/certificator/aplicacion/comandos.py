from saludtech.seedwork.aplicacion.comandos import Comando
from saludtech.modulos.certificator.aplicacion.dto import PermisoDTO
from saludtech.modulos.certificator.aplicacion.basecomando import ValidarPermisoBaseHandler
from dataclasses import dataclass
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtech.modulos.certificator.dominio.entidades import Permiso
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.certificator.aplicacion.mapeadores import MapeadorPermiso
from saludtech.modulos.certificator.infraestructura.repositorios import RepositorioCertificacion

@dataclass
class ValidarPermisoComando(Comando):
    user_id: str

class ValidarPermisoHandler(ValidarPermisoBaseHandler):
    
    def handle(self, comando: ValidarPermisoComando):
        permiso_dto = PermisoDTO(user_id=comando.user_id)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCertificacion.__class__)
        permiso = repositorio.validar_permiso(permiso_dto.user_id)

        if permiso:
            return self.fabrica_permisos.crear_objeto(permiso, MapeadorPermiso())
        return None

@comando.register(ValidarPermisoComando)
def ejecutar_comando_validar_permiso(comando: ValidarPermisoComando):
    handler = ValidarPermisoHandler()
    handler.handle(comando)
