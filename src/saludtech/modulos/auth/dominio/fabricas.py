""" Fábricas para la creación de objetos del dominio de autenticación """

from saludtech.modulos.auth.dominio.entities import Autenticacion
from saludtech.modulos.auth.dominio.excepciones import CredencialesInvalidasExcepcion
from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaSesion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            return mapeador.dto_a_entidad(obj)

@dataclass
class FabricaAuth(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Autenticacion.__class__:
            fabrica_sesion = _FabricaSesion()
            return fabrica_sesion.crear_objeto(obj, mapeador)
        else:
            raise CredencialesInvalidasExcepcion()
