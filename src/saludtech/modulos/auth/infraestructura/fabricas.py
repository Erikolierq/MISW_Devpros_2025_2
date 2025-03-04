from dataclasses import dataclass
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Repositorio
from saludtech.modulos.auth.dominio.repositorios import RepositorioAuth
from .repositorios import RepositorioAuthSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorioAuth(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAuth.__class__:
            return RepositorioAuthSQLite()
        else:
            raise ExcepcionFabrica(f"Repositorio {obj} no existe en la fábrica")
