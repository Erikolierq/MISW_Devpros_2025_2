from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from modulos.auth.aplicacion.queries import ObtenerUsuarioPorCredencialesQuery
from seedwork.aplicacion.queries import ejecutar_query
import time

auth_bp = Blueprint('auth', __name__)

limiter = Limiter(get_remote_address, default_limits=[])

failed_attempts = {}
blocked_ips = {}

MAX_ATTEMPTS = 5  
BLOCK_TIME = 300  

@limiter.limit("10 per minute")
@auth_bp.route('/login', methods=['POST'])
def login():
    """Autentica un usuario y genera un token JWT sin uso de Redis."""
    ip_address = get_remote_address()

    if ip_address in blocked_ips:
        remaining_time = blocked_ips[ip_address] - time.time()
        if remaining_time > 0:
            return jsonify({"error": "IP bloqueada. Intenta más tarde.", "bloqueo_expira_en": int(remaining_time)}), 403
        else:
            del blocked_ips[ip_address] 

    data = request.json
    username = data.get("username")
    password = data.get("password")

    query_resultado = ejecutar_query(ObtenerUsuarioPorCredencialesQuery(username, password))

    if query_resultado is None or query_resultado.resultado is None:
        
        failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1

        if failed_attempts[ip_address] >= MAX_ATTEMPTS:
            blocked_ips[ip_address] = time.time() + BLOCK_TIME 
            return jsonify({"error": "Demasiados intentos fallidos. IP bloqueada por 5 minutos."}), 403

        return jsonify({
            "error": "Usuario o contraseña incorrectos.",
            "intentos_restantes": MAX_ATTEMPTS - failed_attempts[ip_address]
        }), 401

    user = query_resultado.resultado
    token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})

    failed_attempts.pop(ip_address, None)

    return jsonify(access_token=token), 200

