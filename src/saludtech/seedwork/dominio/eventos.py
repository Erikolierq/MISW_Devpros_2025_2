"""
Módulo base para eventos de dominio.
"""
import json
import datetime

class EventoDominioBase:
    """
    Evento de dominio genérico.
    """
    def __init__(self, nombre, datos, version=1):
        self.nombre = nombre
        self.datos = datos
        self.version = version
        self.timestamp = datetime.datetime.utcnow().isoformat()

    def to_json(self):
        return json.dumps({
            "nombre": self.nombre,
            "datos": self.datos,
            "version": self.version,
            "timestamp": self.timestamp
        })
