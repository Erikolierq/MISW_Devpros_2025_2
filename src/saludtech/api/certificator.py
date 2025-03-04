from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt

certificator_bp = Blueprint('certificator', __name__)

@certificator_bp.route('/validate', methods=['GET'])
@jwt_required()
def validate():
    """Valida los permisos del usuario basado en su rol."""
    claims = get_jwt()  
    role = claims.get('role') 

    if role == 1:
        return jsonify({'allowed': False, 'message': 'Acceso denegado para rol 1'}), 403
    elif role == 2:
        return jsonify({'allowed': True, 'message': 'Acceso permitido para rol 2'}), 200

    return jsonify({'allowed': False, 'message': 'Rol desconocido'}), 403
