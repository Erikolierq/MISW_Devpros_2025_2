from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from saludtech.modulos.users.aplicacion.comandos import CrearUsuarioComando
from saludtech.modulos.users.aplicacion.queries import ObtenerUsuario
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando
from saludtech.seedwork.aplicacion.queries import ejecutar_query

users_bp = Blueprint('users', __name__)
@users_bp.route('/', methods=['POST'])
def create_user():
    """Crea un nuevo usuario utilizando un comando."""
    data = request.get_json()

    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Se requieren 'username' y 'password'."}), 400

    try:
        comando = CrearUsuarioComando(
            username=data["username"],
            password=data["password"],
            role=data.get("role", 1)
        )
        ejecutar_commando(comando)
        return jsonify({"message": "Usuario creado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@users_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    """Obtiene información de un usuario utilizando una query."""
    query_resultado = ejecutar_query(ObtenerUsuario(user_id))
    
    if query_resultado.resultado:
        return jsonify(query_resultado.resultado.to_dict()), 200
    
    return jsonify({"message": "Usuario no encontrado"}), 404
