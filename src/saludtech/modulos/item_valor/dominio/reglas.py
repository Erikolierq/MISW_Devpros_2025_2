"""Reglas de negocio del dominio de resultados clínicos

En este archivo encontrará reglas de negocio del dominio de resultados clínicos
"""

from saludtech.seedwork.dominio.reglas import ReglaNegocio
from saludtech.modulos.item_valor.dominio.objetos_valor import ResultadoClinico

class ResultadoClinicoValido(ReglaNegocio):
    """Regla que valida que el resultado clínico contenga datos válidos"""

    def __init__(self, resultado: ResultadoClinico, mensaje="El resultado clínico debe contener un paciente y un resultado válido."):
        super().__init__(mensaje)
        self.resultado = resultado

    def es_valido(self) -> bool:
        return bool(self.resultado.paciente and self.resultado.resultado)
