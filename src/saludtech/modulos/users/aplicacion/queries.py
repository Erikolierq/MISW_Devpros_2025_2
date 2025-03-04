from saludtech.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtech.seedwork.aplicacion.queries import ejecutar_query as query
from saludtech.modulos.users.infraestructura.repositorios import RepositorioUsuarios
from dataclasses import dataclass
from saludtech.modulos.users.aplicacion.basequery import UsuarioQueryBaseHandler
from saludtech.modulos.users.aplicacion.mapeadores import MapeadorUsuario

@dataclass
class ObtenerUsuario(Query):
    id: str

class ObtenerUsuarioHandler(UsuarioQueryBaseHandler):

    def handle(self, query: ObtenerUsuario) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)
        usuario = self.fabrica_usuarios.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorUsuario())
        return QueryResultado(resultado=usuario)

@query.register(ObtenerUsuario)
def ejecutar_query_obtener_usuario(query: ObtenerUsuario):
    handler = ObtenerUsuarioHandler()
    return handler.handle(query)
