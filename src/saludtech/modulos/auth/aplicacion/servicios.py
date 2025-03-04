from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.auth.dominio.entities import Autenticacion
from saludtech.modulos.auth.dominio.fabricas import FabricaAuth
from saludtech.modulos.auth.infraestructura.fabricas import f
from saludtech.modulos.auth.infraestructura.repositorios import RepositorioAuth
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.auth.aplicacion.mapeadores import MapeadorSesion
from saludtech.modulos.auth.aplicacion.dto import SesionDTO

class ServicioAuth(Servicio):

    def __init__(self):
        self._fabrica_repositorio = RepositorioAuth()
        self._fabrica_auth = FabricaAuth()

    def iniciar_sesion(self, sesion_dto: SesionDTO) -> SesionDTO:
        sesion = self._fabrica_auth.crear_objeto(sesion_dto, MapeadorSesion())
        
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioAuth.__class__)
        sesion_guardada = repositorio.validar_credenciales(sesion)

        if sesion_guardada:
            return self._fabrica_auth.crear_objeto(sesion_guardada, MapeadorSesion())
        return None
