import json
from flask import Blueprint, request, jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

# Importa el despachador de comandos y queries
from seedwork.aplicacion.comandos import ejecutar_comando
from seedwork.aplicacion.queries import ejecutar_query

# Importa los commands / queries
from modulos.item_valor.aplicacion.comandos import CrearResultadoClinicoComando
from modulos.item_valor.aplicacion.queries import ObtenerResultadoClinicoQuery

item_valor_bp = Blueprint('item_valor', __name__)

@item_valor_bp.route('/results-comando', methods=['POST'])
@jwt_required()
def crear_resultado_clinico_comando():
    try:
        data = request.get_json()
        patient = data.get('patient')
        result_text = data.get('result')

        if not patient or not result_text:
            return jsonify({"msg": "Faltan campos 'patient' y 'result'"}), 400

        comando = CrearResultadoClinicoComando(patient, result_text)
        resultado = ejecutar_comando(comando)

        # resultado puede ser un dict con el nuevo ID
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

@item_valor_bp.route('/results-query/<int:result_id>', methods=['GET'])
@jwt_required()
def obtener_resultado_clinico_query(result_id):
    try:
        query = ObtenerResultadoClinicoQuery(result_id)
        resultado = ejecutar_query(query)
        if resultado:
            return jsonify(resultado), 200
        else:
            return jsonify({"msg": "Resultado no encontrado"}), 404
    except Exception as e:
        return jsonify({"msg": str(e)}), 500
