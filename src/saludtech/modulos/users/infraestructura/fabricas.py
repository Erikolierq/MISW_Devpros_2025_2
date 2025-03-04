from dataclasses import dataclass
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Repositorio
from saludtech.modulos.users.dominio.repositorios import RepositorioUsuarios
from .repositorios import RepositorioUsuariosSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorioUsuarios(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioUsuarios.__class__:
            return RepositorioUsuariosSQLite()
        else:
            raise ExcepcionFabrica(f"Repositorio {obj} no existe en la fábrica")
