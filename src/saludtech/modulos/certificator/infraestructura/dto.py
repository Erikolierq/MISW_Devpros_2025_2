from saludtech.config.db import db
import uuid
from datetime import datetime

class RoleValidation(db.Model):
    __tablename__ = "role_validations"
    
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    permitido = db.Column(db.Boolean, nullable=False, default=False)
    fecha_validacion = db.Column(db.DateTime, default=datetime.utcnow)
