from saludtech.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtech.seedwork.aplicacion.queries import ejecutar_query as query
from saludtech.modulos.certificator.infraestructura.repositorios import RepositorioCertificacion
from dataclasses import dataclass
from saludtech.modulos.certificator.aplicacion.basequery import PermisosQueryBaseHandler
from saludtech.modulos.certificator.aplicacion.mapeadores import MapeadorPermiso

@dataclass
class ObtenerPermisoUsuario(Query):
    id_usuario: str

class ObtenerPermisoUsuarioHandler(PermisosQueryBaseHandler):

    def handle(self, query: ObtenerPermisoUsuario) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCertificacion.__class__)
        permiso = self.fabrica_permisos.crear_objeto(
            repositorio.obtener_por_usuario(query.id_usuario), 
            MapeadorPermiso()
        )
        return QueryResultado(resultado=permiso)

@query.register(ObtenerPermisoUsuario)
def ejecutar_query_obtener_permiso_usuario(query: ObtenerPermisoUsuario):
    handler = ObtenerPermisoUsuarioHandler()
    return handler.handle(query)
