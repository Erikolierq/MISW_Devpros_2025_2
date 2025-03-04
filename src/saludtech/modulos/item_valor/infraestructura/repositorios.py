""" Repositorio de persistencia para resultados clínicos """

from saludtech.config.db import db
from saludtech.modulos.item_valor.dominio.repositorios import RepositorioResultadosClinicos
from saludtech.modulos.item_valor.dominio.entidades import ResultadoClinico
from saludtech.modulos.item_valor.dominio.fabricas import FabricaResultadosClinicos
from saludtech.modulos.item_valor.infraestructura.dto import ClinicalResult as ResultadoClinicoDTO
from saludtech.modulos.item_valor.infraestructura.mapeadores import MapeadorResultadoClinico
from uuid import UUID

class RepositorioResultadosClinicosSQLite(RepositorioResultadosClinicos):

    def __init__(self):
        self._fabrica_resultados: FabricaResultadosClinicos = FabricaResultadosClinicos()

    @property
    def fabrica_resultados(self):
        return self._fabrica_resultados

    def obtener_por_id(self, id: UUID) -> ResultadoClinico:
        resultado_dto = db.session.query(ResultadoClinicoDTO).filter_by(id=str(id)).one_or_none()
        return self.fabrica_resultados.crear_objeto(resultado_dto, MapeadorResultadoClinico()) if resultado_dto else None

    def obtener_todos(self) -> list[ResultadoClinico]:
        resultados_dto = db.session.query(ResultadoClinicoDTO).all()
        return [self.fabrica_resultados.crear_objeto(resultado, MapeadorResultadoClinico()) for resultado in resultados_dto]

    def agregar(self, resultado: ResultadoClinico):
        resultado_dto = self.fabrica_resultados.crear_objeto(resultado, MapeadorResultadoClinico())
        db.session.add(resultado_dto)
        db.session.commit()
