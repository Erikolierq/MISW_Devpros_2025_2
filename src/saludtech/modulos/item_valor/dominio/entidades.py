from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from saludtech.modulos.item_valor.dominio.events import ResultadoClinicoCreado
from saludtech.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class ResultadoClinico(AgregacionRaiz):
    patient: str
    result_text: str

    def crear_resultado_clinico(self, resultado: ResultadoClinico):
        self.patient = resultado.patient
        self.result_text = resultado.result_text

        self.agregar_evento(ResultadoClinicoCreado(id_resultado=self.id, patient=self.patient, result_text=self.result_text))
