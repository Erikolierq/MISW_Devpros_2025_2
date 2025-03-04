from saludtech.config.db import db
import uuid
from datetime import datetime

class AuthLog(db.Model):
    __tablename__ = "auth_logs"
    
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(500), nullable=False)
    fecha_login = db.Column(db.DateTime, default=datetime.utcnow)
