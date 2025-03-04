from dataclasses import dataclass
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Repositorio
from saludtech.modulos.item_valor.dominio.repositorios import RepositorioResultadosClinicos
from .repositorios import RepositorioResultadosClinicosSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorioResultadosClinicos(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioResultadosClinicos.__class__:
            return RepositorioResultadosClinicosSQLite()
        else:
            raise ExcepcionFabrica(f"Repositorio {obj} no existe en la fábrica")
