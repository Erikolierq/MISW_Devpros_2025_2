"""
Módulo base para elementos de la capa de presentación (API).
"""

from flask import Blueprint

def crear_blueprint(nombre, prefijo_url):
    """
    Helper para crear un Blueprint estándar.
    """
    bp = Blueprint(nombre, __name__, url_prefix=prefijo_url)
    return bp
