from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from modulos.users.aplicacion.comandos import CrearUsuarioComando
from modulos.users.aplicacion.queries import ObtenerUsuarioQuery
from seedwork.aplicacion.comandos import ejecutar_comando
from seedwork.aplicacion.queries import ejecutar_query

users_bp = Blueprint('users', __name__)
@users_bp.route('/', methods=['POST'])
def create_user():
    """Crea un nuevo usuario utilizando un comando."""
    data = request.get_json()
    
    comando = CrearUsuarioComando(
        username=data.get('username'),
        password=data.get('password'),
        role=data.get('role', 1)  
    )
    
    ejecutar_comando(comando)

    return jsonify({"message": "Usuario creado exitosamente"}), 201

@users_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    """Obtiene información de un usuario utilizando una query."""
    query_resultado = ejecutar_query(ObtenerUsuarioQuery(user_id))
    
    if query_resultado.resultado:
        return jsonify(query_resultado.resultado.to_dict()), 200
    
    return jsonify({"message": "Usuario no encontrado"}), 404
