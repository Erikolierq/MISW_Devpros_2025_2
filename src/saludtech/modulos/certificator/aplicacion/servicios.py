from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.certificator.dominio.entidades import Permiso
from saludtech.modulos.certificator.dominio.fabricas import FabricaCertificacion
from saludtech.modulos.certificator.infraestructura.fabricas import FabricaRepositorioCertificacion
from saludtech.modulos.certificator.infraestructura.repositorios import RepositorioCertificacion
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.certificator.aplicacion.mapeadores import MapeadorPermiso
from saludtech.modulos.certificator.aplicacion.dto import PermisoDTO

class ServicioCertificator(Servicio):

    def __init__(self):
        self._fabrica_repositorio = FabricaRepositorioCertificacion()
        self._fabrica_permisos = FabricaCertificacion()

    def validar_permiso(self, permiso_dto: PermisoDTO) -> PermisoDTO:
        permiso = self._fabrica_permisos.crear_objeto(permiso_dto, MapeadorPermiso())

        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCertificacion.__class__)
        permiso_guardado = repositorio.validar_permiso(permiso)

        if permiso_guardado:
            return self._fabrica_permisos.crear_objeto(permiso_guardado, MapeadorPermiso())
        return None
