import os
import threading
from flask import Flask, jsonify
from flask_swagger import swagger
from flask_jwt_extended import JWTManager



# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import modulos.item_valor.aplicacion
    import modulos.certificator.aplicacion
    import modulos.auth.aplicacion
    import modulos.users.aplicacion

def importar_modelos_alchemy():
    import modulos.item_valor.infraestructura.dto
    import modulos.certificator.infraestructura.dto
    import modulos.auth.infraestructura.dto
    import modulos.users.infraestructura.dto

def comenzar_consumidor():
    import modulos.item_valor.infraestructura.consumidores as item_valor
    import modulos.certificator.infraestructura.consumidores as certificator
    import modulos.auth.infraestructura.consumidores as auth
    import modulos.users.infraestructura.consumidores as users

    # Suscripción a eventos
    threading.Thread(target=item_valor.suscribirse_a_eventos).start()
    threading.Thread(target=certificator.suscribirse_a_eventos).start()
    threading.Thread(target=auth.suscribirse_a_eventos).start()
    threading.Thread(target=users.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=item_valor.suscribirse_a_comandos).start()
    threading.Thread(target=certificator.suscribirse_a_comandos).start()
    threading.Thread(target=auth.suscribirse_a_comandos).start()
    threading.Thread(target=users.suscribirse_a_comandos).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'  
    app.config['JWT_TOKEN_LOCATION'] = ['headers']  
    app.config['JWT_HEADER_NAME'] = 'Authorization' 
    app.config['JWT_HEADER_TYPE'] = 'Bearer'  

    app.secret_key = 'super-secret-key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')
    jwt = JWTManager(app) 
    
    from config.db import init_db
    init_db(app)
    from config.db import db
    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

    # Importa Blueprints
    from .item_valor import item_valor_bp
    from .auth import auth_bp
    from .certificator import certificator_bp
    from .users import users_bp

    app.register_blueprint(item_valor_bp, url_prefix='/item_valor')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(certificator_bp, url_prefix='/certificator')
    app.register_blueprint(users_bp, url_prefix='/users')

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Microservices API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
