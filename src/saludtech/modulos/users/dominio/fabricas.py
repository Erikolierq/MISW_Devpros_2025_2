""" Fábricas para la creación de objetos del dominio de usuarios """

from saludtech.modulos.users.dominio.entities import Usuario
from saludtech.modulos.users.dominio.excepciones import UsuarioNoExisteExcepcion
from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaUsuario(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            return mapeador.dto_a_entidad(obj)

@dataclass
class FabricaUsuarios(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Usuario.__class__:
            fabrica_usuario = _FabricaUsuario()
            return fabrica_usuario.crear_objeto(obj, mapeador)
        else:
            raise UsuarioNoExisteExcepcion()
