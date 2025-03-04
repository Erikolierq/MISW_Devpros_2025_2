""" Fábricas para la creación de objetos del dominio de certificación """

from saludtech.modulos.certificator.dominio.entidades import Permiso
from saludtech.modulos.certificator.dominio.excepciones import PermisoDenegadoExcepcion
from seedwork.dominio.repositorios import Mapeador
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaCertificacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            return mapeador.dto_a_entidad(obj)

@dataclass
class FabricaCertificacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Permiso.__class__:
            fabrica_certificacion = _FabricaCertificacion()
            return fabrica_certificacion.crear_objeto(obj, mapeador)
        else:
            raise PermisoDenegadoExcepcion()
