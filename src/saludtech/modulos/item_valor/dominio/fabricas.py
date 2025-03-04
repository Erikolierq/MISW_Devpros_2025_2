""" Fábricas para la creación de objetos del dominio de resultados clínicos """

from saludtech.modulos.item_valor.dominio.entidades import ResultadoClinico
from saludtech.modulos.item_valor.dominio.excepciones import ResultadoClinicoNoExisteExcepcion
from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaResultadoClinico(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            return mapeador.dto_a_entidad(obj)

@dataclass
class FabricaResultadosClinicos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == ResultadoClinico.__class__:
            fabrica_resultado = _FabricaResultadoClinico()
            return fabrica_resultado.crear_objeto(obj, mapeador)
        else:
            raise ResultadoClinicoNoExisteExcepcion()
