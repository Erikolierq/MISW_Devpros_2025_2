from saludtech.seedwork.aplicacion.comandos import Comando
from saludtech.modulos.auth.aplicacion.dto import SesionDTO
from saludtech.modulos.auth.aplicacion.basecomando import IniciarSesionBaseHandler
from dataclasses import dataclass
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtech.modulos.auth.dominio.entities import Autenticacion
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.auth.aplicacion.mapeadores import MapeadorSesion
from saludtech.modulos.auth.infraestructura.repositorios import RepositorioAuth

@dataclass
class IniciarSesionComando(Comando):
    username: str
    password: str

class IniciarSesionHandler(IniciarSesionBaseHandler):
    
    def handle(self, comando: IniciarSesionComando):
        sesion_dto = SesionDTO(
            username=comando.username,
            password=comando.password
        )

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuth.__class__)
        sesion = repositorio.validar_credenciales(sesion_dto.username, sesion_dto.password)

        if sesion:
            return self.fabrica_auth.crear_objeto(sesion, MapeadorSesion())
        return None

@comando.register(IniciarSesionComando)
def ejecutar_comando_iniciar_sesion(comando: IniciarSesionComando):
    handler = IniciarSesionHandler()
    handler.handle(comando)
