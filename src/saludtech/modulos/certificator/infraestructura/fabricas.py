from dataclasses import dataclass
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Repositorio
from saludtech.modulos.certificator.dominio.repositorios import RepositorioCertificacion
from .repositorios import RepositorioCertificacionSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorioCertificacion(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCertificacion.__class__:
            return RepositorioCertificacionSQL()
        else:
            raise ExcepcionFabrica(f"Repositorio {obj} no existe en la fábrica")
