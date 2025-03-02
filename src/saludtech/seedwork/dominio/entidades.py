"""
Módulo base para Entidades del Dominio.
"""

class EntidadBase:
    """
    Clase base para todas las entidades en DDD.
    """
    def equals(self, other):
        # Comparación genérica de identidad
        return self is other
